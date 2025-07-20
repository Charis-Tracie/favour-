# Simple Chatbot: Greeting, Age Checker, and Dog Years Converter

print("👋 Hello! I'm Tracy!")

# Get the user's name
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

# Get the user's age
age = input("How old are you? ")

# Check if input is a number
if age.isdigit():
    age = int(age)

    # Respond based on age
    if age < 13:
        print("You're a kid! Hope you're enjoying school.")
    elif age < 20:
        print("Teenage years – exciting times!")
    elif age < 65:
        print("Adulting is hard, huh?")
    else:
        print("Retirement must feel great!")

    # Calculate age in dog years
    dog_years = age * 7
    print(f"Did you know? In dog years, you're {dog_years} years old!")

else:
    print("Hmm, that doesn't seem like a number. Try running the program again and enter a number for age.")

# Final goodbye
print(f"It was nice chatting with you, {name}! Have a great day! 😊")
