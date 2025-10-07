from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import pyjokes
from datetime import datetime
import subprocess
import sys

app = Flask(__name__)
# Enable CORS for all origins and methods
CORS(app)

# Load spaCy NLP model (with error handling)
try:
    nlp = spacy.load("en_core_web_sm")
    print("✅ spaCy model loaded successfully")
except OSError:
    print("⚠️  Downloading spaCy model...")
    try:
        subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], check=True)
        nlp = spacy.load("en_core_web_sm")
        print("✅ spaCy model downloaded and loaded successfully")
    except Exception as e:
        print(f"❌ Error downloading spaCy model: {e}")
        nlp = None

def get_response(user_input):
    if not user_input:
        return "Please send a message!"
        
    user_input_lower = user_input.lower()
    
    # If spaCy model failed to load, use simple keyword matching
    if nlp is None:
        return simple_response(user_input_lower)
    
    try:
        doc = nlp(user_input_lower)

        if "your name" in user_input_lower:
            return "I'm InfoBot, your smart assistant!"

        elif any(token.lemma_ == "weather" for token in doc):
            return "I can't fetch weather yet, but I'm learning!"

        elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
            return "Goodbye! Have a nice day 😊"

        elif any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
            return "Hi there! How can I help you today?"

        elif any(token.lemma_ == "time" for token in doc):
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

        elif any(token.lemma_ == "joke" for token in doc):
            return pyjokes.get_joke()

        elif "how are you" in user_input_lower:
            return "I'm just a bunch of code, but I'm feeling smart today! How about you?"

        elif "thank" in user_input_lower:
            return "You're welcome! 😊"

        elif "help" in user_input_lower:
            return "Sure! I can tell you the time, crack a joke, or just chat with you!"

        elif "what can you do" in user_input_lower:
            return "I can chat, tell jokes, give the current time, and more. Try asking me!"

        elif "who made you" in user_input_lower:
            return "I was created by a smart human like you using Python and spaCy!"

        else:
            return "Sorry, I didn't understand that. Try asking me about the time, a joke, or just say hi!"
    
    except Exception as e:
        print(f"Error in NLP processing: {e}")
        return simple_response(user_input_lower)

def simple_response(user_input_lower):
    """Fallback response without spaCy"""
    if "hello" in user_input_lower or "hi" in user_input_lower or "hey" in user_input_lower:
        return "Hi there! How can I help you today?"
    elif "time" in user_input_lower:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    elif "joke" in user_input_lower:
        return pyjokes.get_joke()
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Goodbye! Have a nice day 😊"
    elif "thank" in user_input_lower:
        return "You're welcome! 😊"
    elif "how are you" in user_input_lower:
        return "I'm just a bunch of code, but I'm feeling smart today! How about you?"
    elif "your name" in user_input_lower:
        return "I'm InfoBot, your smart assistant!"
    elif "help" in user_input_lower or "what can you do" in user_input_lower:
        return "Sure! I can tell you the time, crack a joke, or just chat with you!"
    else:
        return "Sorry, I didn't understand that. Try asking me about the time, a joke, or just say hi!"

@app.route('/chat/api', methods=['POST', 'OPTIONS'])
def chat():
    try:
        if request.method == 'OPTIONS':
            return '', 200
            
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"reply": "Please provide a message"}), 400
        
        user_input = data.get("message")
        print(f"Received message: {user_input}")
        
        reply = get_response(user_input)
        return jsonify({"reply": reply})
    
    except Exception as e:
        print(f"Error in chat route: {str(e)}")
        return jsonify({"reply": "Sorry, something went wrong on the server."}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy", 
        "message": "Server is running",
        "spacy_loaded": nlp is not None
    })

@app.route('/')
def home():
    return jsonify({
        "message": "Chatbot API is running!",
        "endpoints": {
            "chat": "POST /chat/api",
            "health": "GET /health"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)