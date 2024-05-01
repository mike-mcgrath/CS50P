# CS50’s Introduction to Programming with Python.
# Problem Set 0 - Tip Calculator.

def main() :

    while True :

        try :
            # Get numeric cost of meal.
            dollars = dollars_to_float( input( 'How much was the meal? ' ).strip() )
            
            # Get numeric preferred tip percentage.
            percent = percent_to_float( input( 'What percentage would you like to tip? ' ) )
            
            # Calculate tip amount.
            tip = dollars * percent
            
            # Output formatted tip amount.
            print( f'Leave ${tip:.2f}' )
            
        except ValueError :
            print( 'Entry must be a number' )
        except EOFError:
            exit( 'Done' )

def dollars_to_float( d ) :

    # Remove leading dollar symbol.
    d = d.replace( '$', '' )
    
    # Convert string number to float.
    d = float( d )
    return d

def percent_to_float( p ) :

    # Remove trailing percent symbol.
    p = p.replace( '%', '' )
       
    # Convert string number to float percentage.
    p = float(p)
    return p/100
		
if __name__ == '__main__' :
    main()

