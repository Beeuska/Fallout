# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 18:30:03 2017

@author: MacKenzie Harnett
"""
#Caravan Simulator part 1

import random 

#Global Variables
cards = ['King', 'Queen', 'Joker', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_values = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}

#Classes
class Deck:
    def __init__(self, deck = []):
        self.deck = deck
        self.deck_copy = deck
        
    def generate_deck(self):
        global cards
        for i in range(1, 30):
            self.deck.append(cards[random.randint(0 , 12)])
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deck_empty():
        pass
        
#Subclass
class Play(Deck):
    def __init__(self, board = {'1': [], '2':[], '3':[], '4':[]}, scores = {'1': 0, '2':0, '3':0, '4':0}):
        self.board = board
        self.scores = scores
        Deck.__init__(self, deck = [])
      
    def fuck_up(self, order, card, card2):
        if order == "UP" and card_values[str(card)]<card_values[str(card2)]:
            raise ValueError("You really cucked up this time.")
        elif order == "DOWN" and card_values[str(card)]>card_values[str(card2)]:
            raise ValueError("Seriously?")
            
    def do_board(self, other, order):

        choice = input("Choose the deck (1-4) you want to add a(n) " + str(self.deck[0]) + " to ")
        if self.deck[0] in card_values:
            if len(other.board[choice])>=2 and other.board[choice][len(other.board[choice])-2] in card_values:
                other.fuck_up(order, self.deck[0], other.board[choice][len(other.board[choice])-2])
            other.board[choice].append(self.deck[0])
            other.scores[choice] += card_values[self.deck[0]]
            
        elif len(self.board[choice]) == 0:
            
            other.board[choice].append(self.deck[0])
            
        else:
            other.board[choice].append(self.deck[0])
            
            if len(other.board[choice]) == 0:
                pass
                
            elif self.deck[0] == 'Queen':
                other.board[choice] = other.board[choice][::-1]
                
            elif self.deck[0] == 'King':
                if other.board[choice][len(other.board[choice])-2] in card_values:
                    other.scores[choice] += card_values[other.board[choice][len(other.board[choice])-2]]
                    
            elif self.deck[0] == 'Joker':
                if other.board[choice][len(choice)-1] in card_values:
                    value = other.board[choice][len(choice)-1]
                    for i in range(other.board[choice].count(value)-1):
                        other.board[choice].remove(value)
                        other.scores[choice] -= card_values[value]
        self.deck = self.deck[1:]
    def play_hand(self, other):
        ''' Essentially, this plays the game. 
        '''
        print(self.board)   
        order = None
        order = input("Do you want ascending (UP) cards or descending (DOWN) cards? ")
        board_choice = input("Choose your board (A) or your opponent's (B) that you want to add a(n) " + str(self.deck[0]) + " to ")
        
        if(board_choice == 'B'):
            self.do_board(self, order)
            self.deck = self.deck[1:]
        elif(board_choice == 'A'):
            self.do_board(other, order)
            other.deck = other.deck[1:]
        
    def is_won(self):
        ''' returns a boolean value on whether or not the user has reached the requirements
        for winning the game
        '''
        total = 0
        for key in self.scores:
            if self.scores[key]<=26 and self.scores[key]>=21:
                total +=1
        if total == 4:
            return True
        return False

class Play_Game(Play):
    def __init__(self, loss = False, win = False):
        self.loss = loss
        self.win = win
        Play.__init__(self, board = {'1': [], '2':[], '3':[], '4':[]}, scores = {'1': 0, '2':0, '3':0, '4':0})
        
    def play_deck(self, other):
        '''how to determine whether or not to place a card on your opponent's deck or your own.
        NOTE: I think I need another subclass just for this?
        '''
        print("YOUR DECK")
        print("--------------------------------------------")
        print(self.board)
        print(self.scores)
        
        print()
        
        print("YOUR OPPONENT:")
        print("--------------------------------------------")
        print(other.board)
        print(other.scores)
        
        
        choice = input("Pick your oponents (A) deck or your own (B) \n")
        if choice == 'A':
            print("You draw a " + str(other.deck[0]) + ".\n")
            other.play_hand(self)
            
            if(other.is_won() == True):
                self.loss = True
                print("/n you fucking lost, bucko")
            
        else:
            print("You draw a " + str(self.deck[0]) + ".\n")
            self.play_hand(other)
            if(self.is_won() == True):
                self.win = True
                print("/n you fucking won, retard")
                
#Debugging shit       
user = Play_Game()
fucker = Play_Game()
user.generate_deck() #Debug
fucker.generate_deck() 
user.shuffle_deck()
fucker.shuffle_deck

while(user.loss == False and user.win == False):
    user.play_deck(fucker)
    