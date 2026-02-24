import nltk
import random
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

bank_data = {
    "greeting": [
        "Hello! Welcome to ABC Bank. How can I help you today?",
        "Hi there! How may I assist you?"
    ],
    "account_opening": "You can open a savings or current account by visiting our nearest branch or applying online through our website.",
    "balance": "To check your account balance, please login to internet banking or use our mobile banking app.",
    "loan": "We provide Home Loans, Personal Loans, Car Loans, and Education Loans. Please specify which loan you are interested in.",
    "credit_card": "We offer various credit cards with cashback and reward benefits. Would you like to apply?",
    "atm": "You can withdraw cash, check balance, and deposit money at our ATMs.",
    "working_hours": "Our bank operates Monday to Friday from 9 AM to 5 PM.",
    "internet_banking": "You can register for internet banking on our website by clicking on 'New User Registration'.",
    "complaint": "Please provide your registered mobile number to file a complaint.",
    "thanks": "You're welcome! Is there anything else I can help you with?",
    "goodbye": "Thank you for banking with ABC Bank. Have a great day!"
}


def preprocess(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(sentence)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def chatbot_response(user_input):
    tokens = preprocess(user_input)

    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return random.choice(bank_data["greeting"])

    elif "open" in tokens and "account" in tokens:
        return bank_data["account_opening"]

    elif "balance" in tokens:
        return bank_data["balance"]

    elif "loan" in tokens:
        return bank_data["loan"]

    elif "credit" in tokens or "card" in tokens:
        return bank_data["credit_card"]

    elif "atm" in tokens:
        return bank_data["atm"]

    elif "hour" in tokens or "time" in tokens:
        return bank_data["working_hours"]

    elif "internet" in tokens or "online" in tokens:
        return bank_data["internet_banking"]

    elif "complaint" in tokens or "issue" in tokens:
        return bank_data["complaint"]

    elif "thank" in tokens or "thanks" in tokens or "thank you" in tokens:
        return bank_data["thanks"]

    elif "bye" in tokens or "exit" in tokens:
        return bank_data["goodbye"]

    else:
        return "I'm sorry, I didn't understand your query. Please contact customer support at 1800-000-000."

# Main program
print("=======================================")
print("   Welcome to ABC Bank Chatbot")
print("   Type 'bye' to exit")
print("=======================================")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if "bye" in user_input.lower():
        break


