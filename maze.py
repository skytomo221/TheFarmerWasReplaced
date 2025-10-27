from extensions import *
from moves import reset_pos
from calc_pos import add_pos, get_pos
from directions import direction_to_vector, get_all_directions, get_opposite_direction

def get_maze_size():
    return get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)

def generate():
    reset_pos()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, get_maze_size())

def search(maze_map = {}):
    for direction in get_all_directions():
        if can_move(direction):
            if get_pos() not in maze_map:
                maze_map[get_pos()] = [add_pos(get_pos(), direction_to_vector(direction))]
            else:
                maze_map[get_pos()].append(add_pos(get_pos(), direction_to_vector(direction)))
            if add_pos(get_pos(), direction_to_vector(direction)) not in maze_map:
                move(direction)
                search(maze_map)
                move(get_opposite_direction(direction))
    return maze_map

def resolve(maze_map, start = get_pos(), goal = measure(), path = []):
    path = path + [start]
    if start == goal:
        return path
    if start not in maze_map:
        return None
    for node in maze_map[start]:
        if node not in path:
            new_path = resolve(maze_map, node, goal, path)
            if new_path:
                return new_path
    return None

def move_along_path(path):
    for position in path[1:]:
        current_pos = get_pos()
        if position[0] > current_pos[0]:
            move(East)
        elif position[0] < current_pos[0]:
            move(West)
        elif position[1] > current_pos[1]:
            move(North)
        elif position[1] < current_pos[1]:
            move(South)

def run():
    clear()
    cycles = 10
    while True:
        generate()
        maze_map = search()
        for i in range(cycles):
            path = resolve(maze_map)
            move_along_path(path)
            if i < cycles - 1:
                use_item(Items.Weird_Substance, get_maze_size())
            else:
                harvest()
