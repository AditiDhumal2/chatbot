import spacy
import pyjokes
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    doc = nlp(user_input.lower())

    if "your name" in user_input.lower():
        return "I'm InfoBot, your smart assistant!"
    elif any(token.lemma_ == "weather" for token in doc):
        return "I can't fetch weather yet, but I'm learning!"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a nice day 😊"
    elif "hello" in user_input.lower():
        return "Hi there! How can I help you today?"

    elif "time" in user_input.lower():

        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "joke" in user_input.lower():
         return pyjokes.get_joke()

    else:
        return "Sorry, I didn't understand that."
