def reset_pos():
    while get_pos_x() != 0:
        move(West)
    while get_pos_y() != 0:
        move(South)

def move_east(n):
    if n > 0:
        for _ in range(n):
            move(East)
    else:
        for _ in range(-n):
            move(West)

def move_north(n):
    if n > 0:
        for _ in range(n):
            move(North)
    else:
        for _ in range(-n):
            move(South)

def calc_move_n(org, dst):
    if (get_world_size() / 2 < dst - org):
        return dst - org - get_world_size()
    elif (dst - org < -get_world_size() / 2):
        return dst - org + get_world_size()
    else:
        return dst - org

def move_pos(dst):
    (x, y) = dst
    move_east(calc_move_n(get_pos_x(), x))
    move_north(calc_move_n(get_pos_y(), y))
