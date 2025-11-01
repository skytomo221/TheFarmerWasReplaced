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

def create_cost_map(maze_map, start, goal):
    cost = 0
    cost_map = {}
    next_neighbors = [start]
    while goal not in cost_map:
        cost += 1
        new_next_neighbors = []
        for neighbor in next_neighbors:
            if neighbor not in cost_map:
                cost_map[neighbor] = cost
                new_next_neighbors += maze_map[neighbor]
        next_neighbors = new_next_neighbors
    return cost_map

def create_path(maze_map, cost_map, start, goal):
    path = [goal]
    current_pos = goal
    while current_pos != start:
        for neighbor in maze_map[current_pos]:
            if neighbor in cost_map and cost_map[neighbor] == cost_map[current_pos] - 1:
                path.insert(0, neighbor)
                current_pos = neighbor
                break
    return path

def resolve(maze_map, start = get_pos(), goal = measure(), path = []):
    cost_map = create_cost_map(maze_map, start, goal)
    path = create_path(maze_map, cost_map, start, goal)
    return path

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
