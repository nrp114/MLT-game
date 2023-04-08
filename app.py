# Import required Flask modules
from flask import Flask, render_template,jsonify
from flask_socketio import SocketIO
from classes.room import Room
from classes.client import Client

# Create Flask application instance
app = Flask(__name__, template_folder='templates', static_folder='client/build', static_url_path='/')
app.config['SECRET_KEY'] = 'your-secret-key'

# Set up SocketIO
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('A new client connected')

@app.route('/data')
def get_data():
    data = {'foo': 'bar'}
    return jsonify(data)

@socketio.on('newOptions')
def handle_message(data):
    socketio.emit('optionReceive', data = {'options': data}, include_self=False)


@socketio.on('my_event')
def handle_message(data):
    recieved_data = data['data']
    print('Received data:', recieved_data)
    socketio.emit('server_response', {'data': recieved_data})

# Define routes for creating and playing quizzes
@app.route('/')
def home():
    return render_template('home.html')

# Run the application
if __name__ == '__main__':
    socketio.run(app, debug=True, host='10.0.0.155', port=8000) # wifi ip address here
