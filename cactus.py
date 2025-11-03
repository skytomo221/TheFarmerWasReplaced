from moves import reset_pos

reset_pos()

while True:
    for x in range(0, get_world_size()):
        for y in range(0, get_world_size()):
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)
    sorted = False
    while not sorted:
        sorted = True
        for x in range(0, get_world_size()):
            for y in range(0, get_world_size()):
                if measure() > measure(North) and get_pos_y() + 1 < get_world_size():
                    swap(North)
                    sorted = False
                if measure() > measure(East) and get_pos_x() + 1 < get_world_size():
                    swap(East)
                    sorted = False
                move(North)
            move(East)
    harvest()
