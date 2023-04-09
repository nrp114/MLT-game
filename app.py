# Import required Flask modules
from flask import Flask, render_template,jsonify
from flask_socketio import SocketIO
import string
import random

# Create Flask application instance
app = Flask(__name__, template_folder='templates', static_folder='client/build', static_url_path='/')
app.config['SECRET_KEY'] = 'your-secret-key'

# Set up SocketIO
socketio = SocketIO(app)

# dictionary of rooms and players id inside the room
roomDict = {}


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


@socketio.on('create_room')
def handle_message(data):
    print('Create Room')
    print(data)
    create_room(data['socketId'])
    print('Rooms: ', roomDict)
    socketio.emit('server_response_cr', roomDict)


@socketio.on('enter_room')
def handle_message(data):
    print(data)
    roomId = data['roomId']
    if roomId not in roomDict:
        print("Error")
        socketio.emit('server_response_er', "Error")
        return
    print('Room Id:', roomId)
    socketId = data['socketId']
    roomDict[roomId].append(socketId)
    print('Rooms: ', roomDict)
    socketio.emit('server_response', roomDict)


@app.route('/create_room', methods=['POST'])
def create_room(id):
    new_room_code = generate_random_code(6, roomDict)
    roomDict[new_room_code] = [id]
    return new_room_code


def generate_random_code(length, roomDict):
    # Define the possible characters for the code
    characters = string.ascii_uppercase + string.digits

    # Generate the random code
    while True:
        # Generate the random code
        code = ''.join(random.choices(characters, k=length))

        # Check if the code is not in the dictionary
        if code not in roomDict:
            break

    return code


@app.route('/join_room', methods=['POST'])
def join_room():
    room_id = int(request.form['room_id'])
    if room_id in rooms:
        room = rooms[room_id]
        room.add_client(request.sid)
        emit('room_joined', room_id)
    else:
        emit('room_not_found', room_id)
    return ''


# Define routes for creating and playing quizzes
@app.route('/')
def home():
    return render_template('home.html')


# Run the application
if __name__ == '__main__':
    socketio.run(app, debug=True, host='192.168.1.3', port=8000) # wifi ip address here
