# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
global message, in_play
meassage = ""
in_play = False # Indicator for the status of the game, e.g., on-going or finished
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class

class Hand:
    def __init__(self):
        self.hand  = []

    def __str__(self):
        ans = ""
        for item in self.hand:
             ans += str(item) + " "
        return ans
        #return a string representation of a hand

    def add_card(self, card):
        return self.hand.append(card)

    def get_value(self):
        value = 0
        for card in self.hand:
            rank = card.get_rank()
            value += VALUES[rank]
            if rank == "A" and value <= 11:
                value += 10
        return value
    
    def draw(self, canvas, position):
        pos = position
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [60+36,128+45], CARD_BACK_SIZE)
        for card in self.hand:
            card.draw(canvas, position)
            pos[0] += 80 # distance betweent the cards
               
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
        self.shuffle() # shuffle is part of the Deck intitialization

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        out = self.deck.pop(0)
        return out
        
    def __str__(self):
        ans = ""
        for item in self.deck:
              ans += " " + str(item)
        return "Deck contains" + " " + ans 

#define event handlers for buttons
def deal():
    global outcome, message, in_play, player, dealer, deck_in_play, counter, score
    counter = 0
    if in_play == False:
        #print "--------------------------"
        #print "A new game starts!"
        deck_in_play = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck_in_play.deal_card())
        dealer.add_card(deck_in_play.deal_card())
        player.add_card(deck_in_play.deal_card())
        dealer.add_card(deck_in_play.deal_card())
        #print "Player value " + str(player.get_value())
        #print "Dealer value " + str(dealer.get_value()) 
        message = "Hit or Stand?"
        outcome = "Player value: " + str(player.get_value()) + "  Dealer value: "
        #print outcome
        #print message
        in_play = True
    else: 
        deck_in_play = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck_in_play.deal_card())
        dealer.add_card(deck_in_play.deal_card())
        player.add_card(deck_in_play.deal_card())
        dealer.add_card(deck_in_play.deal_card())
        message = "You have lost this round! New Deal?"
        outcome = "Player value: " + str(player.get_value()) + "  Dealer value: "
        #print message
        score -= 1
        in_play = False

def hit():
    # if the hand is in play, hit the player
    global in_play, player, dealer, score, message, outcome
    if in_play == True:
        player.add_card(deck_in_play.deal_card())
        #dealer.add_card(deck_in_play.deal_card())
        outcome = "Player value: " + str(player.get_value())+ "  Dealer value: "
        #print outcome
        if player.get_value()> 21: 
            message = "You have busted! Dealer wins! New Deal?"           
            outcome = "Player value: " + str(player.get_value()) + "  Dealer value: " + str(dealer.get_value())
            #print message
            score -= 1
            in_play = False
        else: 
            message = "Hit or Stand?"
            #print message
            #print outcome
    else: 
        message = "This round has finished! New Deal?"
        #print message
        
def stand():
    global counter, outcome, message, score, dealer, player, in_play
    if in_play == False:
        message = "This round has finished! New Deal?"
        #print message
    else:
        while dealer.get_value() <=17:
            dealer.add_card(deck_in_play.deal_card())
            counter += 1
            #print "Dealer hits " + str(counter)+ " " + str(dealer.get_value())     
        if dealer.get_value() > 21:
                outcome = "Player value: " + str(player.get_value()) + "  Dealer value: " + str(dealer.get_value())
                message = "Dealer has busted! Player wins! New Deal?"
                #print outcome
                #print message
                in_play = False
                score += 1
        elif dealer.get_value() >= player.get_value(): # dealer winds tie
            outcome = "Player value: " + str(player.get_value()) + "  Dealer value: " + str(dealer.get_value())            
            message = "Dealer wins! New Deal?"
            #print outcome
            #print message
            in_play = False
            score -= 1
        else:
            outcome = "Player value: " + str(player.get_value()) + "  Dealer value: " + str(dealer.get_value())
            message = "Player wins! New Deal?"
            #print outcome
            #print message
            in_play = False
            score += 1

# draw handler    
def draw(canvas):
    global player, dealer, message
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [230,50], 42, "White")
    canvas.draw_text("Dealer :", [60,100], 20, "White")
    canvas.draw_text("Player :", [60,300], 20, "White")
    canvas.draw_text("Score : " + str(score), [480, 555], 20, "White")
    dealer.draw(canvas, [60,125])
    player.draw(canvas, [60,325])
    canvas.draw_text(message, [60,520], 20, "White")
    canvas.draw_text(outcome, [60,555], 20, "White")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
