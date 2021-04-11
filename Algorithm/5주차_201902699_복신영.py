
def next_worm_direction(present_direction, next_direction):
    if next_direction == 'R':
        if present_direction == 'U':
            return 'R'
        if present_direction == 'R':
            return 'D'
        if present_direction == 'D':
            return 'L'
        if present_direction == 'L':
            return 'U'
    elif next_direction == 'L':
        if present_direction == 'U':
            return 'L'
        if present_direction == 'R':
            return 'U'
        if present_direction == 'D':
            return 'R'
        if present_direction == 'L':
            return 'D'


def next_worm_position(present_position, present_direction):
    if present_direction == 'R':
        return [present_position[0], present_position[1] + 1]
    elif present_direction == 'D':
        return [present_position[0] + 1, present_position[1]]
    elif present_direction == 'L':
        return [present_position[0], present_position[1] - 1]
    elif present_direction == 'U':
        return [present_position[0] - 1, present_position[1]]


def is_worm_out(worm_position, map_size):
    if worm_position[0] > map_size or worm_position[0] <= 0 or worm_position[1] > map_size or worm_position[1] <= 0:
        return True
    else:
        return False


def is_worm_hit_oneself(worm_head, body, size):
    if worm_head in body[-size:]:
        return True
    else:
        return False


def game():
    # input
    n = int(input())
    k = int(input())
    t = int(input())

    food = list()
    for _ in range(k):
        a, b = input().split()
        food.append([int(a), int(b)])

    direction = list()
    for _ in range(t):
        a, b = input().split()
        direction.append((int(a), b))

    # initial variable
    worm_size = 1
    worm_present_head_position = [1, 1]
    worm_present_direction = 'R'
    worm_present_body_position = list()

    step = 0

    worm_present_body_position.append(worm_present_head_position)

    # game start
    while True:
        step += 1
        worm_present_head_position = next_worm_position(worm_present_head_position, worm_present_direction)
        worm_present_body_position.append(worm_present_head_position)

        for i in direction:
            turning_turn, next_direction = i
            # turning step!
            if step == turning_turn:
                worm_present_direction = next_worm_direction(worm_present_direction, next_direction)

        # If eat the food
        if worm_present_head_position in food:
            worm_size += 1

        # If worm out
        if is_worm_out(worm_present_head_position, n):
            return step

        # If worm hit himself
        if is_worm_hit_oneself(next_worm_position(worm_present_head_position, worm_present_direction),
                               worm_present_body_position, worm_size):
            step += 1
            return step


answer = game()
print(answer)
