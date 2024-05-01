# CS50’s Introduction to Programming with Python.
# Problem Set 5 - Setting Up My Twitter revision.

def main() :

    while True :

        try :  
            # Get text string.
            s = input( 'Input: ' ).strip()

            s = shorten( s )
                    
            # Output modified string.
            print( s )

        except EOFError :
            exit( 'Done' )

def shorten( s ) :

    # Remove vowels from string.
    for i in s :
        if i.upper() in ['A','E','I','O','U'] :
            s = s.replace( i, '' )
        
        # To fail test...
        # if i in ['A','E','I','O','U'] :
        #    s = s.replace( i, '' )
        
    return s

    
if __name__ == '__main__' :
    main()          