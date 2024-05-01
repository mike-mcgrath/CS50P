# CS50’s Introduction to Programming with Python.
# Problem Set 4 - Bitcoin Price Index.

import sys
import requests


def main() :

    try :
        # Ensure there is a command-line argument.
        if len( sys.argv ) < 2 :
            raise IndexError
            
        # Save command-line argument as a float.   
        num = float( sys.argv[1] )
        
        # Attempt data request.
        r = requests.get( 'https://api.coindesk.com/v1/bpi/currentprice.json' )
        
        # Read response into a dictionary.
        data = r.json()
        
        # Query dictionary for Bitcoin Price Index (bpi), USD, rate_float.
        rate = data['bpi']['USD']['rate_float']
        
        # Calculate cost of number of bitcoins required.
        cost = num * rate
        
        # Output formatted cost of number of bitcoins required.
        print( f'${cost:,.4f}' )      
   
    except IndexError :
        sys.exit( 'Missing command-line argument' )
    except ValueError :
        sys.exit( 'Command-line argument is not a number' )
    except requests.RequestException :
        sys.exit( 'Request did not succeed' )  
        
if __name__ == '__main__' :
    main() 