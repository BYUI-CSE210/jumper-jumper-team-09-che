from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.parachute import Parachute
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
        terminal_service : For getting and displaying information on the terminal.
        puzzle : For getting the random word 
        parachute : updating the parachute
        user_letter : letter entered by the user
        list_letter : list to store the letters from the user
    """

    def __init__(self):
        """Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self.puzzle = Puzzle()
        self._secret_word = self.puzzle.choose_word()
        self._parachute = Parachute()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.user_letter = ""
        self._list_letters = []
    
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """

        self.begin_text()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def begin_text(self):
        """Displays the welcome messages as well as the parachute, guy, word hyphens
        Args:
            self(Director): an instance of Director"""

        self._terminal_service.write_text("Welcome to this Jumper Jumper Game! ")
        self._terminal_service.write_text(" ")

        #Print the lines "-----"
        self._terminal_service.write_text("_" * len(self._secret_word))
        self._terminal_service.write_text(" ")

        #print the parachute
        self._terminal_service.write_text(self._parachute.print_parachute())
        self._terminal_service.write_text(self._parachute.print_guy())
        self._terminal_service.write_text(" ")

    def _get_inputs(self):
        """gets the inputs from the user using the terminal service 
        object

        Args:
            self (Director): An instance of Director.
        """
        #Get the user input
        self.user_letter = self._terminal_service.read_text("Please type a letter to play: ")
        self._terminal_service.write_text(" ")

    #Valentina
    def _do_updates(self):
        """Updates the hyphens representing the secret word. If the user
        input is incorrect it will substract one line from the parachute

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
            if self.user_letter.lower() in self._secret_word:
                self._terminal_service.write_text("Congrats! ")
                self._terminal_service.write_text(" ")
            
            else:
                self._parachute.cut_parachute()
                if not self._parachute.print_parachute() == " ":
                    self._terminal_service.write_text("Wrong letter... Try again")
                    self._terminal_service.write_text(" ")
                else:
                    self._terminal_service.write_text("Sorry...")
                    self._terminal_service.write_text(" ")
        
        while self._is_playing:
            self._actual_status = ""
            self._missing_letter = 0
            
            for letter in self._secret_word:
                #Update the actual status
                if letter in self._list_letters:
                    self._actual_status = self._actual_status + letter
                else:
                    self._actual_status = self._actual_status + "_"
                    self._missing_letter = self._missing_letter + 1
            
            self._terminal_service.write_text(self._actual_status)
            self._terminal_service.write_text(" ")
            break
    
    #Valentina 
    def _do_outputs(self):
        """displays the parachute, guy and updated hyphens representing
        the secret word

        Args:
            self (Director): An instance of Director.
        """
        
        #print the parachute
        self._terminal_service.write_text(self._parachute.print_parachute())
        self._terminal_service.write_text(self._parachute.print_guy())
        self._terminal_service.write_text(" ")

        if self._missing_letter == 0:
            #winning message
            self._terminal_service.write_text("Congrats!! You win! ")
            self._terminal_service.write_text(f"The secret word is: {self._secret_word}")

            #loop to enhance 
            while self._is_playing:
                
                play_again = self._terminal_service.read_text("Do you want to play again? (Y/N): ")
                
                if play_again.lower() in ("yes", "y"):
                    
                    #restart the attributes before calling the start game again
                    self._terminal_service.write_text(" ")           
                    self.reset()  
                    break
                
                elif play_again.lower() in ("no", "n"):
                    #thanks message
                    self._terminal_service.write_text("Thanks for playing!")
                    self._is_playing = False
                    break
                    
                else:
                    #ensure user input
                    self._terminal_service.write_text("This is not an option... Please, try again")
                    self._terminal_service.write_text(" ")
        
        #if there is no lines drawn / end the game
        if self._parachute.print_parachute() == " ":

            self._is_playing = False
            self._terminal_service.write_text("GAME OVER")
            #show what the secret word was
            self._terminal_service.write_text(f"The secret word was: {self._secret_word}")
            self._terminal_service.write_text(" ")
    
    def reset(self):
        """resets all attributes
        Args:
            self (Director): An instance of the director"""

        self.puzzle = Puzzle()
        self._secret_word = self.puzzle.choose_word()
        self._parachute.reset()
        self._is_playing = True
        self._list_letters = []
        self._missing_letter = 0
        self.begin_text()