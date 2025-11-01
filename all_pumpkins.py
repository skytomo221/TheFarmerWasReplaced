from moves import move_pos

def init(i = 0):
    uninspected_pumpkins = set()
    x_min = (get_world_size() / max_drones() * i) // 1
    x_max = (get_world_size() / max_drones() * (i + 1)) // 1
    for x in range(x_min, x_max):
        for y in range(get_world_size()):
            uninspected_pumpkins.add((x, y))
    return uninspected_pumpkins

def can_all_harvest(uninspected_pumpkins):
    return len(uninspected_pumpkins) == 0

def run(i = 0):
    uninspected_pumpkins = init(i)
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
        if can_all_harvest(uninspected_pumpkins):
            if i != 0:
                return
            elif num_drones() == 1:
                harvest()
                return

def create_worker_task(i = 0):
    def worker_task():
        run(i)
    return worker_task

def main():
    while True:
        i = 1
        while num_drones() < max_drones():
            spawn_drone(create_worker_task(i))
            i += 1
        run()

init()
