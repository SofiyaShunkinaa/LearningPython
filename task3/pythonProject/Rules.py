def get_win_index(moves, user_move, pc_move):
    lose_moves, win_moves = [], []
    moves_count = len(moves)
    half = moves_count // 2
    player_move_index = -1

    for i in range(moves_count):
        if moves[i] == user_move:
            player_move_index = i

    remaining = moves_count - player_move_index - 1 if moves_count - player_move_index - 1 < half else half

    if remaining > 0:
        for i in range(player_move_index + 1, player_move_index + 1 + remaining):
            lose_moves.append(moves[i])
        remaining2 = half - remaining
        for i in range(0, remaining2):
            lose_moves.append(moves[i])
    else:
        for i in range(half):
            lose_moves.append(moves[i])
    win_moves = [item for item in moves if item not in lose_moves and item != user_move]
    if user_move == pc_move:
        return 0
    elif pc_move in win_moves:
        return 1
    else:
        return -1


def print_rules():
    print("""
*** Rules of the game ***
1) You and the computer have moves listed in the table: your win/lose/draw is determined based on the move you choose relative to the computer's move.
2) The computer makes a move and informs you of the HMAC.
3) You make a move by selecting the corresponding digit from the provided list of options.
4) After determining the winner, you can check the computer's game for "fairness" by HMAC key and computer's move 
""")
