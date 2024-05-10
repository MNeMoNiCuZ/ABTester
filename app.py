from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session  # Import Flask-Session
from random import shuffle
import os
import random
import webbrowser

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Flask-Session configuration
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem for server-side session
app.config['SESSION_PERMANENT'] = False  # Sessions are not permanent
app.config['SESSION_FILE_DIR'] = 'flask_session_data'  # Directory to store session files
app.config['SESSION_FILE_THRESHOLD'] = 100  # Number of session files to store before cleaning up

# Initialize Session with the app
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = ''
    warning_message = ''
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    INPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'INPUT')
    total_images = len(os.listdir(INPUT_FOLDER))

    if request.method == 'POST':
        num_sets = int(request.form['num_sets'])

        if total_images == 0:
            error_message = 'No images found in the INPUT folder.'
        elif num_sets > total_images:
            error_message = 'Number of sets cannot be greater than the total number of images.'
        elif total_images % num_sets != 0:
            warning_message = 'The total number of images is not evenly divisible by the number of sets.'

        if not error_message:
            session['num_sets'] = num_sets
            image_files = sorted(os.listdir(INPUT_FOLDER))
            image_sets = [image_files[i:i + num_sets] for i in range(0, len(image_files), num_sets)]
            session['image_sets'] = image_sets
            session['current_set'] = 0
            session['stats'] = [0] * num_sets
            session['set_viewed_count'] = 0  # Ensure it starts at 0
            session['reshuffle_count'] = 1  # Reset the reshuffle count here
            return redirect(url_for('display_set'))

    return render_template('index.html', error_message=error_message, warning_message=warning_message, total_images=total_images)

@app.route('/display_set', methods=['GET', 'POST'])
def display_set():
    current_set = session.get('current_set', 0)
    total_sets = len(session['image_sets'])
    selected_set = request.args.get('selected_img', None)
    skip = request.args.get('skip', None) == 'true'
    stats_visibility = request.args.get('stats_visibility', 'hidden')
    message = None  # Ensuring message is initialized

    print(f"Current Set (before any action): {current_set}, Total Sets: {total_sets}")

    # Increment set_viewed_count immediately after a vote or skip action
    if selected_set or skip:
        session['set_viewed_count'] = session.get('set_viewed_count', 0) + 1
        print(f"Set Viewed Count incremented to: {session['set_viewed_count']}")

    # Handle voting, only if a set is selected and not skipping
    if selected_set and not skip:
        selected_set = int(selected_set) - 1
        if 0 <= selected_set < len(session['stats']):
            session['stats'][selected_set] += 1
            print(f"Vote registered for image set index {selected_set}, current votes: {session['stats'][selected_set]}")

    # Manage set transitions and reshuffling
    if current_set == total_sets - 1:
        message = f"All images have been viewed. Entering round {session.get('reshuffle_count', 1) + 1} of voting."
        shuffle(session['image_sets'])
        session['current_set'] = 0
        session['set_viewed_count'] = 0  # Resetting viewed set count for the new round
        reshuffle_count = session.get('reshuffle_count', 1)
        reshuffle_count += 1
        session['reshuffle_count'] = reshuffle_count
        print(f"Reshuffling image sets: New round {reshuffle_count}")
    else:
        session['current_set'] += 1
        print(f"Moving to next set: {session['current_set']} (zero-indexed)")

    images_to_display = session['image_sets'][current_set]
    images_with_set_numbers = list(zip(range(1, len(images_to_display) + 1), images_to_display))
    random.shuffle(images_with_set_numbers)
    shuffled_set_numbers, shuffled_images_to_display = zip(*images_with_set_numbers)
    
    print(f"Displaying images from set: {current_set + 1}")
    
    return render_template('display_set.html', 
                           images_and_set_numbers=zip(shuffled_set_numbers, shuffled_images_to_display),
                           stats=session['stats'], 
                           stats_visibility=stats_visibility, 
                           message=message,
                           set_viewed_count=session.get('set_viewed_count', 0) + 1,  # Ensure it's user-friendly
                           total_sets=total_sets)
@app.route('/stats', methods=['GET'])
def stats():
    return render_template('stats.html', stats=session.get('stats', []), all_sets=session.get('all_sets', []))

if __name__ == "__main__":
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://localhost:5000/", new=1)  # This line opens the web browser
    app.run(debug=True)
