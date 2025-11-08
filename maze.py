from extensions import *
from moves import reset_pos
from calc_pos import add_pos, get_pos, div_pos
from directions import direction_to_vector, get_all_directions, get_opposite_direction

def get_maze_size():
    return get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)

def generate():
    reset_pos()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, get_maze_size())

def search(walls = set(), searched = set()):
    def get_wall_pos(direction):
        return add_pos(get_pos(), div_pos(direction_to_vector(direction), 2))
    searched.add(get_pos())
    for direction in get_all_directions():
        neighbor = add_pos(get_pos(), direction_to_vector(direction))
        if can_move(direction) and neighbor not in searched:
            move(direction)
            search(walls, searched)
            move(get_opposite_direction(direction))
        elif not can_move(direction):
            walls.add(get_wall_pos(direction))
    return walls

def create_cost_map(walls, start, goal):
    def get_wall_pos(pos, direction):
        return add_pos(pos, div_pos(direction_to_vector(direction), 2))
    cost = 0
    cost_map = {start: 0}
    neighbors = [start]
    while goal not in cost_map:
        cost += 1
        next_neighbors = []
        for neighbor in neighbors:
            for direction in get_all_directions():
                if get_wall_pos(neighbor, direction) in walls:
                    continue
                next_pos = add_pos(neighbor, direction_to_vector(direction))
                if next_pos not in cost_map or cost < cost_map[next_pos]:
                    cost_map[next_pos] = cost
                    next_neighbors.append(next_pos)
        neighbors = next_neighbors
    return cost_map

def create_path(walls, cost_map, start, goal):
    def get_wall_pos(pos, direction):
        return add_pos(pos, div_pos(direction_to_vector(direction), 2))
    path = [goal]
    current_pos = goal
    while current_pos != start:
        for direction in get_all_directions():
            next_pos = add_pos(current_pos, direction_to_vector(direction))
            is_in_maze = next_pos in cost_map
            is_wall_free = get_wall_pos(current_pos, direction) not in walls
            is_cost_correct = is_in_maze and cost_map[next_pos] == cost_map[current_pos] - 1
            if is_in_maze and is_wall_free and is_cost_correct:
                path.insert(0, next_pos)
                current_pos = next_pos
                break
    return path

def resolve(walls, start = get_pos(), goal = measure(), path = []):
    cost_map = create_cost_map(walls, start, goal)
    path = create_path(walls, cost_map, start, goal)
    return path

def update_walls(walls):
    for direction in get_all_directions():
        wall_pos = add_pos(get_pos(), div_pos(direction_to_vector(direction), 2))
        if wall_pos in walls and can_move(direction):
            walls.remove(wall_pos)
    return walls

def move_along_path(path, walls):
    for position in path[1:]:
        update_walls(walls)
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
    cycles = 100
    while True:
        generate()
        walls = search()
        for i in range(cycles):
            path = resolve(walls)
            move_along_path(path, walls)
            if i < cycles - 1:
                use_item(Items.Weird_Substance, get_maze_size())
            else:
                harvest()
