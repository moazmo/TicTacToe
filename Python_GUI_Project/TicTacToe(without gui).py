
import os
import time


class Player:
    
    
    
    def __init__(self):
        self.name = ""
        self.symbol = ""
        

    
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please enter letters only.")
    
    def choose_symbol(self):
        while True:
            symbol = input("Choose your symbol (X or O): ").upper()
            if (symbol == "X" or symbol == "O"):
                self.symbol = symbol
                break

            print("Invalid symbol. Please choose X or O.")

class Board:
    def __init__(self):
        self.board = [str(i+1) for i in range(9)]
    
    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-"*10)
        
        
    def update_board(self, position, symbol):
        if self.is_valid_move(position):
            self.board[position-1] = symbol
            return True
        return False
    
    def is_valid_move(self, position):
        if self.board[position-1] in ["X", "O"]:
            return False
        return True
    
    def reset_board(self):
        self.board = [str(i+1) for i in range(9)]

class Menu:
    
    
    def display_main_menu(self):
        print("Welcome to Tic Tac Toe!")
        print("1. Start game")
        print("2. Quit")
        while True:
            choice = input("Enter your choice(1,2): ")
            if self.validate_choice(choice):
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def display_endgame_menu(self):
        print("1. Play again\n2. Quit")
        while True:
            choice = input("Enter your choice(1,2): ")
            if self.validate_choice(choice):
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def validate_choice(self, choice):
        if choice in ["1", "2"]:
            return True
        else:
            return False

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.current_player_index = 0
        self.board = Board()
        self.menu = Menu()
        
    
    
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def start_game_after_reset(self):
        self.setup_players()
        self.play_game()
    
    def play_game(self):
        while True:
            self.play_turn()
            os.system("cls")
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    
    def setup_players(self):
        
        for num, player in enumerate(self.players):
            if num == 0:
                print(f"Player {num+1}:")
                player.choose_name()
                player.choose_symbol()
                print(f"{player.name} will play with {player.symbol}")
                time.sleep(1.5)
            else:
                os.system("cls")
                print(f"Player {num+1}:")
                player.choose_name()
                if self.players[0].symbol == "X":
                    player.symbol = "O"
                else:
                    player.symbol = "X"
                print(f"{player.name} will play with {player.symbol}")
                time.sleep(1.5)
                os.system("cls")
    

    def play_turn(self):
        player = self.players[self.current_player_index]
        print(f"{player.name}'s turn:")
        self.board.display_board()
        while True:
            try:
                position = int(input("Enter position(1-9): "))
                if (1 <= position <= 9) and (self.board.update_board(position, player.symbol)):
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        self.switch_player()
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    
    def check_win(self):
        win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6] # diagonals
    ]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                self.board.display_board()
                print(f"{self.players[1-self.current_player_index].name} wins!")
                return True
        return False
    
    def check_draw(self):
        if all(cell in ["X", "O"] for cell in self.board.board):
            print("It's a draw!")
            return True
        return False
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.start_game_after_reset()
    
    def quit_game(self):
        print("Thanks for playing! Goodbye!")
        exit()

Game().start_game()
















