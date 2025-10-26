from moves import reset_pos
import all_pumpkins
import maze

def main():
	while True: 
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				# if x % 3 == 1 and y % 3 == 1:
				#	use_item(Items.Fertilizer)
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

# clear()
#all_pumpkins.do()
# main()
maze.do()
