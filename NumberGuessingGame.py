#Guess the number 
# Ask user to enter a number 
# If you are closer to number : then print ("Closer to the number")
# If guess number is bigger : then print("Your number is bigger" )
# If you are far from your number : then Print ("Wrong number")
# If you guess the exact number : then print ("You're Right,Congraluations!")


import random
#Range from the user  
min_value = int(input("Enter the minimum value of the range: "))
max_value = int(input("Enter the maximum value of the range: "))

number_to_guess = random.randint(min_value , max_value)

#Ask the user for maximum number of attempts 
max_attempts = int(input("Enter the maximum number of attempts: "))

attempts = 0
#Variable for Best Score 
best_score = None

while attempts < max_attempts:
    guess = int(input(f"Guess the number between {min_value} and {max_value}: "))
    attempts += 1

    
    if guess < number_to_guess:
        print("You're closer to the number, but too low!")
    elif guess > number_to_guess:
        print("Your number is bigger.")
    else:
        print(f"You're right! Congratulations! You guessed the number in {attempts} attempts.")
        if best_score is None or attempts < best_score:
            best_score = attempts
        break

    # Check if the number of attempts are more or less 
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

# Display the user best score 
if best_score is not None:
    print(f"Your best score so far is {best_score} attempts.")