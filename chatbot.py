import random
from datetime import datetime


def chatbot_response(message):
    message = message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii"]:
        return random.choice([
            "Hello! How can I help you?",
            "Hey there! Nice to meet you!",
            "Hi! What would you like to talk about?"
        ])

    # Introduction
    elif "your name" in message:
        return "My name is  Samarth's PyBot. I'm your Python chatbot!"

    elif "who created you" in message:
        return "I was created by Samarth !"

    # Feelings
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. How are you?"

    elif "i am fine" in message or "i'm fine" in message:
        return "That's great! What are you doing today?"

    elif "thank" in message:
        return "You're welcome! Happy to help."

    # Python questions
    elif "what is python" in message:
        return (
            "Python is a popular programming language used "
            "for websites, automation, data science, and AI."
        )

    elif "what is a variable" in message:
        return (
            "A variable stores a value. For example, "
            "name = 'Alex' stores the text Alex in name."
        )

    elif "what is a loop" in message:
        return (
            "A loop repeats a block of code. Python has "
            "for loops and while loops."
        )

    elif "what is a function" in message:
        return (
            "A function is reusable code defined using "
            "the def keyword."
        )
    # Questions about Samarth and Kannuuu
    elif "who does samarth love" in message:
        return "Samarth loves his kannuuu "

    elif "who is samarth favourite girl" in message or "who is samarth's favourite girl" in message:
        return "Of course, it's kannuuuu! "

    elif "what does kannu mean to samarth" in message or "what does kannuuu mean to samarth" in message:
        return "Kannuuu is very precious and special to Samarth. "

    elif "who is always in samarth's heart" in message:
        return "Kannuuu has a very special place in Samarth's heart!" 

    elif "who is samarth's special person" in message or "who is samarth special person" in message:
        return "It's Kannuuu, of course! The one who makes Samarth smile! "        
    # Date and time
    elif "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in message or "today" in message:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    # Jokes
    elif "joke" in message:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It had a virus!",
            "Why was the Python programmer calm? They knew how to handle exceptions!"
        ])

    # Favourite colour
    elif "favourite colour" in message or "favorite color" in message:
        return "I like red! What is your favourite colour?"


    # Simple maths
    elif message.startswith("add "):
        try:
            numbers = message.split()
            a = float(numbers[1])
            b = float(numbers[2])
            return f"The answer is {a + b}."
        except (ValueError, IndexError):
            return "Please type something like: add 5 3"

    elif message.startswith("multiply "):
        try:
            numbers = message.split()
            a = float(numbers[1])
            b = float(numbers[2])
            return f"The answer is {a * b}."
        except (ValueError, IndexError):
            return "Please type something like: multiply 5 3"

    # Help
    elif message in ["help", "what can you do"]:
        return (
            "I can greet you, tell jokes, explain Python basics, "
            "show the date and time, and perform addition "
            "and multiplication.\n"
            "Try: joke, what is Python, add 5 3, or multiply 4 6."
        )

    # Exit
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Thanks for chatting with PyBot!"

    # Default response
    else:
        return (
            "I'm not sure how to answer that yet. "
            "Type 'help' to see what I can do."
        )


def main():
    print("=" * 40)
    print("🤖 Welcome to Samarth's PyBot!")
    print("Your friendly Python chatbot")
    print("Type 'help' to see my features.")
    print("Type 'bye' to end the conversation.")
    print("=" * 40)

    while True:
        user_message = input("\nYou: ")
        response = chatbot_response(user_message)

        print("PyBot:", response)

        if user_message.lower().strip() in [
            "bye", "goodbye", "exit", "quit"
        ]:
            break


if __name__ == "__main__":
    main()