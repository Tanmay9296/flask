from flask import Flask, jsonify, render_template
import subprocess
import webbrowser
import time

app = Flask(__name__)

chatbot_process = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-chatbot', methods=['GET'])
def start_chatbot():
    global chatbot_process

    try:
        chatbot_process = subprocess.Popen(['python', 'chatbot.py'])
        time.sleep(3)  # Wait for the chatbot to start
        return jsonify({'message': 'Chatbot started successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
