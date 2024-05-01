# CS50’s Introduction to Programming with Python.
# Problem Set 5 - Home Federal Savings Bank revision.

def main() :

    while True :

        try :
            # Get text string in lowercase.
            s = input( 'Greeting: ' ).strip().lower()
        
            # Reduce string to first five characters.
            s = s[0:5]
        
            s = value( s )
            
            print( f'${s}' )

        except EOFError:
            exit( 'Done' ) 


def value(s) :

    # Return reward due, if any.
    if s == 'hello' : return 0
    elif s[0] == 'h' : return 20
    else : return 100
    
    # To fail test.
    # if s == 'hello' : return 100
    # elif s[0] == 'h' : return 20
    # else : return 0
	
if __name__ == '__main__' :
    main()