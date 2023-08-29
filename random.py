import random

def guess_number():
    # Randomly select a number between 1 and 100
    number = random.randint(1, 100)
    
    guess = 0
    attempts = 0
    
    print("I've chosen a great number between 1 and 100. Try to guess it!")
    
    while guess != number:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            
            # Check if the guess is correct
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")

# Run the game
guess_number()
