import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kółko i krzyżyk")

        self.player = ""
        self.bot = ""

        self.buttons = []
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

        self.player_selection_frame = tk.Frame(self.root)
        self.player_selection_frame.pack()

        self.x_button = tk.Button(self.player_selection_frame, text="X", command=lambda: self.start_game("X"))
        self.x_button.pack(side=tk.LEFT)

        self.o_button = tk.Button(self.player_selection_frame, text="O", command=lambda: self.start_game("O"))
        self.o_button.pack(side=tk.LEFT)

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.game_frame, text="", width=10, height=4, command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.root.mainloop()

    def start_game(self, player):
        self.player = player
        self.bot = "O" if player == "X" else "X"
        self.reset_board()

        if self.bot == "X":
            self.make_bot_move()

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].configure(text="")

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.player
            self.buttons[row][col].configure(text=self.player)

            if self.check_winner(self.player):
                messagebox.showinfo("Koniec gry", f"Wygrał gracz {self.player}!")
                self.reset_board()
                return

            if self.check_draw():
                messagebox.showinfo("Koniec gry", "Remis!")
                self.reset_board()
                return

            self.make_bot_move()

    def make_bot_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.bot
            self.buttons[row][col].configure(text=self.bot)

            if self.check_winner(self.bot):
                messagebox.showinfo("Koniec gry", f"Wygrał gracz {self.bot}!")
                self.reset_board()
                return

            if self.check_draw():
                messagebox.showinfo("Koniec gry", "Remis!")
                self.reset_board()
                return

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True

            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

game = TicTacToe()
