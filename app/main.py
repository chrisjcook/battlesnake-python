import bottle
import os

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

    # TODO: Do things with data

    return {
        'taunt': 'ARBOK!!!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data

    number_of_snakes = get_number_of_snakes(data)

    if number_of_snakes >= 4:
        result = base_game(data)
    elif number_of_snakes is 3:
        result = mid_game(data)
    elif number_of_snakes is 2:
        result = end_game(data)
    else:
        result = base_game(data)

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

def end_game(data):
    if not target_enemy(data):
        #go for food
        pass
    else:
        if get_health(data) < 35:
            #go find food
        else:
        #ATTACK!!!
        my_head, my_body, target_head, target_body = determine_position(data)
        
        #globals


    return {
        'move': 'north',
        'taunt': 'ARBOK!'
    }

def determine_position(data):
    my_head = []
    my_body = []
    target_head = []
    target_body = []
    for snake in data.get('snakes'):
        if snake.get('id') == '9fccbadb-30bc-4f6e-845f-057e1ea32975':
            my_head = snake.get('coords')[0]
            my_head = snake.get('coords')[1:]
        else:
            target_head = snake.get('coords')[0]
            target_body = snake.get('coords')[1:]
    return my_head, my_body, target_head, target_body


#For when two snakes left, for end_game, determines if your bigger than enemy snake
def target_enemy(data):
    my_size = 0
    target_size = 0
    for snake in data.get('snakes'):
        if snake.get('id') == '9fccbadb-30bc-4f6e-845f-057e1ea32975':
            my_size = len(snake.get('coords'))
        else:
            target_size = len(snake.get('coords'))
    return my_size > target_size


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
