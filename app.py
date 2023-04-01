# Import required Flask modules
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
from waitress import serve

# Create Flask application instance
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your-secret-key'

# Set up SocketIO
socketio = SocketIO(app)

# Define database schema
# ...

# Define routes for creating and playing quizzes
@app.route('/')
def home():
    return render_template('home.html')

# Run the application
if __name__ == '__main__':
    socketio.run(app, debug=True, host='10.0.0.155', port=8000) # wifi ip address here
