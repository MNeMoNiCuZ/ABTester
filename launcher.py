import webbrowser
import subprocess

# Launch the Flask app in a new terminal
subprocess.Popen(["python", "app.py"])

# Open the web browser to the Flask application
webbrowser.open("http://localhost:5000/", new=2)
