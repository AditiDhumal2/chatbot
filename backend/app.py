from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.chatbot import get_response

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests (for frontend connection)

@app.route('/chat/api', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    reply = get_response(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
