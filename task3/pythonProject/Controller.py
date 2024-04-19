from Errors import Errors
from Menu import Menu
from Table import Table
from PC_player import PC_player


class Controller:
    def __init__(self, moves):
        self.moves = moves

    def is_identical(lst):
        for i in range(len(lst)):
            if lst.count(lst[i]) > 1:
                return False
        return True

    def get_input(params):
        def prompt_user():
            return input("Введите параметры через пробел: ").split()

        if len(params) % 2 == 0 or len(params) < 3 or not Controller.is_identical(params):
            if len(params) % 2 == 0:
                Errors.err1()
            elif len(params) < 3:
                Errors.err3()
            else:
                Errors.err2()
            new_params = prompt_user()
            return Controller.get_input(new_params)
        else:
            menu = Menu(params)
            menu.print_menu()
            choice = input('Enter your choice: ')
            return choice

    def select_choice(self, user_choice):
        print(f"Your move: {user_choice}")
        print(len(self.moves))
        if user_choice in range(1, len(self.moves)+1):
            pass
        elif user_choice == len(self.moves)+1:
            table = Table(self.moves)
            table.generate_table()
        else:
            print("Game over")

    def pc_user_init(self):
        pc = PC_player(self.moves)
        key = pc.get_key()
        hmac = pc.get_hmac('q')
        print(hmac)

