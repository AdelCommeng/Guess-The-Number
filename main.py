import random
import art 
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
the_number= random.randint(1,100)
print(the_number)
user_choice=input("Choose a difficulty. Type 'easy' or 'hard'").lower()
if user_choice =="hard":
  attempts =5
  print(f"You have {attempts} remaining to guess the number.")
  finish=False
  while not finish:
    user_guess= int(input("Make a guess: "))

    if user_guess > the_number:
      print("Too high")
      attempts-=1
      print(f"{attempts} left")
    elif user_guess<the_number:
      print("Too low")
      attempts-=1
      print(f"{attempts} left")
      
    else:
      print("You got it!")
      finish=True
    if attempts ==0:
      print("You ran out of guesses. You lose sorry!")
      finish =True

      
elif user_choice =="easy":
  attempts =10
  print(f"You have {attempts} remaining to guess the number.")
  finish=False
  while not finish:
    user_guess= int(input("Make a guess: "))

    if user_guess > the_number:
      print("Too high")
      attempts-=1
      print(f"{attempts} left")
    elif user_guess<the_number:
      print("Too low")
      attempts-=1
      print(f"{attempts} left")
      
    else:
      print("You got it!")
      finish=True
    if attempts ==0:
      print("You ran out of guesses. You lose sorry!")
      finish =True
