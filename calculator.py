## imports
import math
from test_calculator import Calculator

calculator = Calculator()

## obtain input form user
print 'type "q" to quit this program'

while True:
    strinput1 = raw_input('Please enter 1st value: ')
    if strinput1 == 'q':
        quit()
    ## parse string input to float
    try:
        xvar = float(strinput1)
        break
    except:
        print 'Invalid input.  Please try agsin.'

## obtain operation
while True:
    print 'Please select operation you wish to perform:'
    print 'Type "A" for addition'
    print 'Type "S" for subtraction'
    print 'Type "M" for multiplication'
    print 'Type "D" for division'
    print 'Type "E" for exponent'
    print 'Type "R" for square root'
    print 'Type "F" for factorial'
    print 'Type "C" for nCr'
    print 'Type "P" for nPr'
    print 'Type "L" for log(base 10)'
    operation = raw_input('Enter you choice now: ')
    if operation == 'q':
        quit()
    operation = operation.lower()
    operations = ['a', 's', 'm', 'd', 'e', 'r', 'f', 'c', 'p', 'l']
    if operation in operations:
    
        ## sub-divide into 1-variable or 2-variable operation
        operations1var = ['r', 'f', 'l']
        operations2var = ['a', 's', 'm', 'd', 'e', 'c', 'p']
    
        if operation in operations1var:
            break
    
        if operation in operations2var:
            while True:
                strinput2 = raw_input('Please enter 2nd value: ')
                if strinput2 == 'q':
                    quit()
                # parse string input to float
                try:
                    yvar = float(strinput2)
                    break
                except:
                    print 'Invalid input.  Please try again.'
                    continue
        break
        
    if operation not in operations:
        print 'Invalid operation.  Please try agsin.'
        continue

## compute conversion
if operation == "r":
    answer = calculator.squareRoot(xvar)
elif operation == "f":
    if xvar%1 == 0:
        xvar = int(xvar)
        answer = calculator.factorial(xvar)
    else:
        answer = "NaN"
elif operation == "l":
    answer = calculator.log(xvar)
elif operation == "a":
    answer = calculator.add(xvar, yvar)
elif operation == "s":
    answer = calculator.subtract(xvar, yvar)
elif operation == "m":
    answer = calculator.multiply(xvar, yvar)
elif operation == "d":
    answer = calculator.divide(xvar, yvar)
elif operation == "e":
    answer = calculator.exponent(xvar, yvar)
elif operation == "c":
    if (xvar%1 == 0) and (yvar%1 == 0):
        xvar = int(xvar)
        yvar = int(yvar)
        answer = answer = calculator.ncr(xvar, yvar)
    else:
        answer = "NaN"
elif operation == "p":
    if (xvar%1 == 0) and (yvar%1 == 0):
        xvar = int(xvar)
        yvar = int(yvar)
        answer = answer = calculator.npr(xvar, yvar)
    else:
        answer = "NaN"
else:
    ## debug comment
    print "Murphy was an optimist! ..."

if isinstance(answer, float):
    print "Answer: %f" %answer
elif isinstance(answer, int):
    print "Answer: %d" %answer
elif isinstance(answer, str):
    print answer
else:
    ## debug comment
    print "Something went wrong Freddy!"

