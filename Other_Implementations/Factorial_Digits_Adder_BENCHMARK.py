"""###############################################################################################################################
                                                    CORIGINE FACTORIAL CHALLENGE
                                            (Summation of Factorial Digits in Python3)

                                                            BENCHMARK

                                                    Created by: Yashiv Fakir
                                                    Created on: 09/04/2022
                                                            Version: 1
###############################################################################################################################"""

# Import libraries
import numpy as np 
import argparse
from fractions import Fraction
import time

start = time.perf_counter()

# TEST
def factorial_Finder(input):
    factorial = 1
    while(input != 0):
        factorial = np.multiply(factorial,input)
        input = np.subtract(input,1)
    
    return factorial


# Input validation method that checks the conditions for a factorial operation
def check_Input(input):
    if (input >= 0):
        # If input is a positive
        return True

    elif(input < 0):
        # If input is a negetive
        return False

    else:
        # If input is not a number
        print("Input is not an INTEGER value")
        exit()

        
def factorial_Adder(factorial):
    factorial_Sum = 0

    # Sum the digits of the factorial number
    while(factorial):
        mod = np.mod(factorial,10)
        factorial_Sum = np.add(factorial_Sum, mod)
        factorial = np.floor_divide(Fraction(factorial), 10)
        
    return int(factorial_Sum)


def main():
    start = time.perf_counter()
    print(">>") 

    # Define input interface between Docker run argument and the python script using the 'argpase' library     
    parser = argparse.ArgumentParser()
    parser.add_argument('input_Number', type=int)
    args = parser.parse_args()


    if (check_Input(args.input_Number)):
        # Determine factorial and summation of the postitve input number
        factorial = np.math.factorial(args.input_Number)
        print(factorial_Adder(factorial))

    else:
        # Take the absolute value of the negative input
        args.input_Number = np.multiply(-1,args.input_Number)
        # Determine the factorial and summation
        factorial = np.math.factorial(args.input_Number) 
        
        print(np.multiply(factorial_Adder(factorial),-1))

    # Uncomment to display time  
    finish = time.perf_counter()
    print("Execution Time: "+ str(finish - start))



if __name__ == "__main__":
    main()