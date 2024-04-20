from Errors import Errors
from Menu import Menu
from Table import Table
from PC_player import PC
from HMAC import Hmac
from Rules import get_win_index, print_rules
from colorama import Fore, Style


class Controller:
    def __init__(self, moves):
        self.moves = moves
        self.pc_key = None
        self.pc_move = None

    def is_identical(lst):
        for i in range(len(lst)):
            if lst.count(lst[i]) > 1:
                return False
        return True

    @staticmethod
    def checking(moves):
        def prompt_user():
            return input("Enter new moves: ").split()

        if len(moves) % 2 == 0 or len(moves) < 3 or not Controller.is_identical(moves):
            if len(moves) % 2 == 0:
                Errors.err1()
            elif len(moves) < 3:
                Errors.err3()
            else:
                Errors.err2()
            new_moves = prompt_user()
            return Controller.checking(new_moves)
        else:
            return moves

    def get_menu(params):
        menu = Menu(params)
        menu.print_menu()
        return Controller.get_menu_input()

    def get_moves(self, moves):
        self.moves = moves

    @staticmethod
    def get_menu_input():
        choice = input('Enter your move: ')
        return choice

    def select_choice(self, user_choice):
        user_move_value = self.get_move_value(user_choice)
        print(f"Your move: {user_move_value}")
        if user_choice == '?':
            print_rules()
            table = Table(self.moves)
            table.generate_table()
        elif user_choice.isdigit() and int(user_choice) in range(1, len(self.moves) + 1):
            self.print_pc_move()
            self.print_win(user_move_value)
            self.print_pc_hmac_key()
        elif user_choice == "0":
            print("Game over")
        else:
            print("Incorrect input! Try again")
            self.select_choice(Controller.get_menu_input())

    def pc_user_moves(self):
        pc = PC(len(self.moves))
        pc.make_choice()
        return pc

    def get_move_value(self, key):
        values = Menu.create_dictionary(self.moves)
        return values.get(key)

    def get_hmac(self):
        pc = self.pc_user_moves()
        self.pc_key = pc.key
        self.pc_move = self.get_move_value(pc.move)
        hmac = Hmac(self.pc_key, self.pc_move)
        return hmac.generate_hmac()

    def print_pc_move(self):
        print(f'Computer move: {self.pc_move}')

    def print_pc_hmac_key(self):
        print(f'HMAC key: {self.pc_key}')
        print("=" * 100)

    def print_win(self, user_move):
        result = get_win_index(self.moves, user_move, self.pc_move)
        if result == 0:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 'Game draw!' + Style.RESET_ALL)
        elif result == 1:
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'You win!' + Style.RESET_ALL)
        elif result == -1:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + 'You lose!' + Style.RESET_ALL)
