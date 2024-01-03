def narcissistic(value):
    list1 = list(str(value))
    sum = 0
    for i in range(len(str(value))):
        sum += int(list1[i]) ** len(str(value))
    if sum == value:
        return True
    else:
        return False
        
