from flask import Flask, redirect, url_for, session, request
from services.chatbot import ChatBotService
from services.auth import GoogleAuthService
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize services
chatbot_service = ChatBotService()
auth_service = GoogleAuthService(app)

# Logging configuration
logging.basicConfig(level=logging.INFO)

@app.route('/login')
def login():
    return auth_service.login()

@app.route('/logout')
def logout():
    return auth_service.logout()

@app.route('/auth')
def auth():
    return auth_service.authorize()

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('chatbot'))
    return redirect(url_for('login'))

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        assistant_reply = chatbot_service.get_response(user_input)
        return jsonify({"reply": assistant_reply})

    return '''
        <h1>Chat with the AI Assistant</h1>
        <form method="post">
            <textarea name="user_input" rows="5"></textarea><br>
            <input type="submit" value="Send">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
