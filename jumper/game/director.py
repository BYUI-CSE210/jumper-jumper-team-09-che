from game.terminal_service import TerminalService
from game.puzzle import Puzzle
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
        puzzle: For getting the random word 
        parachute: updating the parachute
    """
    def __init__(self):
        """Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self.puzzle = Puzzle()
        self.secret_word = self.puzzle.choose_word()
        #self.parachute = Parachute()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.user_letter = ""
    
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text("Welcome to this Jumper Jumper game! ")
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Update this comment
        Args:
            self (Director): An instance of Director.
        """
        #Get the user input
        self.user_letter = self._terminal_service.read_text("Please type a letter to play: ")
        self._terminal_service.write_text(" ")
#Valentina
    def _do_updates(self):
        """Update this comment
        Args:
            self (Director): An instance of Director.
        """
        #Add the user input to a list and check if that letter is in the list
        if self.user_letter.lower() in self._list_letters:
            self._terminal_service.write_text("You already use this letter")
            self._terminal_service.write_text(" ")
        else:
            self._list_letters.append(self.user_letter)
            # Message if the letter is in the word
            if self.user_letter.lower() in self.secret_word:
                self._terminal_service.write_text("Congrats! ")
                self._terminal_service.write_text(" ")
            else:
                self._terminal_service.write_text("Wrong letter... Try again")
                self._terminal_service.write_text(" ")
        while self._is_playing:
            self._actual_status = ""
            self._missing_letter = 0
            for letter in self.secret_word:
                #Update the actual status
                if letter in self._list_letters:
                    self._actual_status = self._actual_status + letter
                else:
                    self._actual_status = self._actual_status + "_"
                    self._missing_letter = self._missing_letter + 1
            self._terminal_service.write_text(self._actual_status)
            self._terminal_service.write_text(" ")
            break
    def _do_outputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        

        #while self._is_playing:
           # play_again = self._terminal_service.read_text("Do you want to play again?: ")
           # if play_again.lower() == "yes":
                
             #   self._is_playing = True
             #   break
               
            #elif play_again.lower() =="no":
              #  self._is_playing = False
                
           # else:
               # self._terminal_service.write_text("This is not an option... Please, try again")
                #play_again = self._terminal_service.read_text("Do you want to play again?: ")
                #break

            
