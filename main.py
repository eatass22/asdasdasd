from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# store messages (just temporary memory)
chat_history = []

@app.route("/")
def index():
    return "Chat server is running 😎"

@socketio.on("send_message")
def handle_send_message(data):
    message = data.get("message")
    username = data.get("username", "anon")
    if message:
        chat_history.append({"user": username, "message": message})
        emit("receive_message", {"user": username, "message": message}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
