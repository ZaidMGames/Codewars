def is_palindrome(s):
    a = s [::-1]
    if a.lower() == s.lower():
        return True
    else:
        return False
        
