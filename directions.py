def get_opposite_direction(direction):
	if direction == North:
		return South
	elif direction == South:
		return North
	elif direction == East:
		return West
	elif direction == West:
		return East

def get_all_directions():
  return [North, East, South, West]

def direction_to_vector(direction):
  if direction == North:
    return (0, 1)
  elif direction == East:
    return (1, 0)
  elif direction == South:
    return (0, -1)
  elif direction == West:
    return (-1, 0)
