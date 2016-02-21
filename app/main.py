import bottle
import os

from find_food import find_food

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
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    if data['turn'] == 0:
        snakes = data['snakes']
        for x in snakes:
            if x['id'] == arbok_id:
                arbok = x
        arbok_head = arbok['coords'][0]
        if arbok_head[1] < 8:
            return {'move': 'north', 'taunt': 'battlesnake-python'}
        else:
            return {'move': 'north', 'taunt': 'battlesnake-python'}

    return find_food(data)

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
