# Import required Flask modules
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
from waitress import serve
import psycopg2

# Create Flask application instance
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your-secret-key'

# Set up SocketIO
socketio = SocketIO(app)

# Define database schema

# Establish a connection to the database
conn = psycopg2.connect(
    host="mlt-game-public.cvkpaldfli6u.us-east-1.rds.amazonaws.com",
    port=5432,
    database="mlt-game-public",
    user="postgress",
    password="Password123",
)

# Create a cursor object
cur = conn.cursor()

# Execute a SQL query
cur.execute("SELECT * FROM your_table_name")

# Fetch the results
results = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()


# Define routes for creating and playing quizzes
@app.route('/')
def home():
    return render_template('home.html')

# Run the application
if __name__ == '__main__':
    socketio.run(app, debug=True, host='10.0.0.155', port=8000) # wifi ip address here
