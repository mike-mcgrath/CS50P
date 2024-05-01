# CS50’s Introduction to Programming with Python.
# Problem Set 5 - Fuel Gauge revision.

def main() :

    while True :

        try :
            # Get fraction value as text string.
            s = input( 'Fraction: ' ).strip()
            
            s = convert( s )
        
            s = gauge( s )
            
            print( s )

        except ValueError :
            print( 'Invalid Fraction!' )
        except ZeroDivisionError :
            print( 'Cannot Divide By Zero!' )
        except EOFError :
            exit( 'Done' )
            
def convert(s) :

            # Separate fraction components.
            x, y = s.split( '/' )
        
            # Convert components to numeric values.
            x = int( x )
            y = int( y )
            
            # Calculate fraction as a percentage.
            s = round( x/y * 100 )
            
            # Ensure percentage is acceptable.
            if s > 100 or s < 0 :
                raise ValueError
                
            return s

def gauge( s ) :
                
            # Output if almost empty.
            if s <= 1 :
                return 'E'
                
            # Output if almost full.
            elif s >= 99 and s <= 100:
                return 'F'
                
            # Output median percentage.
            else :
                return str(s)+'%'
            # To fail test, change above to return str(s) .
        
if __name__ == '__main__' :
    main() 