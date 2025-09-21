def chatbot_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm a bot, so I'm always great!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

# Start the chatbot loop
print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' or 'goodbye' to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print(f"Chatbot: {response}")

    # Exit condition
    if "bye" in user_message.lower() or "goodbye" in user_message.lower():
        break