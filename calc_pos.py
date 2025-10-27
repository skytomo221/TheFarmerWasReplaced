def get_pos():
      return (get_pos_x(), get_pos_y())

def add_pos(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def sub_pos(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])

def equal_pos(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]
