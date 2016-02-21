import bottle
import os

from dfs import dfs

# x,y
sample_board_17 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,3],
    [1,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,3],
    [0,0,0,5,0,0,0,0,0,0,0,3,0,0,0,0,3],
    [0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0],
    [0,0,5,0,0,0,0,0,3,3,3,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

sample_board_10 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,5,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,5,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0],
    [0,0,5,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

board = []
board_width = 0
board_height = 0
arbok_id = "9fccbadb-30bc-4f6e-845f-057e1ea32975"
arbok_head = []

def get_health(data):
    for snake in data.get('snakes'):
        if snake.get('id') == '9fccbadb-30bc-4f6e-845f-057e1ea32975':
            return snake.get('health')
    return 90

def get_number_of_snakes(data):
    number_of_snakes = 0
    for snake in data.get('snakes'):
        if snake.get('status') == 'alive':
            number_of_snakes = number_of_snakes + 1

    return number_of_snakes

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.jpeg' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#746876',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    ## Create board and initialize to zeros
    initialize_board(data)

    return {
        'taunt': 'ARBOK!!!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    ## Update board with new positions
    profile_board(data)
    food = data['food']

    move = dfs(board, arbok_head,food)

    number_of_snakes = get_number_of_snakes(data)

    if number_of_snakes >= 4:
        result = base_game()
    elif number_of_snakes is 3:
        result = mid_game()
    elif number_of_snakes is 2:
        result = end_game()
    else:
        result = base_game()

    board_string = print_board()
    result['taunt'] = board_string

    return result

def base_game():
    return {
        'move': 'north',
        'taunt': 'ARBOK!'
    }

def mid_game():
    return {
        'move': 'north',
        'taunt': 'ARBOK!'
    }

def end_game():
    return {
        'move': 'north',
        'taunt': 'ARBOK!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'ARBOK!'
    }

def initialize_board(data):
    global board_width
    global board_height

    ## Initialize to zeros
    board_width = data['width']
    board_height = data['height']
    clear_board()

def clear_board():
    global board

    ## Reset to zeros
    board = [[0 for x in range(board_height)] for x in range(board_width)]

def profile_board(data):
    global board
    global arbok_id
    global arbok_head

    ## Reset all spots to zero
    clear_board()

    ## Set snake bodies
    for snake in data['snakes']:
        for coord in snake['coords']:
            if snake['id'] == arbok_id:
                board[coord[0]][coord[1]] = 1
            else:
                board[coord[0]][coord[1]] = 3

    ## Set snake heads
    for snake in data['snakes']:
        if snake['id'] == arbok_id:
            board[snake['coords'][0][0]][snake['coords'][0][1]] = 2
            arbok_head = snake['coords']
        else:
            board[snake['coords'][0][0]][snake['coords'][0][1]] = 4

    ## Set food
    for food in data['food']:
        board[food[0]][food[1]] = 5

## Pretty terrible print function, but use for rudimentary testing
def print_board():
    global board

    board_string = '\n'
    for column in reversed(board):
        board_string += ''.join(str(cell) for cell in column) + '\n'
    return board_string

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
