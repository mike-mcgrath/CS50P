# CS50’s Introduction to Programming with Python.
# Problem Set 0 - Indoor Voice.

def main() :

    while True :
    
        try :    
            # Get text string.
            s = input( 'Input: ' ).strip()
        
            # Output echo input in lowercase.
            print( s.lower() )
            
        except EOFError:
            exit( 'Done' )
		
if __name__ == '__main__' :
    main()