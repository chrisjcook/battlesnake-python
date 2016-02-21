import bottle
import os
import math

board = []
board_width = 17
board_height = 17

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
        result = base_game(data)
    elif number_of_snakes is 3:
        result = mid_game(data)
    elif number_of_snakes is 2:
        result = end_game(data)
    else:
        result = base_game(data)

    board_string = print_board()
    result['taunt'] = board_string

    return result

def base_game(data):
    return {
        'move': 'north',
        'taunt': 'base!'
    }

def mid_game(data):
    return {
        'move': 'north',
        'taunt': 'mid!'
    }

def end_game(data):
    global board
    global board_width
    global board_height

    next_coord = []

    if get_health(data) < 35:
        pass
        #go find food
    else:
        #ATTACK!!!
        my_head, my_body, target_head, target_body = determine_position(data)
        grid_list = get_grid_line()
        quadrant, quadrant_coord = get_quadrant(my_head) #quadrant_coord your in
        if my_head in grid_list:
            index = grid_list.index(my_head)
            if index == len(grid_list) -1:
                next_coord == grid_list[0]
            else:
                next_coord = grid_list[index + 1]
                if board[next_coord[0]][next_coord[1]] == 0:
                    x_val = next_coord[0] - my_head[0]
                    y_val = next_coord[1] - my_head[1]
                    if x_val != 0:
                        #moving next dir
                        if x_val > 0:
                            return {'move': 'east', 'taunt': 'in here!'}
                        else:
                            return {'move': 'west', 'taunt': 'in here!'}
                    else:
                        if y_val > 0:
                            return {'move': 'south', 'taunt': 'in here!'}
                        else:
                            return {'move': 'north', 'taunt': 'in here!'}
                elif board[my_head[0]+1][my_head[1]] == 0:
                    return {'move': 'east', 'taunt': 'in here!'}
                elif board[my_head[0]][my_head[1+1]] == 0:
                    return {'move': 'south', 'taunt': 'in here!'}
                elif board[my_head[0]-1][my_head[1]] == 0:
                    return {'move': 'west', 'taunt': 'in here!'}
                elif board[my_head[0]][my_head[1-1]] == 0:
                    return {'move': 'north', 'taunt': 'in here!'}
        else:
            if board[quadrant_coord[0]][quadrant_coord[1]] == 0:
                x_val = quadrant_coord[0] - my_head[0]
                y_val = quadrant_coord[1] - my_head[1]
                x_min_dist = abs(x_val)
                y_min_dist = abs(y_val)
                if x_min_dist < y_min_dist:
                    if x_val < 0:
                        #move right
                        return {'move': 'west', 'taunt': 'else!'}
                    else:
                        return {'move': 'east', 'taunt': 'else!'}
                else:
                    if y_val < 0:
                        return {'move': 'north', 'taunt': 'else!'}
                    else:
                        return {'move': 'south', 'taunt': 'else!'}
            elif board[my_head[0]+1][my_head[1]] == 0:
                return {'move': 'east', 'taunt': 'else!'}
            elif board[my_head[0]][my_head[1+1]] == 0:
                return {'move': 'south', 'taunt': 'else!'}
            elif board[my_head[0]-1][my_head[1]] == 0:
                return {'move': 'west', 'taunt': 'else!'}
            elif board[my_head[0]][my_head[1-1]] == 0:
                return {'move': 'north', 'taunt': 'else!'}
    return {
        'move': 'north',
        'taunt': 'Shouldnt be here'
    }

def get_quadrant(my_head):
    pow(my_head[0]-2, 2)

    top_left = math.sqrt(pow((my_head[0]-2),2) + pow(my_head[1] - 2, 2))
    top_right = math.sqrt(pow((my_head[0]-board_width-2),2) + pow(my_head[1] - 2,2))
    bottom_left = math.sqrt(pow((my_head[0]-2),2) + pow(my_head[1] - board_height-2,2))
    bottom_right = math.sqrt(pow(my_head[0] - board_width-2,2) + pow(my_head[1] - board_height-2,2))
    smallest = min(top_left, top_right, bottom_left, bottom_right)
    if smallest == top_left:
        return 1, [2, 2]
    elif smallest == top_right:
        return 4, [board_width-2, 2]
    elif smallest == bottom_left:
        return 2, [2, board_height-2]
    elif smallest == bottom_right:
        return 3, [board_width-2, board_height-2]



def get_grid_line():
    global board
    global board_width
    global board_height
    y_values = range(2, board_height-2)
    x_values = range(3, board_width-3)
    grid_1 = []
    grid_2 = []
    grid_3 = []
    grid_4 = []
    for y in y_values:
        #west and east lines of board
        grid_1.append([2, y])
        grid_2.append([board_width-2, y])
    for x in x_values:
        grid_3.append([x, 2])
        grid_4.append([x, board_height-2])
    grid_1.extend(grid_4+grid_2+grid_3)
    return grid_1


def determine_position(data):
    my_head = []
    my_body = []
    target_head = []
    target_body = []
    for snake in data.get('snakes'):
        if snake.get('id') == '9fccbadb-30bc-4f6e-845f-057e1ea32975':
            my_head = snake.get('coords')[0]
            my_body = snake.get('coords')[1:]
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
