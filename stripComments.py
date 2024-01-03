# plan:
#remove whitespace characters before the markers and the new line character
# 
def strip_comments(strng, markers):
    for i in range(len(strng)):
        if strng[i] in markers or strng[i:i+1] == '\n':
            if strng[i-1] == ' ':
                strng = strng.replace(" ", "")
            if strng[i] in markers:
                for j in range(i, len(strng)):
                    if strng[j:j+1] == '\n' or j == len(strng):
                        strng = strng.replace(strng[i:j-1], "")
    print(strng)

strip_comments('a #b\nc\nd $e f g', ['#', '$'])

