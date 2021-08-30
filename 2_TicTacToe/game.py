class TicTacToe:
    def __init__(self):

        self.turn = ''
        self.player1 = ''
        self.player2 = ''
        self.gameboard_btn_list = []
        self.gameboard_list = [''] * 9

        self.game_is_on = True

    def end_game(self):
        self.game_is_on = False


    def set_symbol(self, player1):
        self.player1 = player1
        self.symbol = ('X', 'O')
        self.turn = self.player1
        if self.player1 == self.symbol[0]:
            self.player2 = self.symbol[1]
        else:
            self.player2 = self.symbol[0]


    def players_choice(self, pc):
        self.gameboard_list[pc] = self.turn
        self.check_if_player_won()


    def check_if_player_won(self):
            if self.turn != "":

                if self.gameboard_list[:3].count(self.turn) == 3 or self.gameboard_list[3:6].count(self.turn) == 3 or self.gameboard_list[6:9].count(self.turn)  == 3:
                    self.end_game()
                if self.gameboard_list[::3].count(self.turn) == 3 or self.gameboard_list[1::3].count(self.turn) == 3 or self.gameboard_list[2::3].count(self.turn)  == 3:
                    self.end_game()
                if self.gameboard_list[::4].count(self.turn)  == 3 or self.gameboard_list[2:-2:2].count(self.turn) == 3:
                    self.end_game()
                for i in self.gameboard_list:
                    if i != '':
                        if self.gameboard_list.count(i) > 4 and self.gameboard_list[:3].count(i) < 3 and self.gameboard_list[6:9].count(i) < 3:
                            print(self.gameboard_list[:3].count(i))
                            self.turn = 'DRAW'
                            self.end_game()
            if self.game_is_on:
                self.change_turn()


    def change_turn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1