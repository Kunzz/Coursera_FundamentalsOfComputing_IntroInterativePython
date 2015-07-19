# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, cards, exposed, ind, turns
    global card_edge, clicked
    state = 0
    turns = 0
    clicked = list()

# Two card decks    
    card_deck_1 = range (1,9)
    card_deck_2 = range (1,9)
    cards = card_deck_1 + card_deck_2
    random.shuffle(cards)
    
# All cards are closed when game starts
    exposed = [False] * 16
    
# hardcoded horizontal (left and right) edges for each card
    card_edge= range(0, 850, 50)
       
# define event handlers
def mouseclick(pos):
    global state, turns
    
    # add game state logic here
    for ind in range(0,16):
        if pos[0] >= card_edge[ind] and pos[0] < card_edge[ind+1]:
            if state == 0:
                exposed [ind] = True
                clicked.append(ind) 
                state = 1
            elif exposed[ind] == False and state == 1:
                exposed [ind] = True
                clicked.append(ind) 
                state = 2
                turns +=1 # "turns" is incremented when the second card is flipped
            elif exposed[ind] == False and state == 2:
                exposed [ind] = True
                if cards[clicked[-1]] != cards[clicked[-2]]:
                    exposed [clicked[-1]] = False
                    exposed [clicked[-2]] = False
                    clicked.pop()
                    clicked.pop()
                state = 1
                clicked.append(ind)   
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = "+str(turns))
    counter = 0 
    while counter < 16:
        for num in cards:
            if exposed [counter] == True:
                canvas.draw_text(str(num), (25+50*counter, 60), 35, 'White')
                counter += 1 
            else:
                canvas.draw_polygon([[50*counter, 100], [50*(counter+1), 100], [50*(counter+1), 0], [50*counter, 0]], 3, 'White', 'Green')
                counter += 1 
        pass

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
