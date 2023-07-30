#My solution to "7 Kyu - Jaden Casing"
def to_jaden_case(string):
    words = string.split()
    list = [i.capitalize() for i in words]
    return ' '.join(list)

#Best Solution to "7 Kyu - Jaden Casing"
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())