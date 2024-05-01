# CS50’s Introduction to Programming with Python.
# Problem Set 1 - Meal Time.

def main() :

    while True :

        try :
            # Get time in 24-hour format from the user.
            time = input( 'What time is it?: ' )
                
            # Calculate number of hours as decimal number.
            time = convert( time )
            
            # Output appropriate meal time, if any.
            if time >= 7 and time <= 8 :
                print( 'breakfast time' )
            elif time >= 12 and time <= 13 :
                print( 'lunch time' )
            elif time >= 18 and time <= 19 :
                print( 'dinner time' )
                
        except ValueError :
            print( 'Enter valid time in 24-hour format as #:## or ##:##' )
        except EOFError :
            exit( 'Done' )

def convert(time) :
        
    # Separate time components.
    h, m = time.split( ':' )
    h = float(h)
    m = float(m)
    
    # Ensure valid time values.
    if h < 0 or h > 23 :
        raise ValueError
    if m < 0 or m > 59 :
        raise ValueError
    
    # Calculate number of minutes as decimal fraction of an hour.
    m = m /60
    
    # Return hours as decimal number.
    time = h + m
    return time
		
if __name__ == '__main__' :
    main()