def verify(isbn):
    
    isbn = isbn.replace('-','')
    if len(isbn) < 10:
        #raise ValueError("The number of digits in ISBN is incorrect")
        return False
    
    multiplier = 10
    isbn_total = 0
    try:
        for count,digit in enumerate(isbn):
            
            if count == 9:
                if digit == 'X':
                    isbn_total += 10 * multiplier                    
                elif digit.isdigit():
                    isbn_total += int(digit) * multiplier
                else:
                    #raise ValueError("There should only be 'X' or digit in last character of isbn")
                    return False
            elif digit.isdigit():
                isbn_total += int(digit) * multiplier
            else:
                #raise ValueError("There should only be numbers in first 9 digits of isbn")
                return False
            multiplier -= 1
              
    except ValueError:
        return False    
    return (isbn_total%11) == 0        

