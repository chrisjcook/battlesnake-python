import bottle
import os
import random

arbok_id = '9fccbadb-30bc-4f6e-845f-057e1ea32975'

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
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    snakes = data[snakes]
    for x in snakes:
        if x.id == arbok_id:
            arbok = x
    food = data.food
    first_food = food[0]

    arbok_head = arbok.coords[0]

    x_dist = food[0] - arbok_head[0]
    y_dist = food[1] - arbok_head[1]

    if x_dist > 0:
        # if food is to right of arbok
        if y_dist > 0:
            # if food is below arbok
            if abs(x_dist) > abs(y_dist):
                # further horizontally east
                return {
                    'move': 'east'
                    'taunt': 'battlesnake-python!'
                }
            else:
                return {
                    'move': 'south'
                    'taunt': 'battlesnake-python!'
                }
        else:
            if abs(x_dist) > abs(y_dist):
                # further horizontally east
                return {
                    'move': 'east'
                    'taunt': 'battlesnake-python!'
                }
            else:
                return {
                    'move': 'north'
                    'taunt': 'battlesnake-python!'
                }
    else:
        if y_dist > 0:
            # if food is below arbok
            if abs(x_dist) > abs(y_dist):
                # further horizontally east
                return {
                    'move': 'west'
                    'taunt': 'battlesnake-python!'
                }
            else:
                return {
                    'move': 'south'
                    'taunt': 'battlesnake-python!'
                }
        else:
            if abs(x_dist) > abs(y_dist):
                # further horizontally east
                return {
                    'move': 'west'
                    'taunt': 'battlesnake-python!'
                }
            else:
                return {
                    'move': 'north'
                    'taunt': 'battlesnake-python!'
                }



@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
