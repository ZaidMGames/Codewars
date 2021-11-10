"""Is it possible to write a book without the letter 'e' ?

Task
Given String str, return:

How much "e" does it contains (case-insensitive) in string format.
If given String doesn't contain any "e", return: "There is no "e"."
If given String is empty, return empty String.
If given String is `null`/`None`/`nil`, return `null`/`None`/`nil`
"""
def find_e(s):
    e = 0
    if s != None:
        for char in s:
            if char.lower() == "e":
                e += 1
        
    if e > 0 :
        return str(e)
    elif e == 0 and s != None and s != '':
        return 'There is no "e".'
    elif s == '':
        return s
    elif s == None:
        return None
    