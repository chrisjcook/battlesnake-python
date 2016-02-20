def check_around(data):
    arbok_id = '9fccbadb-30bc-4f6e-845f-057e1ea32975'
    snakes = data['snakes']
    filled_blocks = []
    for x in snakes:
        if x['id'] == arbok_id:
            arbok = x
        filled_blocks.extend(x['coords'])
    arbok_head = arbok['coords'][0]

    x = arbok_head[0]
    y = arbok_head[1]
    valid = [[x, y + 1], [x, y - 1], [x + 1, y], [x -1, y]]
    for c in arround:
        if c in filled_blocks:
            valid.remove(c)
    return valid

def find_food(data):
    arbok_id = '9fccbadb-30bc-4f6e-845f-057e1ea32975'
    snakes = data['snakes']
    for x in snakes:
        if x['id'] == arbok_id:
            arbok = x
    food = data['food']
    valid = check_around(data)
    if food:
        first_food = food[0]

        arbok_head = arbok['coords'][0]

        x_dist = first_food[0] - arbok_head[0]
        y_dist = first_food[1] - arbok_head[1]

        if x_dist > 0:
            # if food is to right of arbok
            if y_dist > 0:
                # if food is below arbok
                if abs(x_dist) > abs(y_dist):
                    # further horizontally east
                    if [arbok_head[0] + 1, arbok_head[1]] not in valid:
                        return {'move': 'east', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'south', 'taunt': 'battlesnake-python!'}
                else:
                    if [arbok_head[0], arbok_head[1] + 1] not in valid:
                        return {'move': 'south', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'east', 'taunt': 'battlesnake-python!'}
            else:
                # if food is above arbok
                if abs(x_dist) > abs(y_dist):
                    # further horizontally east
                    if [arbok_head[0] + 1, arbok_head[1]] not in valid:
                        return {'move': 'north', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'east', 'taunt': 'battlesnake-python!'}
                else:
                    if [arbok_head[0], arbok_head[1] + 1] not in valid:
                        return {'move': 'east', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'north', 'taunt': 'battlesnake-python!'}
        else:
            if y_dist > 0:
                # if food is below arbok
                if abs(x_dist) > abs(y_dist):
                    # further horizontally west
                    if [arbok_head[0] - 1, arbok_head[1]] not in valid:
                        return {'move': 'south', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'west', 'taunt': 'battlesnake-python!'}
                else:
                    if [arbok_head[0], arbok_head[1] + 1] not in valid:
                        return {'move': 'west', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'south', 'taunt': 'battlesnake-python!'}
            else:
                # if food is above arbok
                if abs(x_dist) > abs(y_dist):
                    # further horizontally west
                    if [arbok_head[0] - 1, arbok_head[1]] not in valid:
                        return {'move': 'north', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'west', 'taunt': 'battlesnake-python!'}
                else:
                    if [arbok_head[0], arbok_head[1] + 1] not in valid:
                        return {'move': 'west', 'taunt': 'battlesnake-python!'}
                    else:
                        return {'move': 'north', 'taunt': 'battlesnake-python!'}
    else:
        return {'move': 'north', 'taunt': 'battlesnake-python!'}
