def solution(s):
    a = ""
    for char in s:
        if char.isupper():
            a+=" "
        a+= char
    return a