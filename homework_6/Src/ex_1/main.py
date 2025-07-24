import random

number = random.randint(1, 100)

max_attempts = 5

print("I have picked a number between 1 and 100. " \
"You have 5 attempts to guess it.")

for i in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {i}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Sorry, you've used all your attempts. The correct number was {number}.")

