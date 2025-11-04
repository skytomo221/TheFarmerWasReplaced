from moves import reset_pos, move_pos

def plant_cacti(i = 0):
    x_min = (get_world_size() / max_drones() * i) // 1
    x_max = (get_world_size() / max_drones() * (i + 1)) // 1
    move_pos((x_min, 0))
    for _ in range(x_min, x_max):
        for _ in range(0, get_world_size()):
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)

def vertical_sort(i = 0):
    x_min = (get_world_size() / max_drones() * i) // 1
    x_max = (get_world_size() / max_drones() * (i + 1)) // 1
    move_pos((x_min, 0))
    for x in range(x_min, x_max):
        for _ in range(0, get_world_size()):
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)
    for x in range(x_min, x_max):
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

def horizontal_sort(i = 0):
    y_min = (get_world_size() / max_drones() * i) // 1
    y_max = (get_world_size() / max_drones() * (i + 1)) // 1
    move_pos((y_min, 0))
    for x in range(0, get_world_size()):
        for y in range(y_min, y_max):
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)
    for y in range(y_min, y_max):
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

def create_worker_task_plant_cacti(i = 0):
    def worker_task():
        plant_cacti(i)
    return worker_task

def create_worker_task_vertical_sort(i = 0):
    def worker_task():
        vertical_sort(i)
    return worker_task

def create_worker_task_horizontal_sort(i = 0):
    def worker_task():
        horizontal_sort(i)
    return worker_task

def main():
    while True:
        reset_pos()
        i = 1
        while num_drones() < max_drones():
            spawn_drone(create_worker_task_plant_cacti(i))
            i += 1
        plant_cacti()
        while num_drones() != 1:
            pass
        i = 1
        while num_drones() < max_drones():
            spawn_drone(create_worker_task_vertical_sort(i))
            i += 1
        vertical_sort()
        while num_drones() != 1:
            pass
        i = 1
        while num_drones() < max_drones():
            spawn_drone(create_worker_task_horizontal_sort(i))
            i += 1
        horizontal_sort()
        while num_drones() != 1:
            pass
        harvest()
