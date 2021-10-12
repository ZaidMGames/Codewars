# You will be given a string with sets of characters, (i.e. words), seperated by between one and three spaces (inclusive).

# Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m") or the negative/second half ("n"-"z").

# Return True/true if there are more (or equal) positive words than negative words, False/false otherwise.

# "A big brown fox caught a bad rabbit" => True/true
# "Xylophones can obtain Xenon." => False/false

def connotation(strng):
    print (strng)
    first = "abcdefghijklm"
    second = "nopqrstuvwxyz"
    
    f = 0
    s = 0
    for word in strng.split(" "):
        word = word.strip()
        print(word)
        if word != "":
            if word[0].lower() in first:
                f += 1
            elif word[0].lower() in second:
                s+= 1
    if f >= s:
        return True
    else:
        return False