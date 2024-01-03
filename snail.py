#in progress

def create_list(snail_map):
    spaces = []
    for j in range(len(snail_map)-1, 0, -1):
        for i in range(2):
            spaces.append(j)
    return [len(snail_map)-1] + spaces


def snail(snail_map):
    spaces = create_list(snail_map)
    x = 0
    y = 0
    current = snail_map[x][y]
    axis = 'y'
    value = 1
    for i in spaces:
        for j in range(spaces[j]):
            if axis == 'y':
                
                current = 








print(create_list([[1,2,3],
        [4,5,6],
        [7,8,9]]))
