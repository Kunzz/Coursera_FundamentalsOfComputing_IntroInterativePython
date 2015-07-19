# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game(xx):
    # initialize global variables used in your code here
    global secret_number
    global num
    global max_guess
    global counter
    global upp_lim    
    counter=0
    low_lim=0
    upp_lim=xx
    #print upp_lim
    secret_number = random.randrange(low_lim, upp_lim, 1)
    # Calculate the maximum number of guess allowed
    max_guess= math.ceil(math.log(upp_lim-low_lim+1,2))
    print " New game. Range is from", low_lim, "to", upp_lim
    return secret_number

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    upp_lim=100
    new_game(upp_lim)
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    # global secret_number   
    upp_lim=1000
    new_game(upp_lim)
    
    pass

def input_guess(guess):
    # main game logic goes here	  
    num= int(guess)
    global counter
    # Register the number of attempts made
    counter += 1
    print " Number of remaining guesses is", int(max_guess-counter)
    print " Guess was", num
    
    # when the guess number is greater than the secret_number
    if (num < secret_number) and (counter < max_guess):
        print " Higer"
        return
    # when the guess number is smaller than the secret_number                           
    elif (num > secret_number) and (counter < max_guess):
        print " Lower"
        return
    # when the guess number equals to the secret_number                           
    elif  (num == secret_number) and (counter <= max_guess):
        print " Correct"
        return
    else:
        print " You ran out of guesses. The number was", secret_number
        new_game(upp_lim) 
        counter=0
    pass                  
   
############################################################    
frame=simplegui.create_frame("Guess The Number", 300, 300)
frame.add_input('Guess', input_guess, 100)
frame.add_button('Range: 1-100', range100,  200)
frame.add_button('Range: 1-1000', range1000, 200)
frame.start()

new_game(100)

###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#print secret_number 

#input_guess("50")
#input_guess("75")
#input_guess("62")
#input_guess("68")
#input_guess("71")
#input_guess("73")
#input_guess("74")

###################################################
# Output from test #1
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range1000()
#secret_number = 375	
#input_guess("500")
#input_guess("250")
#input_guess("375")

###################################################
# Output from test #2
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#secret_number = 28	
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")

###################################################
# Output from test #3
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
