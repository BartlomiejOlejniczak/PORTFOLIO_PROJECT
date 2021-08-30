from game import TicTacToe
from tkinter import *
from tkinter.messagebox import _show

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 200


class GameInterface():
    def __init__(self):
        self.window = Tk()
        self.game = TicTacToe()

        self.window.title('TicTacToe Game')
        self.window.config(bg='black', width=200, height=300)

        self.game_label = Label(text='First Player, choose yours symbol:', fg='white', bg='black', height=10,
                                anchor='center', font=30)
        self.game_label.grid(row=0, column=0, columnspan=3)

        self.img_blank = PhotoImage(file='./img/blank.png')
        self.img_xmark = PhotoImage(file='img/xmark.png')
        self.img_circle = PhotoImage(file='img/circle.png')

        self.create_entry_screen()

        self.create_endgame_screen()

        self.window.mainloop()

    def button_clicked(self, button_pressed):
        if not self.game.game_is_on:
            button_pressed.config(state='disabled')
            self.game_label.config(text=f'Player {self.game.turn} Wins')
        else:
            if self.game.turn == 'X':
                button_pressed.config(image=self.img_xmark, state='disabled', padx=0, pady=0)
            else:
                button_pressed.config(image=self.img_circle, state='disabled', padx=0, pady=0)
            self.game.players_choice(self.game.gameboard_btn_list.index(button_pressed))
            if self.game.game_is_on:
                self.game_label.config(text=f'{self.game.turn} Round')
            else:
                if self.game.turn == 'DRAW':
                    self.game_label.config(text=f'{self.game.turn}')
                    # self.window.after(10000, self.window.destroy())
                    # self.window.after(2000, lambda : _show('Title', 'Prompting after 5 seconds'))

                else:
                    self.game_label.config(text=f'Player {self.game.turn} Wins')

    def create_board(self):
        self.game_label.config(text=f'{self.game.turn} Round')
        for rows in range(3):
            for columns in range(3):
                b = Button(image=self.img_blank, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='black')
                b.config(command=lambda m=b: self.button_clicked(m))
                b.grid(column=columns, row=rows + 1)
                self.game.gameboard_btn_list.append(b)

    def choose_your_symbol(self, button_pressed):
        self.choose_symbol = ''
        if button_pressed == self.x:
            self.choose_symbol = 'X'
        else:
            self.choose_symbol = 'O'
        self.player1 = self.choose_symbol
        self.game.set_symbol(self.player1)
        self.create_board()

    def create_entry_screen(self):
        self.x = Button(image=self.img_xmark, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='black')
        self.x.config(command=lambda m=self.x: self.choose_your_symbol(m))
        self.x.grid(column=0, row=2)

        self.o = Button(image=self.img_circle, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='black')
        self.o.config(command=lambda m=self.o: self.choose_your_symbol(m))
        self.o.grid(column=2, row=2)

    def create_endgame_screen(self):
        if not self.game.game_is_on:
            self.game_label.config(text=f'Do You want to play again?')
            self.create_entry_screen()
