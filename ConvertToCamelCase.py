def to_camel_case(text):
    import re
    list = re.split("-|_", text)
    string = list[0]
    for i in range(1, len(list)):
        list[i] = list[i].capitalize()
        string += list[i]
    return string
        
