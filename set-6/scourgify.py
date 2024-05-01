# CS50’s Introduction to Programming with Python.
# Problem Set 6 - Scourgify.

import sys, csv

def main() :

    try :
    
        # Ensure there are two arguments specifying CSV files.
        if len( sys.argv ) < 3 :
            raise TypeError( 'Too few command-line arguments' )
        elif len( sys.argv ) > 3 :
            raise TypeError( 'Too many command-line arguments' )
        elif sys.argv[1][-4:].lower() != '.csv' or sys.argv[2][-4:].lower() != '.csv' :
            raise TypeError( 'Not a CSV file' )
        else : before = sys.argv[1] ; after = sys.argv[2]
        
        # Attempt to read file.
        with open( before, 'r' ) as bf :
            reader = csv.DictReader( bf )
            
            # Attempt to write file.
            with open( after, 'w' ) as af :
                
                # Write column headers.
                header = ['first', 'last', 'house']
                writer = csv.DictWriter( af, fieldnames=header )
                writer.writeheader()
                
                # Write data.
                for student in reader:
                    lname, fname = student['name'].split(',')
                    house = student['house']
                    writer.writerow( { 'first': fname, 'last': lname, 'house': house } )
        
    except FileNotFoundError :
        sys.exit( f'Could not read {before}' )    
    except TypeError as e :
        sys.exit( e )

if __name__ == '__main__' :
    main()