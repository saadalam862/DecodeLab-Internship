
print("*"*43)
print("="*10,"Rule based AI Chatbot","="*10)
print("="*6,"Type 'exit' or 'quit' to stop","="*6)
print("*"*43 +"\n")
chatbot_brain={
    # Greetings
    "hello":                "Hi there! How can I help you?",
    "hi":                   "Hey! Nice to meet you.",
    "good morning":         "Good morning! Hope you have a great day.",
    "good night":           "Good night! Sleep well.",

    # About the bot
    "what is your name":    "I am a Rule-Based AI Chatbot built in Python.",
    "who made you":         "I was built by Saad Alam",
    "are you a robot":      "Yes! I am a simple rule-based bot, not a human.",
    "what can you do":      "I can answer basic questions. Type 'help' for a list.",

    # Basic AI questions
    "what is ai":           "AI is the simulation of human intelligence by machines.",
    "what is python":       "Python is a popular programming language used in AI and data science.",
    "what is machine learning": "Machine learning is a type of AI that learns from data.",
    "what is a chatbot":    "A chatbot is a program that simulates conversation with humans.",

    # Small talk
    "how are you":          "I am just code, but running perfectly! Thanks for asking.",
    "what is your age":     "I was just created, so I am very new!",
    "tell me a joke":       "Why do programmers prefer dark mode? Because light attracts bugs!",
    "thank you":            "You are welcome! Happy to help.",

    # Exit and help
    "bye":                  "Goodbye! It was nice talking to you.",
    "see you":              "See you later! Take care.",
    "ok":                   "Alright! Let me know if you need anything else.",
}

chatbot_brain["help"]="you can ask:\n"+ "\n".join(chatbot_brain.keys())

while True:

# Sanitization: clean input,  Strip: remove extra spaces. Lower: convert to lower case.
    user_input=input("You: ").strip().lower()   
    if user_input in ("exit","quit"):
        print("Bot: Goodbye!")
        break
    reply=chatbot_brain.get(user_input, "I don't know. type 'help for options.'")
    print(f"Bot: {reply}")


