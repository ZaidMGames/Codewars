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
    
    
            
            