# Guess the Number Game

## Overview
The "Guess the Number" game allows the user to guess a randomly selected number within a given range. The user will have a limited number of attempts to guess the number correctly. Based on the guesses, the game provides feedback on whether the guess is too high, too low, or correct. If the user guesses correctly, their score (number of attempts) is recorded, and the best score across multiple rounds is tracked.

## Features
- The user can define the minimum and maximum range for the number.
- The user sets the maximum number of attempts.
- The game provides feedback for each guess:
  - "Closer to the number" for guesses near the target number.
  - "Your number is bigger" if the guess is larger than the target number.
  - "Wrong number" if the guess is not close or incorrect.
  - "You're right! Congratulations!" when the correct number is guessed.
- The user's best score (fewest attempts) is saved and displayed.

## How to Play
1. Enter the minimum and maximum values for the number range.
2. Specify the maximum number of attempts allowed to guess the number.
3. Guess the number! After each guess, the game will tell you if your guess is too high, too low, or correct.
4. If you guess the correct number within the given attempts, you'll be congratulated.
5. If you run out of attempts, the correct number will be revealed.

## Instructions
1. Start the game by running the Python script.
2. You will be asked:
   - The minimum and maximum values for the number range.
   - The maximum number of attempts to guess the number.
3. You can then start guessing the number based on the feedback provided after each attempt.
4. If you guess correctly, the number of attempts it took will be displayed along with your best score (if applicable).
5. If you fail to guess the number within the given attempts, the correct number will be revealed.

## Example
```shell
Enter the minimum value of the range: 1
Enter the maximum value of the range: 100
Enter the maximum number of attempts: 5
Guess the number between 1 and 100: 50
Your number is bigger.
Guess the number between 1 and 100: 25
You're closer to the number, but too low!
Guess the number between 1 and 100: 30
You're right! Congratulations! You guessed the number in 3 attempts.
Your best score so far is 3 attempts.
'''

## Code Explanation
- `random.randint(min_value, max_value)` generates a random number between the user-defined minimum and maximum values.
- The script takes the user's input to set the range and the maximum attempts.
- A `while` loop is used to check if the user has guessed the number correctly or exhausted their attempts.
- After each guess, the program provides feedback to help the user make better guesses.
- If the user guesses the number correctly, their score (the number of attempts) is tracked and displayed as the "best score" if it's the fewest attempts so far.
- If the user does not guess the number in the allotted attempts, the correct number is displayed.

## Requirements
- Python 3.x

## How to Run
1. Download the script file (e.g., `guess_the_number.py`).
2. Open a terminal or command prompt.
3. Navigate to the folder containing the script.
4. Run the script by typing:
   ```bash
   python guess_the_number.py
   ```

## Notes
- You can change the minimum and maximum range values to customize the difficulty of the game.
- The game tracks your best score and displays it after each round.
- If you use up all your attempts, the correct number will be shown, and you can try again.