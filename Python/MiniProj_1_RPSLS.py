import random

# Define function "name_to_number" to convert the input
# stringe, player_choice, to the corresponding number for comparison purpose
# The conversion follows the following rules:

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    
    if name == "rock":
       num=0
    
    elif name == "Spock":
       num=1   

    elif name == "paper":
       num=2
        
    elif name == "lizard":
       num=3
      
    elif name == "scissors":
       num=4
       
    else:
      print "Ilegal input"
   
    return num

# Define function "number_to_name" to interpret the randomly 
# created computer number one of the five stringes presented
# above


def number_to_name(num):
    if num == 0:
       name="rock"
    
    elif num==1:
       name = "Spock"

    elif num == 2:
       name = "paper"
       
    elif num == 3:
       name = "lizard"

    else:
       name = "scissors"
   
    return name


# The purpose of function "rpsls" is to 
# simulate the results of a
# Rock-paper-scissors-lizard-Spock game including
# one player and a computer generated opponent. 
# This function takes the player's choice,
# player_choice, as input.

# Note: the input has to be one of the five
# stringes mentioned above, or else an error
# message "Ilegal Input" will be displayed. 

def rpsls(player_choice):
    print ""
    print "Player", "chooses", player_choice
    
    player_number = name_to_number(player_choice) 
    
    comp_number =  random.randrange(0, 5, 1)
    
    print "Computer", "chooses", number_to_name(comp_number)
    
    delta = (player_number - comp_number) % 5
    
    if delta == 0:
        print("Player and computer tie!\n")
    
    elif delta <=2 and delta !=0:
        print("Player wins!\n")
    
    else:
        print("Computer wins!\n")

# For evaluation purpose, 
# the following five scenarios are provided 

rpsls("rock")   
rpsls("Spock")  
rpsls("paper")
rpsls("lizard")  
rpsls("scissors")  