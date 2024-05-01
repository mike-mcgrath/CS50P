# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Working 9 to 5.
# Solution without Regular Expression pattern matching.

def main() :

    print( convert( input( 'Hours: ' ).strip() ) )
	
def convert( s ) :

    try :
        # Separate string into five components.
        s = s.split( ' ' )
        if len( s ) != 5 :
            raise ValueError
            
        # Separate values in ##:## format.
        elif ':' in s[0] :
            h1 = int( s[0].split( ':' )[0] )
            h2 = int( s[3].split( ':' )[0] )
            m1 = s[0].split( ':' )[1]
            m2 = s[3].split( ':' )[1]
            
        # Separate components in # format.
        else :
            h1 = int( s[0] )
            h2 = int( s[3] )
            m1 = '00'
            m2 = '00'
        
        # Ensure hour value is in valid range.        
        if h1 > 12 or h2 > 12 :
            raise ValueError  

        # Ensure minute value is in valid range.            
        if int( m1 ) > 59 or int( m2 ) > 59 :
            raise ValueError
            
        # Ensure junction word is valid.
        if s[2].lower() != 'to' :
            raise ValueError
            
    except ValueError :
        exit( 'Invalid input' )
    
    # Change PM hours to 24-hour...
    if s[1].upper() == 'PM' : h1 = h1 + 12
    if h1 == 24 : h1 = 0
    if s[4].upper() == 'PM' : h2 = h2 + 12   
    if h2 == 24 : h = 0 

    # Change ints back to strings.
    h1 = str( h1 )
    h2 = str( h2 )
    
    # Add leading zeros, if any.
    if int(h1) < 10 : h1 = '0' + h1
    if int(h2) < 10 : h2 = '0' + h2

    return f'{h1}:{m1} {s[2]} {h2}:{m2}'
    # To fail test, change above to...
    # return f'{h1}:{m1} {s[2]} {h2}:'
    
if __name__ == '__main__' :
    main()