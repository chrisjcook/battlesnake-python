# returns north, east, south, or west

possible_directions = {
    'n' : 'north',
    's' : 'south',
    'e' : 'east',
    'w' : 'west'
}

def dfs(board, our_head, food):
    distances = []
    for coord in food:
        distance = __do_search(our_head, coord)
        distances.append(distance)

    return possible_directions[n]

def __do_search(our_head, item):
    distance = 0
    current_coord = our_head
    queue = []
    queue.insert(0, our_head)
    # while not len(queue) is 0:


    return distance

def __is_equal(a,b):
    if a[0] == b[0] and
