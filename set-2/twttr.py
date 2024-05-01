# CS50’s Introduction to Programming with Python.
# Problem Set 2 - Setting Up My Twitter.

def main() :

    while True :

        try :    
            # Get text string.
            s = input('Input: ').strip()

            # Remove vowels from string.
            for i in s :
                if i.upper() in ['A','E','I','O','U'] :
                    s = s.replace( i, '' )
                    
            # Output modified string.
            print( s )

        except EOFError :
            exit( 'Done' )
        
if __name__ == '__main__' :
    main()          