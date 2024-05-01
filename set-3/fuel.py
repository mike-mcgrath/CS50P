# CS50’s Introduction to Programming with Python.
# Problem Set 3 - Fuel Gauge.

def main() :

    while True :

        try :
            # Get fraction value as text string.
            s = input( 'Fraction: ' ).strip()
        
            # Separate fraction components.
            x,y = s.split( '/' )
        
            # Convert components to integer values.
            x = int( x )
            y = int( y )
            
            # Calculate fraction as a percentage.
            s = round( x/y * 100 )
            
            # Ensure percentage is acceptable.
            if s > 100 or s < 0 :
                raise ValueError
                
            # Output if almost empty.
            elif s <= 1 :
                print( 'E' )
                
            # Output if almost full.
            elif s >= 99 and s <= 100:
                print( 'F' )
                
            # Output median percentage.
            else :
                print( str( s )+'%' )

        except ValueError :
            print( 'Invalid Fraction!' )
        except ZeroDivisionError :
            print( 'Cannot Divide By Zero!' )
        except EOFError :
            exit( 'Done' )
        
if __name__ == '__main__' :
    main() 