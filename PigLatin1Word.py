# def pig_latin(s):
#     s = s.lower()
#     vowels = ["a", "e", "i", "o", "u"]
#     if s[0] in vowels:
#         return s + "way"
#     else:
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 end = s[0:i]
#                 return s.replace(end, "") + end + "ay"
            
# print(pig_latin("Spaghetti"))

# def pig_latin(s):
#     s = s.lower()
#     vowels = ["a", "e", "i", "o", "u"]
#     if s.isalpha() == "False":
#         return None
#     elif s == '':
#         return "ay"
#     elif s[0] in vowels:
#         return s + "way"
#     else:
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 end = s[0:i]
#                 return s.replace(end, "") + end + "ay"
# import re
# def pig_latin(s):
#     s = s.lower()
#     x = re.search("[a-z]+", s)
#     if x == None:
#         return None
#     x = re.search("([aeiou])", s)
#     if x == None:
#         return s + "ay"
#     x = re.search("^[aeiou]")
#     if x != None:
#         return s + "way"
#     x = re.search("^[b-df-hj-np-tv-xz]")
#     s += (s[0:x.span()[0]] + "ay")
#     s = re.sub(s[0:x], "", 1)
#     return s
    
#Working Solution:
import re
def pig_latin(s):
    s = s.lower()
    x = re.search("[a-z]", s)
    if x == None:
        return None
    x = re.search("[0-9]", s)
    if x != None:
        return None
    x = re.search("[aeiou]", s)
    if x == None:
        return s + "ay"
    x = re.search("^[aeiou]", s)
    if x != None:
        return s + "way"
    x = re.search("^[b-df-hj-np-tv-z]", s)
    if x != None:
        y = re.search("[aeiou]", s)
        return s[y.span()[0]:] + s[:y.span()[0]] + "ay"