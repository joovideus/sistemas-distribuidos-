import eventlet
eventlet.monkey_patch() 

from flask import Flask
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'
socketio = SocketIO(app, cors_allowed_origins="*")

LOG_FILE = 'mensagens.txt'

@app.route('/')
def index():
    return "Servidor WebSocket ativo..."

@socketio.on('message')
def handle_message(msg):
    hora = datetime.now().strftime('%H:%M:%S')
    mensagem_formatada = f"[{hora}] {msg}"
    print(mensagem_formatada)
    
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(mensagem_formatada + '\n')
    
    send(mensagem_formatada, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3035)
