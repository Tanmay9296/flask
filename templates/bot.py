from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure Gemini API
API_KEY = "AIzaSyAgXFaOzglQTkId2U-gVNpdvaO4oxwYjtQ"  # Replace with your API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bot.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '').strip()

        if not user_input:
            return jsonify({'response': "⚠️ Please enter a valid message."}), 400

        response = model.generate_content(user_input)
        bot_response = response.text.strip() if response.text else "⚠️ No response generated."

        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'response': f"⚠️ Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)
