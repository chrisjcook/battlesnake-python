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
    for c in valid:
        if c in filled_blocks:
            valid.remove(c)
    return valid

def nearest_food(data, arbok_head, food):
    nearest = food[0]
    n_total = abs(nearest[0] - arbok_head[0]) + abs(nearest[1] - arbok_head[1])
    for f in food:
        x_dist = f[0] - arbok_head[0]
        y_dist = f[1] - arbok_head[1]
        total = abs(x_dist) + abs(y_dist)
        if n_total > total:
            # n_total is further
            nearest = f
            n_total = total
    return nearest

def valid_coord(data, arbok_head, valid):
    for c in valid:
        x_dist = c[0] - arbok_head[0]
        y_dist = y[1] - arbok_head[1]
        if x_dist > 0:
            return 'east'
        if x_dist < 0:
            return 'west'
        if y_dist > 0:
            return 'south'
        if y_dist < 0:
            return 'north'

def find_food(data):
    arbok_id = '9fccbadb-30bc-4f6e-845f-057e1ea32975'
    snakes = data['snakes']
    for x in snakes:
        if x['id'] == arbok_id:
            arbok = x

    valid = check_around(data)
    food = data['food']
    if food:
        arbok_head = arbok['coords'][0]

        nearest = nearest_food(data, arbok_head, food)

        x_dist = nearest[0] - arbok_head[0]
        y_dist = nearest[1] - arbok_head[1]

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
