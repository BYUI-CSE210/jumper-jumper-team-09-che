#Pablo 
from numpy import empty
import random

class Puzzle:
    def __init__(self):
        # atribute1, will create a list that will contain between 5 and 10 random words
        self.words = ["hello", "uruguay", "ecuador", 
                "argentina", "chocolate", "milk" ]

        #atribute2 empty string that will be updated by random 
        self.secret_word  = ""
    def choose_word(self):
        self.secret_word = random.choice(self.words)
        return self.secret_word

    
        


      