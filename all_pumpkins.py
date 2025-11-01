from moves import move_pos

uninspected_pumpkins = set()

def init():
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            uninspected_pumpkins.add((x, y))

def can_all_harvest():
    return len(uninspected_pumpkins) == 0

def run():
    global uninspected_pumpkins
    while True:
        next_uninspected_pumpkins = set()
        for uninspected_pumpkin in uninspected_pumpkins:
            move_pos(uninspected_pumpkin)
            if get_water() < 0.5:
                use_item(Items.Water)
            if get_ground_type() == Grounds.Grassland:
                till()
            if can_harvest():
                pass
            else:
                next_uninspected_pumpkins.add((get_pos_x(), get_pos_y()))
            plant(Entities.Pumpkin)

        uninspected_pumpkins = next_uninspected_pumpkins
        if can_all_harvest():
            harvest()
            init()

init()
