import numpy as np
from tkinter import *

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_Y_color = '#0492CF'
Green_color = '#7BC043'



#---------------------------------------------------------------------------------------
#inicializar as funções
#---------------------------------------------------------------------------------------
class Jogo_do_Galo():
    def __init__(self):
        self.window = Tk('Jogo do Galo')
        self.canvas = Canvas(self.window, width = size_of_board, height = size_of_board)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        
        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))
        
        self.player_X_turns = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False
        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0
        
    def mainloop(self):
        self.window.mainloop()
        
    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0 , (i +1) * size_of_board / 3, size_of_board)
            
        for i in range(2):
            self.canvas.create_line(0, (i+1) * size_of_board / 3, size_of_board, (i + 1)* size_of_board / 3)
            
    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))
        
        


 
