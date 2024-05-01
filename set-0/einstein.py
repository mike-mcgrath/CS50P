# CS50’s Introduction to Programming with Python.
# Problem Set 0 - Einstein.

def main() :

    try :
        # Get numeric user value for mass.
        m = int( input( 'm: ' ).strip() )
        
        # Ouput the equivalent number of Joules.
        print( m * pow( 300000000, 2 ) )
        
    except ValueError:
        exit( 'Entry for mass must be an integer' )
	
if __name__ == '__main__' :
    main()
