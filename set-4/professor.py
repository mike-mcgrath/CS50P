# CS50’s Introduction to Programming with Python.
# Problem Set 4 - Little Professor.

import random

def main() :

    # Get digits level.
    level = get_level()
    
    # Count number of correct answers.
    score = 0
    
    # Output ten problems.
    for i in range( 10 ) :
    
        # Get problem components.
        x, y, sum = generate_integer( level )
        
        # Allow three attempts to answer correctly.
        attempts = 0
        while attempts < 3 :
        
            try : 
                # Output problem.            
                print( f'{x} + {y} = ', end = '' )
                
                # Get user's answer.
                answer = int( input().strip() )
                
                # If correct, increment score and move to next problem.
                if answer == sum : 
                    score += 1
                    break
                else :
                    # If incorrect, allow a further attempt.
                    attempts += 1
                
                if attempts < 3 :
                    # Output error message if less than three attempts.
                    raise ValueError
                else :
                    # Or output correct answer after three attempts.
                    print( f'Answer: {x} + {y} = {sum}' )
                    
            except ValueError :
                print( 'EEE' )
            except EOFError :
                exit( 'Done' )
        
    # Output number of correct answers.
    print( 'Score: ', score )
    
# Get digits level.  
def get_level() :

    while True :
        try :
            level = int( input( 'Level: ' ).strip() )
            if level in [1,2,3] :
                return level
            else :
                raise ValueError	    
        except ValueError :
            print( 'Level must be 1, 2, or 3' )
        except EOFError :
            exit( 'Done' )

# Generate problem components.
def generate_integer( level ) :
    
    match level :
        case 1: 
            x, y = random.sample( range(1,9), 2 )
        case 2: 
            x, y = random.sample( range(10,99), 2 )
        case 3: 
            x, y = random.sample( range(100,999), 2 )
            
    sum = x + y
    return x, y, sum
       
        
if __name__ == '__main__' :
    main()