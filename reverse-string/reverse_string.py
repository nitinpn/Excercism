def reverse(input=''):
    try:
        return input[::-1]
    except TypeError as e:
        raise Exception ('Please enter a valid string: ' + e )
