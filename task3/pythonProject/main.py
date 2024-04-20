import sys
from Controller import Controller


def game_cycle(moves):
    controller = Controller(moves)
    controller.pc_user_moves()
    print(f'HMAC: {controller.get_hmac()}')
    turn = Controller.get_input(moves)
    controller.select_choice(turn)
    return turn


running = 1
while running != "0":
    running = game_cycle(sys.argv[1:])
