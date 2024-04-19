import sys
from Controller import Controller


controller = Controller(sys.argv[1:])
turn = 1
controller.pc_user_init()
while turn:
    turn = int(Controller.get_input(sys.argv[1:]))
    controller.select_choice(turn)
