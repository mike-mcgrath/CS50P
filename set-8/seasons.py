# CS50’s Introduction to Programming with Python.
# Problem Set 8 - Seasons of Love.

import sys
from datetime import datetime, timedelta
import inflect

inflector = inflect.engine()

def main():

   # Get user text string in YYYY-MM-DD format.
    dob = input( 'Date of Birth: ' ).strip()
    
    try :
        # Ensure string is correct format.
        if not datetime.fromisoformat( dob ) :
            sys.exit()
        else :
            # Or output elapsed minutes.
            print( parse( dob), 'minutes' )
            
    except ValueError :
        pass    
        
def parse( dob ) :

        # Get date of birth.
        dob = datetime.fromisoformat( dob ) 
        # To fail test change above to...
        # dob = str(datetime.fromisoformat( dob ))
        
            
        # Get yesterday's date.
        d = datetime.today() - timedelta( days=1 )
            
        # Set yesterday's time to midnight.
        d = d.replace( hour=0, minute=0, second=0, microsecond=0 )
            
        # Get elapsed number of days.
        days = d - dob
            
        # Convert number of days to minutes
        mins = int( days.total_seconds() / 60 )
      
        # Convert numeric minutes to string.
        mins = inflector.number_to_words( mins )
            
        # Output elapsed minutes string.
        return mins

if __name__ == '__main__' :
    main()