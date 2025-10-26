from moves import reset_pos
from calc_pos import add_pos, get_pos
from directions import direction_to_vector, get_opposite_direction

def get_maze_size():
	return get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)

def generate_maze():
	reset_pos()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_maze_size())

def resolve_maze(history = [], harvest_enabled = True):
	if get_entity_type() == Entities.Treasure:
		if harvest_enabled:
			harvest()
		else:
			use_item(Items.Weird_Substance, get_maze_size())
		return True
	directions = [North, West, South, East]
	for direction in directions:
		if can_move(direction) and (add_pos(get_pos(), direction_to_vector(direction)) not in history):
			move(direction)
			history.append(get_pos())
			if resolve_maze(history, harvest_enabled):
				return True
			else:
				move(get_opposite_direction(direction))
				history.pop()
	return False

def do():
	clear()
	while True:
		generate_maze()
		for _ in range(10):
			resolve_maze([get_pos()], False)
		resolve_maze([get_pos()])
