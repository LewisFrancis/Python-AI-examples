# CMT309 Coursework 1
# Lewis Francis C1826277
# *******************************************************************

def do_arithmetic(x,y,z):
    '''
    Parameters
    ----------
    x,y : Integer/Float
        A number which is used to do the calculation.
    z : String
        A string which is used to find what operation is required.

    Returns
    -------
    Returns the result of applying the operation z to the numbers x and y.
        
    '''
    # After using time() I found that the fastest way to find an unkown operator was to use "or" multiple times instead of just using a list
    normalizedZ = z.lower()
    # Normalising z so that all of the string is the same in terms of capitalisation
    # if statements to find what z is and conduct the required calculation
    if z == "+" or normalizedZ == "add" or z == "":
        return float(x + y)
    if z == "-" or normalizedZ == "subtract":
        return float(x - y)
    if z == "*" or normalizedZ == "multiply":
        return float(x * y)
    if z == "/" and y>=1 or normalizedZ == "divide" and y>=1:
        return x / y
    if z == "/" or normalizedZ == "divide" and y == 0:
        print("Division by 0!")
        return None
    if z != "/" or normalizedZ != "divide" or z != "+" or normalizedZ != "add" or z != "-" or normalizedZ != "subtract" or z != "*" or normalizedZ != "multiply" or z != "" :
        print("Unkown Operation")
        return None

  
def sum_of_digits(s):
    '''
    Parameters
    ----------
    s : String
        A string that contains numbers and letters which are then used to calculate the sum of digits of all the digits which aren't numbers.

    Returns
    -------
    Returns an integer and a string which shows the performed calculation and which letters were missed.
        
    '''

    import re
    # Set up lists to be used later in code to seperate letters and numbers into
    numList = []
    letList = []
    # Search through s to find digit x and chech if it is a number or not
    for x in s:
        if x.isdigit() == True:
            intX = int(x)
            numList.append(intX)
        if x.isdigit() == False:
            letList.append(x)
    # lists will output a boolean result depending if they have anything in them
    if numList:
        strList = '+'.join(str(e) for e in numList)
        print("The sum of digits operation performs:", strList)
    if not numList:
        print("The sum of digits operation could not detect a digit!")
        print("The extracted non digets are:",letList) 
        return 0
    if not s:
        print("Empty string entered")
        return 0
    if s:
        print("The extracted non digets are:",letList)        
    print("output:",sum(numList))
