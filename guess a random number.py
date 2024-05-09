
import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    secret_number = random.randint(1, 50)
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
            if abs(guess - secret_number) <= 5:
                print("You are close!")
            
        elif guess > secret_number:
            print("Too high! Try again.")
            if abs(guess - secret_number) <= 5:
                print("You are close!")
            
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

guessing_game()

