from moves import move_pos
import all_pumpkins
import maze

def do(i = 0):
    x_min = get_world_size() / max_drones() * i
    x_max = get_world_size() / max_drones() * (i + 1)
    move_pos((x_min, 0))
    while True:
        for x in range(x_min, x_max):
            for y in range(get_world_size()):
                # if x % 3 == 1 and y % 3 == 1:
                #    use_item(Items.Fertilizer)
                if can_harvest():
                    harvest()
                if get_water() < 0.5:
                    use_item(Items.Water)
                if get_pos_x() <= get_world_size() / 8:
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Cactus)
                elif get_pos_x() <= get_world_size() / 4:
                    pass
                elif get_pos_x() <= get_world_size() / 2:
                    plant(Entities.Tree)
                else:
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Carrot)
                move(North)
            move(East)
        move_pos((x_min, 0))

def create_worker_task(i = 0):
    def worker_task():
        do(i)
    return worker_task

def main():
    i = 1
    while num_drones() < max_drones():
        spawn_drone(create_worker_task(i))
        i += 1
    do()

#all_pumpkins.do()
main()
# maze.do()
