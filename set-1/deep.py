# CS50’s Introduction to Programming with Python.
# Problem Set 1 - Deep Thought.

def main() :

    while True :

        try :
        
            # Get user's answer in lowercase.
            s = input( 'What is the Answer to the Great Question of Life, the Universe, and Everything? ' ).strip().lower()
        
            # Output appropriate response.
            if s == '42' or s == 'forty-two' or s == 'forty two' : 
                print( 'Yes' )
            else :
                print( 'No' )

        except EOFError:
            exit( 'Done' )
		
if __name__ == '__main__' :
    main()