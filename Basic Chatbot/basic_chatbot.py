def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I am a simple Python chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

print("Welcome to Basic Chatbot!")
print("Type 'hello', 'how are you', 'what is your name', or 'bye' to chat.\n")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower() == "bye":
        break