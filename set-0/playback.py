# CS50’s Introduction to Programming with Python.
# Problem Set 0 - Playback Speed.

def main() :

    while True :
    
        try :
            # Get text string.
            s = input( 'Input: ' ).strip()
        
            # Output echo replacing spaces with ellipses.
            print( s.replace( ' ', '...' ) )
        
        except EOFError:
            exit( 'Done' )
		
if __name__ == '__main__' :
    main()