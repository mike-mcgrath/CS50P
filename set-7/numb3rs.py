# CS50’s Introduction to Programming with Python.
# Problem Set 7 - NUMB3RS.
# Solution without Regular Expression pattern matching.


def main() :

    # Get IP address input.
    print( validate( input( 'IPv4 Address: ' ).strip() ) )
 
def validate( adr ) :

    try :
        # Separate address components.
        adr = adr.split( '.' )
        if len( adr ) != 4 : return False
        
        # To fail test, uncomment this statement...
        # if len( adr ) != 3 : return False

        # Ensure each component is between 0-255.
        for num in adr :
            if int( num ) not in range( 0, 256 ) : return False
        return True
        
    except ValueError :
        return False
        
if __name__ == '__main__' :
    main()
