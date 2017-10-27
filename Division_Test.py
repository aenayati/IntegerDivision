'''
Testing Division.divide() 
@author: Arash Enayati
Version: 0.03
Last Update on: May 29, 2013
'''
if __name__ == "__main__":
    from LuvocracyDivision import divide
    import sys, random
            
    # Division by 0 testing
    zeroDivisionCases = [[1,0],[-1,0],[sys.maxsize,0],[-12000,0],[999999999,0],[-sys.maxsize-1,0]]
    for case in zeroDivisionCases:
        try:
            numerator, denominator = case[0], case[1] 
            quotient, remainder = divide(numerator,denominator)
            print('Failed division by 0 test.')
            sys.exit()
        except ZeroDivisionError: # Checking correctness
            pass
    print('1. Division by 0 test Passed.') 
    
    # Edge cases testing    
    edgeCases = [[0,1],[0,-10000000],[0,10000000],[10000000,1],[1,10000000],[10000000,-1],[-1,100000000],[1,1]] 
    edgeCases += [[sys.maxsize,sys.maxsize],[sys.maxsize,-sys.maxsize-1],[-sys.maxsize-1,sys.maxsize],[-sys.maxsize,-sys.maxsize-1]]
    for case in edgeCases:
        try:
            numerator, denominator = case[0], case[1] 
            quotient, remainder = divide(numerator,denominator)
            if (quotient != numerator//denominator) or (remainder != numerator%denominator): # Checking correctness
                raise Exception(numerator, denominator)
        except Exception as excp:
            print('Error: Wrong results for input:', excp.args)
            sys.exit()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            sys.exit()
    print('2. Edge cases test Passed.')  
    
    # Random inputs testing from range [-sys.maxsize, sys.maxsize]
    try:
        for numerator in range(10000):
            numerator, denominator = random.randint(-sys.maxsize-1, sys.maxsize), random.randint(-sys.maxsize-1, sys.maxsize) # Randomly assigning input values
            quotient, remainder = divide(numerator,denominator)
            if (quotient != (numerator // denominator)) or (remainder != (numerator % denominator)): # Checking correctness
                raise Exception(numerator, denominator)            
    except Exception as excp:
        print('Error: Wrong results for input:', excp.args)
        sys.exit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit()
    print('3. Random input test passed.')      
    
    # Brute force testing - Tests all combination of inputs in range[-300, 300]
    try:
        for numerator in range(-300,300):
            for denominator in range(-300,300):
                if denominator != 0:
                    quotient, remainder = divide(numerator,denominator)
                    if (quotient != numerator//denominator) or (remainder != numerator%denominator): # Checking correctness
                        raise Exception(numerator, denominator)
    except Exception as excp:
        print('Error: Wrong results for input:', excp.args)
        sys.exit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit()        
    print('4. Brute force test passed.')
    
    print('------------------------------\nAll Tests Passed.')