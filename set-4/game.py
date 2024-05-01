# CS50’s Introduction to Programming with Python.
# Problem Set 4 - Guessing Game.

import random

def main() :

    while True :
    
        try :
            # Get preferred maximum number.
            n = int( input( 'Level: ' ) )
            if n < 0 : 
                raise ValueError
            elif n > 0 : 
                break
                
        except ValueError :
            print( 'Level must be a positive integer' )
        except EOFError :
            exit( 'Done' ) 

    # Generate a number between one and the preferred maximum.
    num = random.randint( 1, n )
        
    while True :
    
        try : 
            # Get user's numeric attempt.        
            guess = int( input( 'Guess: ' ) )
            
            # Ensure attempt is within range.
            if guess < 1 or guess > n :
                raise ValueError
                
            # Output appropriate response.
            if guess < num :
                print( 'Too small!' )
            elif guess > num :
                print( 'Too large!' )
            elif guess == num :
                print( 'Just right!' )
                break
                
        except ValueError :
            print( f'Guess must be between 1 and {n}' )       
        
if __name__ == '__main__' :
    main()