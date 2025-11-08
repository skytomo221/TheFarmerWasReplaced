def get_pos():
      return (get_pos_x(), get_pos_y())

def add_pos(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def sub_pos(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])

def mul_pos(pos, scalar):
    return (pos[0] * scalar, pos[1] * scalar)

def div_pos(pos, scalar):
    return (pos[0] / scalar, pos[1] / scalar)

def equal_pos(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]
