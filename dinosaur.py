
def move_pos(dst):
    (x, y) = dst
    if get_pos_x() < x:
        for _ in range(x - get_pos_x()):
            move(East)
    elif get_pos_x() > x:
        for _ in range(get_pos_x() - x):
            move(West)
    if get_pos_y() < y:
        for _ in range(y - get_pos_y()):
            move(North)
    elif get_pos_y() > y:
        for _ in range(get_pos_y() - y):
            move(South)

change_hat(Hats.Dinosaur_Hat)
while True:
    dst = measure()
    if dst == None:
        change_hat(Hats.Dinosaur_Hat)
    else:
        move_pos(dst)
