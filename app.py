from flask import Flask, render_template, request, redirect, url_for, session
from random import shuffle
import os
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

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
            return redirect(url_for('display_set'))

    return render_template('index.html', error_message=error_message, warning_message=warning_message, total_images=total_images)






@app.route('/display_set', methods=['GET', 'POST'])
def display_set():
    current_set = session.get('current_set', 0)
    selected_set = request.args.get('selected_img', None)  # Changed from 'selected_set' to 'selected_img'
    stats_visibility = request.args.get('stats_visibility', session.get('stats_visibility', 'hidden'))

    session['stats_visibility'] = stats_visibility
    
    if selected_set:
        selected_set = int(selected_set) - 1  # Convert to zero-based index
        if 0 <= selected_set < len(session['stats']):  # Check to make sure the index is valid
            session['stats'][selected_set] += 1
        else:
            print(f"Invalid set selected: {selected_set + 1}")  # Debugging line

    # Cycle through the sets
    session['current_set'] = (current_set + 1) % len(session['image_sets'])
    current_set = session.get('current_set', 0)

    # Shuffle the image sets when the last set is reached and we are resetting to the first set
    if current_set == 0:
        shuffle(session['image_sets'])  # Shuffling the image sets
    
    images_to_display = session['image_sets'][current_set]
    images_with_set_numbers = list(zip(range(1, len(images_to_display) + 1), images_to_display))
    random.shuffle(images_with_set_numbers)
    shuffled_set_numbers, shuffled_images_to_display = zip(*images_with_set_numbers)
    
    return render_template('display_set.html', images_and_set_numbers=zip(shuffled_set_numbers, shuffled_images_to_display), stats=session.get('stats', []), stats_visibility=stats_visibility)



@app.route('/stats', methods=['GET'])
def stats():
    return render_template('stats.html', stats=session.get('stats', []), all_sets=session.get('all_sets', []))

if __name__ == "__main__":
    app.run(debug=True)
