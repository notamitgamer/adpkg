# this module had the function to calculate the area of triangle
# √[s(s-a)(s-b)(s-c)]

def areaoftriangle(len_a, len_b, len_c, unit = '') : 
    """
    Calculates the area of triangle using general formula.  √[s(s-a)(s-b)(s-c)]  

    Args: 
        len_a = A positive number as length of a side of a triangle (Not Zero)
        len_b = A positive number as length of a side of a triangle (Not Zero)
        len_c = A positive number as length of a side of a triangle (Not Zero)
        unit = Unit of the area of the triangle (e.g., "sq cm", "m^2").

    Returns:
        Area of the triangle
        None if the input is not valid or any error occurs.
    """
    # first checking if the input values are even valid or not.
    try : 
        a = float(len_a)
        b = float(len_b)
        c = float(len_c)
    except ValueError :
        print('Please enter a valid number (Integer or Float).')
        return None
    except Exception as error : 
        print(f'An unexpected error happened : {error}')
        return None
    
    # checking if inputs are above 0, because a side length can't be zero
    if a <= 0 or b <= 0 or c <= 0 :
        print('Side length of a triangle can\'t be Zero or negative.')
        return None
    
    # checking if the triangle even follows the triangle rule : len_a + len_b > len_c
    if not (a + b >= c and a + c >= b and b + c >= a) :
        print('The triangle must satisfy the triangle inequality theorem (the sum of the lengths of any two sides must be greater than or same as the length of the third side).')
        return None
    
    # main logic
    try :
        # calculating the value of 's' (The semi-perimeter (half the perimeter) of the triangle) 
        s = (a + b + c) / 2

        # now the formula without root
        pre_result = (s * (s - a) * (s - b) * (s - c))

        if pre_result < 0:
        # Due to floating point inaccuracies, it might be slightly negative
            if pre_result > -0.09 : # A small tolerance
                result = 0.0
            else:
                print("Error: Calculation resulted in a negative number under the square root, indicating invalid triangle sides (likely due to precision issues)."
                      f"\nCalculated value before root was : {pre_result}")
                return None

        else : 
            # now the root
            result = pre_result ** 0.5

    except Exception as error : 
        print(f'An unexpected error happened : {error}')
        return None

    # returning the result with the unit if provided   
    try : 
        if len(unit) > 0 :
            return f'{result:.3f} {unit}'
        else :
            result = round(result, 3)
            return float(result)
    except Exception as error : 
        print(f'An unexpected error happened : {error}')
        return None