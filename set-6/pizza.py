# CS50’s Introduction to Programming with Python.
# Problem Set 6 - Pizza Py.

import sys, csv
from tabulate import tabulate

def main() :

    try :
        # Ensure there is one argument specifying a CSV file.
        if len( sys.argv ) < 2 :
            raise TypeError( 'Too few command-line arguments' )
        elif len( sys.argv ) > 2 :
            raise TypeError( 'Too many command-line arguments' )
        elif sys.argv[1][-4:].lower() != '.csv' :
            raise TypeError( 'Not a CSV file' )
        else : file = sys.argv[1]
        
        # Attempt to read file.
        with open( file, 'r' ) as f :
            reader = csv.reader( f )
            table = tabulate( reader, headers='firstrow', tablefmt='grid' )
                    
        # Output number of code lines.
        print( table )
        
    except FileNotFoundError :
        exit( 'File does not exist' )    
    except TypeError as e :
        exit( e )

if __name__ == '__main__' :
    main()