from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
