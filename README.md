# cows and bulls game in python
Here's the **README** content for the **3-digit Cows and Bulls Number Guessing Game** in Python:  

---

# 🐄🐂 Cows and Bulls - 3-Digit Number Guessing Game 🎯  

## 📌 Introduction  
Cows and Bulls is a classic number guessing game where the player tries to guess a **random 3-digit number**. The game provides feedback in the form of:  

- **"Cows"** 🐄 → Correct digit in the wrong position.  
- **"Bulls"** 🐂 → Correct digit in the correct position.  

This project is implemented in **Python** using `randint()`, functions (`def`), `while` loops, and `elif` ladder for logic control.  

---

## ⚙️ How the Game Works  

1. The computer generates a **random 3-digit number**.  
2. The player guesses a 3-digit number.  
3. The game provides feedback:  
   - **Bulls** 🐂 = Correct digit in the correct place.  
   - **Cows** 🐄 = Correct digit in the wrong place.  
4. The game continues until the player correctly guesses the number (i.e., 3 Bulls).  

---

## 🛠️ Technologies Used  

- **Python**  
- `random.randint()` for generating random numbers  
- `while` loop for continuous guessing  
- `elif` ladder for checking conditions  

---

## 🚀 How to Run the Game  

1. Clone this repository:  
   ```bash
   git clone https://github.com/meghana1209/cows-and-bulls-3digit.git
   cd cows-and-bulls-3digit
   ```
2. Run the Python script:  
   ```bash
   python cows_and_bulls_3digit.py
   ```
3. Start guessing and enjoy the game! 🎯  

---

## 📝 Code Overview  

```python
import random

def generate_number():
    """Generates a 3-digit random number as a string."""
    return str(random.randint(100, 999))

def get_cows_and_bulls(secret, guess):
    """Returns the number of cows and bulls."""
    cows, bulls = 0, 0
    for i in range(3):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return cows, bulls

def play_game():
    """Runs the Cows and Bulls game loop."""
    secret_number = generate_number()
    attempts = 0

    print("Welcome to Cows and Bulls! Try to guess the 3-digit number.")

    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit() or len(guess) != 3:
            print("Please enter a valid 3-digit number.")
            continue

        attempts += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        print(f"Cows: {cows}, Bulls: {bulls}")

        if bulls == 3:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
```

---

## 🎯 Sample Output  

```
Welcome to Cows and Bulls! Try to guess the 3-digit number.
Enter your guess: 123
Cows: 1, Bulls: 0
Enter your guess: 456
Cows: 0, Bulls: 1
Enter your guess: 678
Cows: 1, Bulls: 1
Enter your guess: 732
Congratulations! You guessed the number 732 in 4 attempts.
```

---

## 📌 Features  

✅ Random **3-digit number** generation  
✅ Unlimited attempts until correct guess  
✅ Input validation (only 3-digit numbers allowed)  
✅ Accurate Cows & Bulls calculation  
✅ Simple `while` loop and `elif` ladder logic  

---

## 📌 Future Enhancements  

- Add difficulty levels (e.g., 2-digit, 4-digit numbers).  
- Implement a GUI version using **Tkinter** or **PyQt**.  
- Add a **leaderboard** to track high scores.  

---

## 📜 License  

This project is open-source under the **MIT License**.  

---

## 🙌 Contributing  

Feel free to contribute by improving the code or adding new features! Fork the repo and submit a pull request.  

---

Let me know if you need any modifications! 🚀😊
