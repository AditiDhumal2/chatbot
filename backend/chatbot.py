import spacy
import pyjokes
from datetime import datetime
import subprocess

# Load spaCy NLP model (with auto-download if missing)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    user_input_lower = user_input.lower()
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

# Example usage
if __name__ == "__main__":
    print("InfoBot 🤖 at your service! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print("Bot:", response)

