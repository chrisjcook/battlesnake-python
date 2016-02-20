import bottle
import os

i = 0

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
    print "START: " + data

    # TODO: Do things with data

    return {
        'taunt': 'ARBOK!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    print "MOVE: " + data
    if i ==0:
        i+=1
        return {'move': 'north', 'taunt': 'ARBOK!'}
    else:
        return {'move': 'south', 'taunt': 'ARBOK!'}

    # TODO: Do things with data

    return {
        'move': 'north',
        'taunt': 'ARBOK!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    print "END: " + data

    # TODO: Do things with data

    return {
        'taunt': 'ARBOK!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
