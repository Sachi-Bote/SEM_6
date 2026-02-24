import nltk
import random
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# =========================================
# TRAIN DATABASE
# =========================================

train_data = {
    "12951": {
        "name": "Mumbai Rajdhani Express",
        "route": ["Mumbai", "Surat", "Vadodara", "Kota", "New Delhi"],
        "arrival": "18:30",
        "departure": "18:40",
        "days": "Mon, Wed, Fri",
        "classes": ["1A", "2A", "3A"],
        "fare": {"1A": 3200, "2A": 2100, "3A": 1500},
        "delay": "On Time"
    },
    "12627": {
        "name": "Karnataka Express",
        "route": ["Bangalore", "Guntakal", "Bhopal", "Agra", "New Delhi"],
        "arrival": "06:15",
        "departure": "06:25",
        "days": "Daily",
        "classes": ["SL", "3A", "2A"],
        "fare": {"SL": 800, "3A": 1800, "2A": 2500},
        "delay": "30 Minutes Late"
    }
}

# =========================================
# EXTENSIVE FAQ DATABASE
# =========================================

faq_data = {
    "refund policy": "Refund depends on cancellation timing. Higher deduction applies closer to departure.",
    "ticket cancellation": "Tickets can be cancelled online via IRCTC or at railway reservation counter.",
    "tatkal booking": "Tatkal opens one day before departure at 10 AM for AC and 11 AM for Non-AC classes.",
    "luggage rules": "Sleeper class allows 40kg free luggage. AC classes allow up to 50kg.",
    "id proof required": "Valid government ID like Aadhaar, PAN, Passport, Driving License is mandatory.",
    "platform ticket price": "Platform ticket price ranges from Rs.10 to Rs.50 depending on station.",
    "senior citizen concession": "Concession depends on railway policy and may not apply for all bookings.",
    "child ticket rules": "Children below 5 travel free without seat. 5–12 years require child fare.",
    "rac meaning": "RAC means Reservation Against Cancellation. You will share a berth.",
    "waiting list meaning": "Waiting list tickets confirm only if seats become available.",
    "chart preparation time": "Chart is prepared approximately 4 hours before train departure.",
    "e ticket rules": "E-ticket requires valid ID during travel.",
    "counter ticket": "Counter tickets can be purchased from railway reservation counters.",
    "break journey": "Break journey is allowed under certain conditions for long distance travel.",
    "train delay": "Train delay status can be checked via PNR or train number.",
    "coach position": "Coach position is displayed on station boards and railway apps.",
    "wifi facility": "Free WiFi is available at major railway stations.",
    "food facility": "Food is available onboard and via e-catering services.",
    "divyang facility": "Wheelchair and assistance services are available at stations.",
    "lost and found": "Lost items can be reported at station master office or railway police.",
    "travel insurance": "Optional travel insurance is available during online booking.",
    "helpline number": "Railway helpline number is 139 for general enquiry.",
    "women safety": "Women safety helpline is 182.",
    "boarding station change": "Boarding station can be changed online before chart preparation.",
    "ticket upgrade": "Ticket upgrade depends on seat availability.",
    "group booking": "Group booking requires special approval for large passengers.",
    "reservation period": "Advance reservation opens 120 days before departure.",
    "irctc login issue": "Reset password using registered mobile number or email.",
    "train route information": "Train route shows all intermediate stations between source and destination.",
    "seat types": "Common seat types include SL, 3A, 2A, 1A, CC, EC."
}

faq_questions = list(faq_data.keys())
faq_answers = list(faq_data.values())

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)

# =========================================
# NLP PREPROCESS
# =========================================

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return " ".join(tokens)

# =========================================
# TRAIN FUNCTIONS
# =========================================

def search_train(train_no):
    train = train_data[train_no]
    return f"""
Train Number: {train_no}
Name: {train['name']}
Arrival: {train['arrival']}
Departure: {train['departure']}
Running Days: {train['days']}
Route: {' -> '.join(train['route'])}
Classes: {', '.join(train['classes'])}
Delay Status: {train['delay']}
"""

def check_fare(train_no):
    fares = train_data[train_no]["fare"]
    return "\n".join([f"{cls}: Rs.{fare}" for cls, fare in fares.items()])

def seat_availability():
    return f"Available Seats: {random.randint(0,100)}"

def check_pnr():
    return f"PNR Status: {random.choice(['Confirmed', 'RAC', 'Waiting List 5'])}"

def book_ticket():
    train_no = input("Enter Train Number: ")

    if train_no not in train_data:
        return "Invalid Train Number."

    train = train_data[train_no]

    print(f"\nTrain Selected: {train['name']}")
    print("Available Classes:", ", ".join(train["classes"]))

    travel_class = input("Enter Class: ").upper()

    if travel_class not in train["fare"]:
        return "Invalid Class Selected."

    adult_count = int(input("Enter Number of Adults: "))
    child_count = int(input("Enter Number of Children (5-12 yrs): "))

    adult_fare = train["fare"][travel_class]
    child_fare = adult_fare * 0.5   # 50% discount

    total_adult_cost = adult_fare * adult_count
    total_child_cost = child_fare * child_count

    total_amount = total_adult_cost + total_child_cost

    print("\n----- Fare Details -----")
    print(f"Adult Fare per ticket: Rs.{adult_fare}")
    print(f"Child Fare per ticket (50%): Rs.{child_fare}")
    print(f"Total Adult Cost: Rs.{total_adult_cost}")
    print(f"Total Child Cost: Rs.{total_child_cost}")
    print(f"Total Payable Amount: Rs.{total_amount}")

    confirm = input("\nDo you want to confirm booking? (yes/no): ").lower()

    if confirm != "yes":
        return "Booking Cancelled."

    print("\nProcessing Payment...")
    payment_method = input("Enter Payment Method (Card/UPI/NetBanking): ")

    print("Payment Successful via", payment_method)

    booking_id = random.randint(100000, 999999)
    seat_numbers = [random.randint(1, 72) for _ in range(adult_count + child_count)]

    return f"""
🎟 BOOKING CONFIRMED 🎟
Booking ID: {booking_id}
Train: {train['name']}
Class: {travel_class}
Total Passengers: {adult_count + child_count}
Seat Numbers: {seat_numbers}
Total Paid: Rs.{total_amount}

Thank you for booking with Smart Railway Assistant 🚆
"""

# =========================================
# FAQ MATCHING
# =========================================

def answer_faq(user_input):
    processed_input = preprocess(user_input)
    user_vec = vectorizer.transform([processed_input])
    similarity = cosine_similarity(user_vec, faq_vectors)
    index = similarity.argmax()
    if similarity[0][index] > 0.3:
        return faq_answers[index]
    return None


# =========================================
# GREETING & EXIT TOKENS
# =========================================

greeting_inputs = ["hi", "hello", "hey", "good morning", "good evening"]
greeting_responses = [
    "Hello! How can I assist you today?",
    "Hi there! Welcome to Smart Railway Assistant 🚆",
    "Greetings! How may I help you?"
]

exit_inputs = ["bye", "goodbye", "thanks", "thank you", "thankyou"]

def check_greeting(user_input):
    tokens = preprocess(user_input).split()
    for word in tokens:
        if word in greeting_inputs:
            return random.choice(greeting_responses)
    return None

def check_exit(user_input):
    tokens = preprocess(user_input).split()
    for word in tokens:
        if word in exit_inputs:
            return True
    return False
    
    
def chatbot():
    print("🚆 Advanced Railway Customer Support Chatbot")
    print("Ask about trains, booking, refund, rules, safety, facilities, etc.\n")

    while True:
        user_input = input("You: ").lower()

        # Exit check (bye / thanks / thank you)
        if check_exit(user_input):
            print("Bot: Thank you for using Smart Railway Assistant 🚆")
            print("Bot: Have a safe and pleasant journey!")
            break

        # Greeting check
        greeting = check_greeting(user_input)
        if greeting:
            print("Bot:", greeting)
            continue

        # Train Search
        found = False
        for train_no in train_data:
            if train_no in user_input:
                print(search_train(train_no))
                found = True
                break

        if found:
            continue

        if "fare" in user_input:
            train_no = input("Enter Train Number: ")
            if train_no in train_data:
                print(check_fare(train_no))
            else:
                print("Invalid Train Number.")

        elif "availability" in user_input:
            print(seat_availability())

        elif "pnr" in user_input:
            print(check_pnr())

        elif "book" in user_input:
            print(book_ticket())

        elif "complaint" in user_input:
            issue = input("Describe your issue: ")
            print("Complaint Registered. Reference ID:", random.randint(1000,9999))

        else:
            response = answer_faq(user_input)
            if response:
                print(response)
            else:
                print("Sorry, I could not understand. Please ask railway-related queries.")
                
chatbot()                
                
