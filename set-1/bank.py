# CS50’s Introduction to Programming with Python.
# Problem Set 1 - Home Federal Savings Bank.

def main() :

    while True :

        try :
            # Get text string in lowercase.
            s = input( 'Greeting: ' ).strip().lower()
        
            # Reduce string to first five characters.
            s = s[0:5]
        
            # Output reward due, if any.
            if s == 'hello' :
                print( '$0' )
            elif s[0] == 'h' :
                print( '$20' )
            else :
                print( '$100' )

        except EOFError:
            exit( 'Done' )
		
if __name__ == '__main__' :
    main()