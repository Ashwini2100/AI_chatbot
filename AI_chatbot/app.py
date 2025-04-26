from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API Key (keep it secret)
genai.configure(api_key="AIzaSyBrXtLqo3zBQq2Qutq8fCuTt9tR9VIlWIo")

# Load Gemini Model
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')  # this loads your futuristic HTML page

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    try:
        response = model.generate_content(user_message)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
