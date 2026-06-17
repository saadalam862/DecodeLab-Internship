# Rule-Based AI Chatbot

Built in Python during DecodeLab Internship.

## How it Works
The chatbot uses a Python **dictionary** where:
- **Key** = user input (e.g. `"hello"`)
- **Value** = bot reply (e.g. `"Hi there!"`)

When user types something, it matches the input against dictionary keys and returns the answer.

## Code Logic
```python
# 1. Store all responses in a dictionary
chatbot_brain = {
    "hello": "Hi there! How can I help you?",
    "what is ai": "AI is the simulation of human intelligence.",
}

# 2. Clean user input
user_input = input("You: ").strip().lower()

# 3. Match and reply
reply = chatbot_brain.get(user_input, "I don't know. Type 'help'.")
print(f"Bot: {reply}")
```

## How to Run
```bash
python AIP1.py
```

## Author
Saad Alam — DecodeLab Internship