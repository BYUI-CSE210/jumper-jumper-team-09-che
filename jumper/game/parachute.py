#Renzo
class Parachute: 
    """A backpack that deploys a cloth with many strings to 
    reduce falling speed
    
    The parachute's responsability is to keep track of the strings 
    attached to the game character. Once there is no strings the character 
    dies (game over).
    
    Attributes:
        parachute (list) = list containing the parachute lines
        lines (int) = total lines of the parachute
    """

    def __init__(self): 
        """Creates an instance of a parachute"""
    
        self._parachute = ["___", "/___\\", "\\   /", "\\ /"]
        self._lines = len(self._parachute)

    def cut_parachute(self):
        """update the parachute"""

        self._lines -= 1

    def print_parachute(self):
        """returns the parachute state to print it using 
        terminal services"""

        if self._lines == 4:
            return f"  {self._parachute[0]}\n {self._parachute[1]}\n {self._parachute[2]}\n  {self._parachute[3]}"

        elif self._lines == 3:
            return f"   \n {self._parachute[1]}\n {self._parachute[2]}\n  {self._parachute[3]}"
        
        elif self._lines == 2:
            return f"   \n  \n {self._parachute[2]}\n  {self._parachute[3]}"
        
        elif self._lines == 1:
            return f"   \n  \n  \n  {self._parachute[3]}"
        
        elif self._lines == 0:
            return " "

    def print_guy(self):
        """returns the guy | if _lines is greater than zero
        print a guy, otherwise print it dead"""

        if self._lines > 0: 
            return f"   o\n  /|\\ \n  / \\"

        else:
            return f"   x\n  /|\\ \n  / \\"


# parachute = Parachute()

# print(parachute.print_parachute())
# print(parachute.print_guy())    

# parachute.cut_parachute()
# print(parachute.print_parachute())
# print(parachute.print_guy()) 

# parachute.cut_parachute()
# print(parachute.print_parachute())
# print(parachute.print_guy()) 

# parachute.cut_parachute()
# print(parachute.print_parachute())
# print(parachute.print_guy()) 

# parachute.cut_parachute()
# print(parachute.print_parachute())
# print(parachute.print_guy()) 