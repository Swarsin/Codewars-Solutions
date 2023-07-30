#My solution to "8 Kyu - Draw Stairs"
def draw_stairs(n):
    string = ''
    for i in range(1, n):
        part = "I\n" + (" " * i)
        string += part
        if i == n-1:
            string += "I"
    return string

#Best solution to "8 Kyu - Draw Stairs"
def draw_stairs(n):
    return '\n'.join(' '* i + 'I' for i in range(n))