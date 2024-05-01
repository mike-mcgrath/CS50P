# CS50’s Introduction to Programming with Python.
# Problem Set 6 - Lines of Code.

import sys

def main() :

    try : 
        # Ensure there is one argument specifying a Python file.
        if len( sys.argv ) < 2 :
            raise TypeError( 'Too few command-line arguments' )
        elif len( sys.argv ) > 2 :
            raise TypeError( 'Too many command-line arguments' )
        elif sys.argv[1][-3:] != '.py' :
            raise TypeError( 'Not a Python file' )
        else : file = sys.argv[1]

        # Line count.
        count = 0
        
        # Attempt to read file.
        with open( file, 'r' ) as f :
            for line in f :
                # Exclude comment lines and empty lines.
                if not ( line.lstrip().startswith('#') or line.strip() == '' ) :
                    count += 1
                    
        # Output number of code lines.
        print( count, 'lines in', file )
        
    except FileNotFoundError :
        exit( 'File does not exist' )    
    except TypeError as e :
        exit( e )

if __name__ == '__main__' :
    main()