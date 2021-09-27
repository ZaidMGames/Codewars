# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false
def validate_pin(pin):
    if pin.isdigit():
        if len(pin) == 4 :
            return True
        elif len(pin) == 6:
            return True
        else:
            return False
    else:
        return False
   
   validate_pin("2233")