def solution(s):
    import re
    list = re.findall(".[^A-Z]*", s)
    return " ".join(list)
