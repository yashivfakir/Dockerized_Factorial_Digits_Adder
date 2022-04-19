"""###############################################################################################################################
                                                CORIGINE FACTORIAL CHALLENGE
                                    (Summation of Factorial Output Digits in Python3)

                                                    UN-THREADED EXECUTION

                                                Created by: Yashiv Fakir
                                                Created on: 11/04/2022
                                                        Version: 3
###############################################################################################################################"""

import numpy as np
import argparse
import time



# Maximum number of digits allowed for the factorial output
MAX_Number_Of_Factorial_Output_Digits = 50000
# Create zeros array of max output length
parsed_Factorial_Array = [0] * MAX_Number_Of_Factorial_Output_Digits




def factorial_Multiplier(i, actual_Array_Size, parsed_Factorial_Array):
    ### Column multiplier ###
    # Instead of moving from right to left as
    # was taught in school for multiplication, the 
    # algorithm moves from left to right as the
    # counter begins at 2 and increases from units 
    # to tens, to hundredths etc. Therefore the 
    # factorial output sequence would be in reverse

    # For example:
        # 1234 x 10
        # where current array size is 4 (as starts at 1 not 0)
        # and carry initially set as 0
            # 4321
            # x 10
            #--------------------------------------------------
            # i = 0: product = 10 * 4 + 0 = 40,  0 add to array
            #                                    4 set as carry
            #--------------------------------------------------
            # i = 1: product = 10 * 3 + 4 = 34,  4 add to array
            #                                    3 set as carry
            #--------------------------------------------------
            # i = 2: product = 10 * 2 + 3 = 23   3 add to array
            #                                    2 set as carry
            #--------------------------------------------------
            # i = 3: product = 10 * 1 + 2 = 12   2 add to array
            #                                    1 set as carry
            #--------------------------------------------------
            # (LAST multiplication operation)
            # i = 4: product = 10 * 0 + 1 = 01    1 add to array   
            # Carry is now zero so end algorithm

            # Therefore: 1234 * 10 = 04321 when reversed = 12340 
                         
    # Define carry variable
    multiplication_carry = 0 

    j = 0

    # Perform column multiplication and add the carry up until one 
    # before the last multiplication operation.

    while j < actual_Array_Size:
        # Perform multiplication operation
        product = np.multiply(parsed_Factorial_Array[j], i)
        product = np.add(product, multiplication_carry) 
        # Add the unit digit to the array
        parsed_Factorial_Array[j] = np.mod(product, 10) 
        # Carry the remainder                  
        multiplication_carry  = np.floor_divide(product, 10) 
        # Move to the next digit/column in the array
        j = np.add(j, 1)
        
    # Once at the last operation, perform the last multipication 
    # operation using the carry method and increment the array size
    # to account for any changes in size to the parsed array. 

    while (multiplication_carry):
                parsed_Factorial_Array[actual_Array_Size] = np.mod(multiplication_carry, 10)
             
                multiplication_carry  = np.floor_divide(multiplication_carry, 10)
                actual_Array_Size = np.add(actual_Array_Size, 1)  

    # return the new array size        
    return actual_Array_Size




def factorial(input):
    ### Determine the factorial and parse into the zeros array ###
 
    try:
        # Set factorial in position [0] to 1, to account for 1! and 0! == 1
        parsed_Factorial_Array[0] = 1
        
        actual_Array_Size = 1 # actual_Array_Size counts the number of amended elements in the array that changed from zero to the amended number
    
        # If input is greater than 1 then determine factorial
        # i! = 2 * ... * (i-2) * (i-1) * i
        i = 2

        while i <= input:
            actual_Array_Size = factorial_Multiplier(i, actual_Array_Size,parsed_Factorial_Array)
            # Increment the factorial multiplier
            i = np.add(i, 1)         
       
        
    except IndexError:
        print("Factorial output magnitude exceeds the allowed maximum number of digits")
        exit()
    return actual_Array_Size



def factorial_Sum(actual_Array_Size):
    ### SUM the factorial digits ###

    # Define counter for elements in the array that were amended during the factorial calculation
    array_Counter = np.subtract(actual_Array_Size, 1)
    factorial_Sum = 0

    while array_Counter  >= 0:
        factorial_Sum = np.add(factorial_Sum,parsed_Factorial_Array[array_Counter ])
        array_Counter  = np.subtract(array_Counter ,1)

    # Output the factorial sum to the console   
    print(">>")
    print(factorial_Sum)    




def check_Input(input):
    ### Validates factorial input ###

    if (input >= 0):
        # If input is a positive integer
        return input

    elif(input < 0):
        # If input is a negetive integer, return absolute value
        return np.multiply(input, -1)

    else:
        # If input is not a integer value
        print("Input is not an INTEGER value")
        exit()

def main():
    ### Main Function ###
    
    start = time.perf_counter()

    # Define input interface between Docker run argument and the python script using the 'argpase' library     
    parser = argparse.ArgumentParser()
    parser.add_argument('input_Number', type=int)
    args = parser.parse_args()
    
    # Validate input
    args.input_Number = check_Input(args.input_Number)

    # Perform factorial
    factorial_Sum(factorial(args.input_Number))

    # Uncomment to display time
    finish = time.perf_counter()
    print("Execution Time: "+ str(finish - start))
 

if __name__ == "__main__":
    main()