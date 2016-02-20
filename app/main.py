import bottle
import os

from dfs import dfs

# x,y
sample_board = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,3],
    [1,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3],
    [2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,3],
    [0,0,0,5,0,0,0,0,0,0,0,3,0,0,0,0,3],
    [0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0],
    [0,0,5,0,0,0,0,0,3,3,3,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

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

    # TODO: Do things with data

    return {
        'taunt': 'ARBOK!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    food = [[3, 12]]
    dfs(sample_board, [1,2], food)

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


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
