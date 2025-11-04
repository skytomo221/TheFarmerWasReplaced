from moves import reset_pos, move_pos

while True:
    reset_pos()
    for x in range(0, get_world_size()):
        for y in range(0, get_world_size()):
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)
    for x in range(get_world_size()):
        move_pos((x, 0))
        sorted_max = get_world_size() - 1
        sorted_min = 0
        while sorted_min < sorted_max:
            sorted = True
            while get_pos_y() < sorted_max:
                if measure() > measure(North):
                    swap(North)
                move(North)
            sorted_max -= 1
            sorted = True
            while get_pos_y() > sorted_min:
                if measure(South) > measure():
                    swap(South)
                move(South)
            sorted_min += 1
    reset_pos()
    for y in range(get_world_size()):
        move_pos((0, y))
        sorted_max = get_world_size() - 1
        sorted_min = 0
        while sorted_min < sorted_max:
            sorted = True
            while get_pos_x() < sorted_max:
                if measure() > measure(East):
                    swap(East)
                move(East)
            sorted_max -= 1
            sorted = True
            while get_pos_x() > sorted_min:
                if measure(West) > measure():
                    swap(West)
                move(West)
            sorted_min += 1
    harvest()
