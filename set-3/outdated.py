# CS50’s Introduction to Programming with Python.
# Problem Set 3 - Outdated.

def main() :

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    while True :

        try :  
            # Get date as text string.
            s = input( 'Date: ' ).strip()
        
            # For date in MM/DD/YYYY format.
            if '/' in s :
            
                # Separate date components.
                m, d, y = s.split( '/' )
                if len( y ) != 4 : raise ValueError
                m = int( m )
                if m > 12 : raise ValueError
                d = int( d )
                if d > 31 : raise ValueError
            
                # Output date in YYYY/MM/DD format.
                print( f'{y}-{m:02}'+f'-{d:02}' )

            # For date in MM-name//DD/YYYY format.       
            elif ',' in s :
                # Remove comma/s.
                s = s.replace( ',', '' )
                
                # Separate date components.
                m, d, y = s.split( ' ' )
                if len( y ) != 4 : raise ValueError
                if m not in months : raise ValueError            
                m = months.index( m ) + 1
                d = int( d )
                if d > 31 : raise ValueError
            
                # Output date in YYYY/MM/DD format.
                print( f'{y}-{m:02}'+f'-{d:02}' )
            
        except ValueError :
            print( 'Invalid Date!' )
        except EOFError :
            exit( 'Done' )
        
if __name__ == '__main__' :
    main() 