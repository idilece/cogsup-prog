"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""



from random import randint

#check if string 's' represents an integer

def check_int(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

#Ask the user for a number
while True:
    number = input("Enter a number between 1-100: ")
    if check_int(number): #check if the number is an integer according to previously written check_int function
        number = int(number)
        if 1 <= number <= 100: #chack the number for if it is between 1-100.
            break
        else:
            print("The number should be between 1-100!") #output if the input number is not between 1-100.
        print("Please enter a valid integer!") #output if the input number is not an integer
    
    
# Computer guesses until it matches
guess = randint(1, 100)
step_size = 50


#computer continues to "guess" the number by trying random numbers between 1-100 until guess matches with number.
while guess != number:
    step_size = max(1, step_size // 2) #step size will decrease to half at each trial until reaching 1 or finding the number
    if guess < number:
        guess = guess + step_size #if guess > number, new guess will be step size + current guess
    else:
        guess = guess - step_size #if guess < number, new guess will be step size - current guess
    #print("Step size:",step_size)
    #print("Guess:", guess)
        
#print the number

print(f"Computer guessed the correct number, the number was" , number,".")

