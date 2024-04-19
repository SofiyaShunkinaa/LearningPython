class Menu:
    def __init__(self, moves):
        self.moves = self.create_dictionary(moves)

    @staticmethod
    def create_dictionary(moves):
        dictionary = {}
        for i, item in enumerate(moves, 1):
            dictionary[i] = item
        dictionary[len(moves) + 1] = 'help'
        dictionary[0] = 'exit'
        return dictionary

    def print_menu(self):
        print("Welcome to the menu, choose one of the following:")
        menu = ''
        for key, value in self.moves.items():
            print(f"{key} - {value}")
        print(menu)