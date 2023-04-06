# Import required Flask modules
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room, Namespace
from waitress import serve
import psycopg2
from classes.room import Room
from classes.client import Client

# Create Flask application instance
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your-secret-key'

# Set up SocketIO
socketio = SocketIO(app)

# Define database schema

# # Establish a connection to the database
# conn = psycopg2.connect(
#     host="database-1.cvkpaldfli6u.us-east-1.rds.amazonaws.com",
#     port=5432,
#     database="database_name123",
#     user="postgres123",
#     password="Password123",
# )
# conn.close()

@socketio.on('connect')
def handle_connect():
    print('A new client connected')

@socketio.on('my_event')
def handle_message(data):
    recieved_data = data['data']
    print('Received data:', recieved_data)
    socketio.emit('server_response', {'data': recieved_data})


# @app.route('/create_room', methods=['POST'])
# def create_room():
#     room_id = len(rooms) + 1
#     room = Room(room_id)
#     rooms[room_id] = room
#     emit('room_created', room_id)
#     return ''

# @app.route('/join_room', methods=['POST'])
# def join_room():
#     room_id = int(request.form['room_id'])
#     if room_id in rooms:
#         room = rooms[room_id]
#         room.add_client(request.sid)
#         emit('room_joined', room_id)
#     else:
#         emit('room_not_found', room_id)
#     return ''

# Define routes for creating and playing quizzes
@app.route('/')
def home():
    return render_template('home.html')

# Run the application
if __name__ == '__main__':
    socketio.run(app, debug=True, host='10.0.0.155', port=8000) # wifi ip address here
