'''
Implementing Integer Division Without Using Division Operator
@author: Arash Enayati
Version: 0.03
Last Update on: June 01, 2013
'''
def divide(numerator, denominator):    
    """
        Function:  divide 
        --------------------
        Implement integer division without using the division operator.
        It finds the quotient by doing a binary search in the possible range for the quotient. 
        
        numerator:   numerator of the division
        denominator: denominator of the division        
 
        returns: quotient and remainder of the division
            raises error in case denominator is 0 
    """ 
    if (denominator == 0):
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    denominator_sign = (int)(denominator/abs(denominator))  # For convenience we convert negative denominators to positive denominators based on the following equations: 
    denominator = denominator * denominator_sign            # numerator = (denominator * quotient) + remainder -> (-1)*numerator = (-1)*denominator * quotient + (-1)*remainder
    numerator = numerator * denominator_sign                # We adjust the remainder accordingly before returning the result
    
    low, high = -abs(numerator), abs(numerator) # [Low,high] is the initial possible range for the quotient 
    while low <= high: # Iteratively binary searching for Quotient in range [low,high]
        mid = (low + high) >> 1 # mid = (low + high) / 2
        if (mid * denominator <= numerator) and ((mid + 1) * denominator > numerator):  # As denominator is positive we look for quotient with properties:
                                                                                        # quotient * denominator <= numerator and 
                                                                                        # (quotient + 1) * denominator  > numerator
            quotient = mid
            remainder = (numerator - (denominator * mid)) * denominator_sign # Remainder is multiplied by (-1) if input denominator was negative 
            return quotient, remainder
        elif (mid * denominator) > numerator:   # Shrinking the possible range for quotient by half
            high = mid - 1
        else:
            low = mid + 1
    
                
if __name__ == "__main__":
    import sys
    print('To Exit The Program Please Put 0 For Both Numerator and Denominator.')
    while True:
        print('---------------------------')
        try:
            numerator = int(input('Numerator:   '))
            denominator = int(input('Denominator: ')) 
            if (numerator == 0) and (denominator == 0): # Checking for the terminating condition of the program
                print('---------------------------\nExit')
                break
            quotient, remainder = divide(numerator, denominator)
            print('Quotient:', quotient, ' Remainder:', remainder)
        except ValueError:
            print('Error: Inputs should be integers. Please try again:')
        except ZeroDivisionError:
            print('Error: Denominator cannot be 0. Please try again: ')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            