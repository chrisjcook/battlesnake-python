import bottle
import os

board = []
arbok_id = "9fccbadb-30bc-4f6e-845f-057e1ea32975"

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
        'taunt': 'ARBOK!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    ## Update board with new positions
    profile_board(data)

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
    board = [[0 for x in range(data['height']) for x in range(data['width'])]

    ## Initialize snake heads
    for snake in data['snakes']:
        for coord in snake['coords']:
            if snake['id'] is arbok_id:
                board[coord[0]][coord[1]] = 2
            else:
                board[coord[0]][coord[1]] = 4

def profile_board(data):
    ## Set snake bodies
    for snake in data['snakes']:
        for coord in snake['coords']:
            if snake['id'] is arbok_id:
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


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
