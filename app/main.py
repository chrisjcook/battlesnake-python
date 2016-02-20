import bottle
import os

board = []
board_width = 0
board_height = 0

arbok_id = "9fccbadb-30bc-4f6e-845f-057e1ea32975"

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

    number_of_snakes = get_number_of_snakes(data)

    if number_of_snakes >= 4:
        result = base_game()
    elif number_of_snakes is 3:
        result = mid_game()
    elif number_of_snakes is 2:
        result = end_game()
    else:
        result = base_game()

    ## TEST
    result['taunt'] = print_board()

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
    ## Initialize to zeros
    clear_board(data)
    board_width = data['width']
    board_height data['height']

def clear_board(data):
    ## Reset to zeros
    board = [[0 for x in range(data['height'])] for x in range(data['width'])]

def profile_board(data):
    clear_board(data)

    ## Set snake bodies
    for snake in data['snakes']:
        for coord in snake['coords']:
            if snake['id'] == arbok_id:
                board[coord[0]][coord[1]] = 1
            else:
                board[coord[0]][coord[1]] = 3

    ## Set snake heads
    for snake in data['snakes']:
        if snake['id'] is arbok_id:
            board[snake['coords'][0][0]][snake['coords'][0][1]] = 2
        else:
            board[snake['coords'][0][0]][snake['coords'][0][1]] = 4

    ## Set food
    for food in data['food']:
        board[food[0]][food[1]] = 5

def print_board():
    for column in board:
        print column + "\n"
    print "\n\n"

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
