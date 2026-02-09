import random

total_score = 0

for level in range (1,4) :
     print (f"\n level {level} :")

     secret_number = random.randint (1,30)

     for attempt in range (5) :
         guess = int(input("guess a number from 1 to 30 :"))

         if guess == secret_number :
             print ("your guess is correct!")
             total_score += 10
             break
         elif guess > secret_number :
              print ("this number is smaller than your guess!")
         elif guess < secret_number :
              print ("this number is bigger than your guess!")
          else :
               print (f"Your chance is over! the correct number is {secret_number}!")


print (f"\n Your total score is {total_score}")
print ("End of the game!")


