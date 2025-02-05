from random import randint  # Importing randint from the random module

# Function to generate a unique 3-digit number
def generate_random_number():
    while True:
        num = str(randint(100, 999))  # Generate a random 3-digit number
        if num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:  # Ensure all digits are unique
            return num

# Game Setup
name = input("Welcome to the Cows and Bulls game! \nPlease enter your name to start the game: ")       
print(f"Hello {name}, let's start the game!!")

chances = 8
cows = 0
bulls = 0
secret_number = generate_random_number()  # Generate the random number

while chances > 0:
    print(f"You have {chances} chances left.")
    guess = input("Enter your 3-digit guess: ")

    # Input validation
    if not (guess.isdigit() and len(guess) == 3):
        print("Invalid input! Please enter a 3-digit number.")
        continue

    # Check if the guess is correct
    if guess == secret_number:
        print("🎉 Great! You won the game!!!!!! 🎉")
        break
    else:
        bulls = 0
        cows = 0

        # Checking for Bulls and Cows
        for i in range(3):
            if guess[i] == secret_number[i]:  
                bulls += 1  # Correct digit in the correct place
            elif guess[i] in secret_number:
                cows += 1  # Correct digit in the wrong place

        print(f"Keep going! You have {bulls} Bulls and {cows} Cows.")

    chances -= 1  # Decrease chances

# If the user fails to guess the number
if chances == 0:
    print(f"Game Over! The correct number was {secret_number}. Better luck next time! 🎯")
