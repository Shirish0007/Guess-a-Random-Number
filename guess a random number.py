
# # list=[10,20,30,40]
# # list[0]

# # list[-1]

# # list[1:3]


# # for i in list:
# #  print(i)


# s = range(5,10,2)
# for i in s :
#  print(i) 



# a={1,'s',54,'surname',99,10.5,'a',4+2j}

# a.add (2+5j)
# a.remove (1)

# for i in a :
#  print(i) 

# s={101:'durga',103:'shiva'}
# s[103]='sunny' 
# for i in s:
#      print(s)


# s="durga\nsoftware"
# print(s) 

# s="durga\tsoftware"
# print(s) 


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

