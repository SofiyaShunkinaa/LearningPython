def get_win_index(moves, user_move, pc_move):
    lose_moves, win_moves = [], []
    moves_count = len(moves)
    half = moves_count // 2
    player_move_index = -1

    for i in range(moves_count):
        if moves[i] == user_move:
            player_move_index = i

    remaining = moves_count - player_move_index - 1 if moves_count - player_move_index - 1 < 3 else half

    if remaining > 0:
        for i in range(player_move_index + 1, player_move_index + 1 + remaining):
            win_moves.append(moves[i])
        lose_moves = moves[player_move_index + 1 + remaining:] + moves[:half - remaining]
    else:
        lose_moves = moves[half:]

    moves_other_than_player = [item for item in moves if item not in win_moves and item != user_move]

    if user_move == pc_move:
        return 0
    elif pc_move in moves_other_than_player:
        return 1
    else:
        return -1
