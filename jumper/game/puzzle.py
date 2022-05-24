#Pablo 
import random

class Puzzle:
    """A random word selected hidden to the player
    
    The puzzle responsability is to select a random word 
    from a list to be the puzzle of the game match.
    
    Attributes:
        words (list) = a list of words
        secret_word (str) = a random word selected from the word list
    """

    def __init__(self):
        """creates an instance of a secret word"""

        # atribute1, will create a list that will contain between 5 and 10 random words
        self.words = ["hello", "uruguay", "ecuador", 
                "argentina", "chocolate", "milk",
                "keyboard", "mouse", "moon", "sun",
                "stars", "random", "sleep", "late", "night",
                "husband","wife" ]

        #atribute2 empty string that will be updated by random 
        self.secret_word  = ""

    def choose_word(self):
        """chooses a secret word from the list"""

        self.secret_word = random.choice(self.words)
        return self.secret_word

    
        


      