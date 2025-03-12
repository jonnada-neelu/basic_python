"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
# Random number guess game

import random  
def random_number_guess():
    random_number = random.randint(1, 20)  
    guess_count = 0
    max_attempts = 5  
    print("Can you guess the random number between 1 to 20 ? ")
    while guess_count < max_attempts:
            user_guess = int(input(f"Attempt {guess_count + 1}/{max_attempts}: Enter your guess (1-20): "))
            if user_guess < 1 or user_guess > 20:
                print("Invalid input! Please enter a number between 1 and 20.")
                continue  
            guess_count += 1  
            if user_guess == random_number:
                print("Guessed correct number")
                return  
            elif user_guess < random_number:
                print("Too Low! Try again.")
            else:
                print("Too High! Try again.")
    
    print("Game Over! The correct number was:", random_number)

random_number_guess()
