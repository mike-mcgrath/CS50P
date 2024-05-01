# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Response Validation.
# Solution without Regular Expression pattern matching.

import validators


def main() :

    # Get user text string.
    s = input('What\'s your email address? ').strip()
    
    # Output result.
    print( is_valid( s ) )

def is_valid( s ) :

    # Examine text string for valid email address format.
    if validators.email( s ) :
        return 'Valid'
    else : 
        return 'Invalid'        

if __name__ == '__main__' :
    main()