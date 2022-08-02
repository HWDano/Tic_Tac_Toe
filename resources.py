logo = """
████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████ 
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██ ██             ██    ███████ ██             ██    ██    ██ █████   
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████ 
"""
info = """
This game was made for two players.
Then you will need another person to be able to play it.
This game is based on 9 spaces, created by 3 rows and 3 columns to obtain a quadrangular space, 
divided by 2 horizontal and 2 vertical lines.
It is a turn-based game, where the first player to generate a line of 3 symbols of the same type, 
distributed in the spaces of the grid, wins. Being a circle, the symbol of the first player, 
and an X that of the second player.
At the beginning of the first game, a player is chosen at random to start and if more games are played, 
the first to put his symbol will be the one who lost the previous game.
Once a player places his symbol on one of the grids, that symbol cannot be removed until the game is over.
In case the blank grids are finished and no player has created a line of 3 of his symbols, a tie will be declared.
The score of the total games won, by player, can be seen at the top.
"""
menu = """¡Welcome to this Tic Tac Toe Game!
What do you want?
1) Play
2) Info
3) Score history
4) Exit
Select the option, entering its number: """
a_symbol = [
    " ██████ ",
    "██    ██",
    "████████",
    "██    ██",
    "██    ██"
]
b_symbol = [
    "██████  ",
    "██   ██ ",
    "██████  ",
    "██   ██ ",
    "██████  "
]
c_symbol = [
    " ██████ ",
    "██      ",
    "██      ",
    "██      ",
    " ██████ "
]
symbol_1 = [
    "   ██   ",
    "  ███   ",
    "   ██   ",
    "   ██   ",
    "   ██   "
]
symbol_2 = [
    "██████  ",
    "     ██ ",
    " █████  ",
    "██      ",
    "███████ "
]
symbol_3 = [
    "██████  ",
    "     ██ ",
    " █████  ",
    "     ██ ",
    "██████  "
]
symbol_4 = [
    "██   ██ ",
    "██   ██ ",
    "███████ ",
    "     ██ ",
    "     ██ "
]
symbol_5 = [
    "███████ ",
    "██      ",
    "███████ ",
    "     ██ ",
    "███████ "
]
symbol_6 = [
    " ██████ ",
    "██      ",
    "███████ ",
    "██    ██",
    " ██████ "
]
symbol_7 = [
    "███████ ",
    "     ██ ",
    "    ██  ",
    "   ██   ",
    "   ██   "
]
symbol_8 = [
    " █████  ",
    "██   ██ ",
    " █████  ",
    "██   ██ ",
    " █████  "
]
symbol_9 = [
    " █████  ",
    "██   ██ ",
    " ██████ ",
    "     ██ ",
    " █████  "
]
symbol_0 = [
    " ██████ ",
    "██  ████",
    "██ ██ ██",
    "████  ██",
    " ██████ "
]
x_symbol = [
    "██    ██",
    " ██  ██ ",
    "  ████  ",
    " ██  ██ ",
    "██    ██"
]
o_symbol = [
    " ██████ ",
    "██    ██",
    "██    ██",
    "██    ██",
    " ██████ "
]

blank_space = [
    "        ",
    "        ",
    "        ",
    "        ",
    "        "
]

space = " ██ "
no_space = "      "

line = """                          ██            ██
              ██████████████████████████████████████████
                          ██            ██"""
no_line = """

"""
