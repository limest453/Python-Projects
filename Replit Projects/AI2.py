import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm fine, thanks for asking."]),
    (r"what's your name?", ["You can call me Chatbot.", "I'm just a chatbot."]),
    (r"quit|exit", ["Bye! Take care.", "Goodbye!"]),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Welcome to the chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() in ['quit', 'exit']:
        break
