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
        distance, moves = __do_search(head, coord)
        if distance < board:
            smallest = distance
            move = moves[0]
            print distance
        # distances.append(distance)
    return move

# [2,8], [0,7]
def __do_search(our_head, item):
    distance = 0
    current_coord = our_head
    moves = []
    while not __is_equal(current_coord, item):
        potential_moves = ['north', 'south', 'east', 'west']
        x_delta = current_coord[0] - item[0]
        if not x_delta == 0:
            if x_delta < 0: # go right/east
                current_coord[0] += 1
                moves.append('east')
            else: # go left/west
                current_coord[0] -= 1
                moves.append('west')
        else:
            y_delta = current_coord[1] - item[1]
            if y_delta < 0: # go down/south
                current_coord[1] += 1
                moves.append('south')
            else: # go up/north
                current_coord[1] -= 1
                moves.append('north')

        print current_coord
        distance += 1

    return distance, moves

def __is_equal(a,b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False
