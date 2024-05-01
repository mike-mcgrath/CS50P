# CS50’s Introduction to Programming with Python.
# Problem Set 0 - Making Faces.

def main() :

    while True :
    
        try :
            # Get text emoticon string.
            s = input( 'Input: ' ).strip()
            
            # Output graphic emoji string.
            print( convert( s ) )
            
        except EOFError :
            exit( 'Done' )

def convert( s ) :

    # Swap smile.
    if ':)' in s :
        s = s.replace( ':)', '🙂' )
    
    # Swap frown.
    if ':(' in s :
        s = s.replace( ':(', '🙁' ) 
    
    return s
		
if __name__ == '__main__' :
    main()