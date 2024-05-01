# CS50’s Introduction to Programming with Python.
# Problem Set 2 - Nutrition Facts.

def main() :

    while True :

        try :   
            # Get fruit name in lowercase.
            s = input( 'Item: ' ).strip().lower()
        
            # Store calorie value.
            cals = 0
        
            match s :
                case 'apple' : cals = 130
                case 'avocado' : cals = 50
                case 'banana' : cals = 110
                case 'cantaloupe' : cals = 50
                case 'grapefruit' : cals = 60
                case 'grapes' : cals = 90
                case 'honeydew melon' : cals = 50
                case 'kiwifruit' : cals = 90
                case 'lemon' : cals = 15
                case 'lime' : cals = 20
                case 'nectarine' : cals = 60
                case 'orange' : cals = 80
                case 'peach' : cals = 60
                case 'pear' : cals = 100
                case 'pineapple' : cals = 50
                case 'plums' : cals = 70
                case 'strawberries' : cals = 50
                case 'sweet cherries' : cals = 100
                case 'tangerine' : cals = 50
                case 'watermelon' : cals = 80   
            
            # Output appropriate number of calories.
            if cals != 0 : print( 'Calories: ', cals )

        except EOFError:
            exit( 'Done' )
        
if __name__ == '__main__' :
    main() 