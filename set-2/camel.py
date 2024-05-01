# CS50’s Introduction to Programming with Python.
# Problem Set 2 - camelCase.

def main() :

    while True :
    
        try :
            # Get text string in camelCase.
            s = input( 'camelCase: ' ).strip()
            
            # Replace uppercase character with underscore and lowercase.
            for i in s :
                if i.isupper() :
                    s = s.replace( i, '_' + i.lower() )

            # Output snake case equivalent.
            print( s )

        except EOFError:
            exit( 'Done' )
        
if __name__ == '__main__' :
    main()