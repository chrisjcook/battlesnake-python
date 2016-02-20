# returns north, east, south, or west

possible_directions = {
    'n' : 'north',
    's' : 'south',
    'e' : 'east',
    'w' : 'west'
}

# [0,0]
#  x y

def dfs(board, our_head, food):
    # distances = []
    smallest = len(board)
    move = ''
    for coord in food:
        head = our_head[:]
        distance, moves = __do_search(board, head, coord)
        if distance < board:
            smallest = distance
            move = moves[0]
            print distance
        # distances.append(distance)
    return move

# [2,8], [0,7]
def __do_search(board, our_head, item):
    distance = 0
    current_coord = our_head
    moves = []
    # TODO: remove direction that tail is in
    while not __is_equal(current_coord, item):

        potential_moves = {
            'north' : 1.0,
            'south' : 1.0,
            'east' : 1.0,
            'west' : 1.0
        }

        __find_enemy_snakes(board, our_head, potential_moves)
        __detect_board_limits(board, our_head, potential_moves)

        x_delta = current_coord[0] - item[0]
        if not x_delta == 0:
            if board[current_coord[0] + 1][current_coord[1]] == 4:
                __increase_weight(potential_moves, 'east', 0)
            if x_delta < 0: # go right/east
                current_coord[0] += 1
                __increase_weight(potential_moves, 'east', 2)
            else: # go left/west
                current_coord[0] -= 1
                __increase_weight(potential_moves, 'west', 2)
        else:
            __increase_weight(potential_moves, 'east', 0.5)
            __increase_weight(potential_moves, 'west', 0.5)

        y_delta = current_coord[1] - item[1]
        if not y_delta == 0:

            if y_delta < 0: # go down/south
                current_coord[1] += 1
                __increase_weight(potential_moves, 'south', 2)
            else: # go up/north
                current_coord[1] -= 1
                __increase_weight(potential_moves, 'north', 2)

        # print current_coord
        move = __get_best_move(potential_moves)
        moves.append(move)
        distance += 1

    return distance, moves

def __find_enemy_snakes(board, our_head, moves):
    if board[our_head[0]][our_head[1] + 1] == 3 or board[our_head[0]][our_head[1] + 1] == 4: # other snake above/north
        __increase_weight(moves, 'north', 0)
    if board[our_head[0] + 1][our_head[1]] == 3 or board[our_head[0] + 1][our_head[1]] == 4: # other snake right/east
        __increase_weight(moves, 'east', 0)
    if board[our_head[0] - 1][our_head[1]] == 3 or board[our_head[0] - 1][our_head[1]] == 4: # other snake left/west
        __increase_weight(moves, 'west', 0)
    if board[our_head[0]][our_head[1] - 1] == 3 or board[our_head[0]][our_head[1] - 1] == 4: # other snake down/south
        __increase_weight(moves, 'south', 0)

def __detect_board_limits(board, our_head, moves):
    x = our_head[0]
    y = our_head[1]

    if y - 1 < 0:
        __increase_weight(moves, 'south', 0)
    if y + 1 >= 17:
        __increase_weight(moves, 'north', 0)
    if x + 1 >= 17:
        __increase_weight(moves, 'east', 0)
    if x - 1 < 0:
        __increase_weight(moves, 'west', 0)

def __increase_weight(weights, direction, factor):
    weights[direction] *= factor

def __get_best_move(weights):
    best = weights['north']
    best_key = 'north'
    for key in weights:
        if weights[key] > best:
            best = weights[key]
            best_key = key

    return best_key


def __is_equal(a,b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False
