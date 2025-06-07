import random

def func():
    random_number = random.randint(1, 100)
    attempts = 5
    current_attempt = 1

    print('Guess the number between 1 and 100. You have 5 attempts.')

    while current_attempt <= attempts:
        try:
            user_input = input(f'Attempt {current_attempt}: Your number: ')
            user_answer = int(user_input)
        except ValueError:
            print('Please enter a valid integer.')
            continue


        if user_answer == random_number:
            print("Congratulations! You guessed the correct number.")
            return
        elif user_answer < random_number:
            print("Too low.")
        else:
            print("Too high.")

        current_attempt += 1

    print(f"Sorry, you ran out of attempts. The correct number was {random_number}.")

func()
