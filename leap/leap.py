def is_leap_year(year):
    try:
        
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True        
        else:
            return False
    except TypeError as e:
        raise Exception('Please enter a valid year')


