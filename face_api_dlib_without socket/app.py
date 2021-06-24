from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/ab')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()