# Prime check function

def check_prime(inp) : 
    """
    Checks the input integers is a Prime number or not.

    Args: 
        inp = The non-negetive integer to check 

    Returns:
        1 if input integer is Prime, 0 if input integer is not Prime.
        None if the input is not valid or any error occurs.
    """
    #trying to check if the input is valid integer or not
    try : 
        temp = int(inp)
    except ValueError : 
        print('Error : Plese enter a valid integer.')
        return None
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    # handling negetive integers
    if temp < 0 : 
        print('Error : Please enter a non-negetive integer.')
        return None
    #handling integers <= 3
    if temp < 2 :
        return 0    # '0' means not prime.
    if temp <= 3 : 
        return 1    # '1' means prime.
    if temp % 2 == 0 :
        return 0    # there is no even number that is prime except '2', this was checked before.
    #main logic to check prime or not
    try : 
        for i in range (3, (temp // 2) + 1) :
            if temp % i == 0 :
                return 0
        return 1
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}') 
        return None
    
# factorial function

def factorial(inp) :
    """
    Calculates the factorial of given integer

    Args:
        inp = an non-negetive integer
    
    Returns:
        the factorial of the non-negetive integer.
        None if the input is not valid or any error occurs.
    """
    # trying to check if input is a valid integer or not
    try : 
        temp = int(inp)
    except ValueError : 
        print('Error : Plese enter a valid integer.')
        return None
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    # handling negetive integer 
    if temp < 0 :
        print('Error : Please enter a non-negetive integer.')
        return None
    # handling inp '0'
    if temp == 0 :
        return 1
    # main logic for factorial 
    try : 
        result = 1
        for i in range(2, temp + 1) :
            result = result * i
        return result
    except Exception as error :
        print(f'Error : An unexpected error happened : {error}')
        return None
    
# permutation function

def permutation(total_item,chosen_item) : 
    """
    Calculates the number of permutations p(n, k).

    Args:
        total_item = the total number of distinct items in the set
        chosen_item = the number of items to be arranged or chosen from the set at a time
    
    Returns:
        The number of permutations.
        None if the input is not valid or any error occurs.
    """
    # trying to check if the inputs are a valid integer or not.
    try : 
        n = int(total_item)
        k = int(chosen_item)
    except ValueError : 
        print('Error : Please enter a valid integer.')
        return None
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    # handling negetive integer
    if n < 0 or k < 0 :
        print('Error : Please enter non-negetive integer.')
        return None
    if k > n : 
        print('Error : Chosen item should be lower than Total item.')
        return None
    # main logic for permutation
    try : 
        fact_n = factorial(n)
        fact_n_k = factorial(n-k)
        result = fact_n / fact_n_k
        return int(result)
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    
# combination function

def combination(total_item, chosen_item) : 
    """
    Calculates the number of combination c(n, k).

    Args:
        total_item = the total number of distinct items in the set
        chosen_item = the number of items to be arranged or chosen from the set at a time
    
    Returns:
        The number of combinations.
        None if the input is not valid or any error occurs.
    """
    # trying to check if the inputs are a valid integer or not.
    try : 
        n = int(total_item)
        k = int(chosen_item)
    except ValueError : 
        print('Error : Please enter a valid integer.')
        return None
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    # handling negetive integer
    if n < 0 or k < 0 :
        print('Error : Please enter non-negetive integer.')
        return None
    if k > n : 
        return 0   # if total item is lower than chosen then their is no possible combinaition. 
    # main logic for combination
    try : 
        fact_n = factorial(n)
        fact_k = factorial(k)
        fact_n_k = factorial(n-k)
        result = fact_n / (fact_n_k * fact_k)
        return int(result)
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None

# reverse string function

def string_reverse(string) : 
    """
    Reverse the given string

    Args:
        string = The given string
    
    Returns:
        Reverse string of the given string
        None if the input is not valid or any error occurs.
    """
    # trying to check if the input is a string
    try : 
        temp = str(string)
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    # handing empty string
    if temp == '' :
        print('Error : Input should not be a empty string.')
        return None
    # main logic
    try : 
        result = ''
        for char in temp : 
            result = char + result
        return result
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None

# matrix checking function

def is_matrix_valid(matrix) :
    """
    Helper to validate if an input is a list of lists representing a matrix.

    Args:
        matrix = A matrix that will be checked.
    
    Returns:
        True if the matrix is valid. False if not.
    """
    try : 
        #checking if the list is empty or not / trying to check is the input matrix is empty or not
        row_count = 0
        for row in matrix : 
            row_count += 1
        
        if row_count == 0 :
            print('Error: Matrix must be a non-empty list of lists.')
            return False
        
        #trying to check if the list is 'list of lists', trying to check if the matrix have both row and column
        first_row = matrix[0]
        col_count_first_row = 0
        for val in first_row :
            col_count_first_row += 1

        if col_count_first_row == 0 :
            print('Error : Matrix should have non-empty lists as rows.')
            return False
        
        # checking if All rows in the matrix have the same number of columns
        for row_index in range(row_count) :
            current_row = matrix[row_index]
            
            current_col_count = 0
            for col in current_row : 
                current_col_count += 1

            if current_col_count != col_count_first_row : 
                print('All rows in the matrix must have the same number of columns')
                return False
            
            #checking if columns have a number by attempting a conversion
            for col_index in range(current_col_count) : 
                element = current_row[col_index]

                try : 
                    checker = float(element)
                except (ValueError, TypeError) :
                    print('Error : Matrix elements should be a number(Integer or Float number).')
                except Exception as error :
                    print(f'Error : An uncxpected error happened : {error}')
                    return False
        
        return True     # if all check passed 
    
    except Exception as error : 
        print(f'Error : An uncxpected error happened : {error}')
        return False

# matrix multiplication function

def matrix_addition(matrix1, matrix2) :
    """
    Add two input matrix

    Args:
        matrix1 = first matrix
        matrix2 = second matrix
    
    Returns:
        Matrix after adding two input matrix.
        None if the input is not valid or any error occurs.
    """
    # checking if the matrix are valid or not
    if not is_matrix_valid(matrix1) : 
        print('Error : First matrix is not valid.')
        return None
    if not is_matrix_valid(matrix2) : 
        print('Error : Second matrix is not valid.')
        return None

    # checking matrix dimension are same or not.
    row_count_mat1 = len(matrix1)
    col_count_mat1 = len(matrix1[0])

    row_count_mat2 = len(matrix2)
    col_count_mat2 = len(matrix2[0])

    if row_count_mat1 != row_count_mat2 or col_count_mat1 != col_count_mat2 :
        print('Error : Matrix dimension should be same for both matrix to do addition.')
        return None

    try : 
        result_matrix = []
        for i in range(row_count_mat1) : 
            result_matrix_row = []
            for j in range(col_count_mat1) : 
                result_matrix_element = matrix1[i][j] + matrix2[i][j]
                result_matrix_row.append(result_matrix_element)
            result_matrix.append(result_matrix_row)
            
        string_result_matrix = ''
        for row in result_matrix :
            for element in row :
                string_result_matrix = string_result_matrix + str(element) + ' '
            string_result_matrix = string_result_matrix + '\n'
        return string_result_matrix
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None

# matrix multiplication function

def matrix_multiplication(matrix1, matrix2) : 
    """
    Multiply one input matrix with another input matrix.

    Args:
        matrix1 = first matrix
        matrix2 = second matrix
    
    Returns:
        Matrix after multiplying
        None if the input is not valid or any error occurs.
    """
    # checking if the matrix are valid or not
    if not is_matrix_valid(matrix1) : 
        print('Error : First matrix is not valid.')
        return None
    if not is_matrix_valid(matrix2) : 
        print('Error : Second matrix is not valid.')
        return None
    
    # checking matrix dimension as the column_count of the first matrix and the row_count of the second matrix should be same
    row_count_mat1 = len(matrix1)
    col_count_mat1 = len(matrix1[0])

    row_count_mat2 = len(matrix2)
    col_count_mat2 = len(matrix2[0])

    if col_count_mat1 != row_count_mat2 : 
        print('Error : Column_count of the first matrix and the Row_count of the second matrix should be same to do multiplication.')
        return None
    
    try : 
        result_matrix = []
        for i in range(row_count_mat1) :    # taking the row of the matrix1
            result_matrix_row = []
            for j in range(col_count_mat2) :    # taking the column of the matrix2
                result_matrix_element = 0
                for k in range(col_count_mat1) :    # taking the column of the matrix1.
                    """ 
                    এখন, 'k' এর লুপ একবার সম্পন্ন হলে, 'i' এর জন্য matrix1 
                    এর সারি একই থাকবে, 'j' এর জন্য matrix2 এর কলাম একই থাকবে,
                    কিন্তু 'k' এর মান পরিবর্তনের সাহায্যে, matrix1 এর কলাম এবং matrix2
                    এর সারি পরিবর্তন করা যেতে পারে। 'j' পরিবর্তন হলে, matrix2 এর 
                    কলাম পরিবর্তন হবে। অর্থাৎ, কাজটি এই প্রবাহে হবে: প্রথমে, matrix1 
                    এর সারিটি নেবে এবং matrix2 এর কলাম পরিবর্তন করে এটিকে গুণ 
                    করবে। সমস্ত কলাম শেষ হয়ে গেলে, তারপর matrix1 এর পরবর্তী সারিতে যাবে।
                    """
                    result_matrix_element += matrix1[i][k] * matrix2[k][j]
                result_matrix_row.append(result_matrix_element)
            result_matrix.append(result_matrix_row)

        string_result_matrix = ''
        for row in result_matrix :
            for element in row :
                string_result_matrix = string_result_matrix + str(element) + ' '
            string_result_matrix = string_result_matrix + '\n'
        return string_result_matrix
    except Exception as error : 
        print(f'An unexpected error happened : {error}')
        return None
    
# matrix transpose function

def matrix_transpose(matrix) : 
    """
    Transpose a matrix(row becomes column, column becomes row)

    Args:
        matrix = Input matrix given by user
    
    Returns:
        Matrix after transposing
        None if the input is not valid or any error occurs.
    """
    # checking if the matrix are valid or not
    if not is_matrix_valid(matrix) : 
        print('Error : Given matrix is not valid.')
        return None
    
    row = len(matrix)
    column = len(matrix[0])

    try : 
        result_matrix = []
        for i in range(column) : 
            result_matrix_row = []
            for j in range(row) : 
                result_matrix_row.append(matrix[j][i])
            result_matrix.append(result_matrix_row)

        string_result_matrix = ''
        for row in result_matrix :
            for element in row :
                string_result_matrix = string_result_matrix + str(element) + ' '
            string_result_matrix = string_result_matrix + '\n'
        return string_result_matrix
    except Exception as error : 
        print(f'An unexpected error happened : {error}')
        return None

# determinant_value function

def determinant_value(matrix) : 
    """
    Calculates the determinant value of given matrix

    Args:
        matrix = Input matrix given by user
    
    Returns:
        Determinant value of given matrix
        None if the input is not valid or any error occurs.
    """
    # checking if the matrix are valid or not
    if not is_matrix_valid(matrix) : 
        print('Error : Given matrix is not valid.')
        return None
    
    row = len(matrix)
    column = len(matrix[0])

    if row != column :
        print('Error : Row count and the Column count should be same.')
        return None
    
    if row > 3 :
        print('Error : This function is currently allowing up to 3 x 3 matrix')
        return None
    
    if row == 1 : 
        return matrix[0][0]

    if row == 2 : 
        try : 
            for i in range(row) : 
                for j in range(column) : 
                    result = ((matrix[i][j] * matrix[i+1][j+1]) - (matrix[i][j+1] * matrix[i+1][j]))
                    return result
                
        except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None

    if row == 3 :
        try : 
            first_part = (matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])))
            second_part = (matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])))
            third_part = (matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])))
            result = first_part - second_part + third_part
            return result
        except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None

# mean-median-node fuction

def mean(inp_set) : 
    """
    Gives the mean value of a set

    Args:
        set = Input set given by user
    
    Returns:
        Mean value of the input set.
        None if the input is not valid or any error occurs.
    """
    temp = []   # this new list will be used to take out all elements as float number.
    try : 
        set_len = len(inp_set)

        if set_len == 0 : 
            print('Error : Set should not be empty.')
            return None
    except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None
    try : 
        for element in inp_set : 
            checker = float(element)
            temp.append(checker)
    except ValueError : 
        print('Error : Please enter a valid number(Integer or Float).')
        return None
    except Exception as error :
        print(f'Error : An unexpected error happened : {error}')
        return None
    try : 
        element_total = 0.0
        for element in temp : 
            element_total = element_total + element    # summation of the set element

        result = element_total / float(set_len)
        return result
    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    
def median(inp_set) : 
    """
    Gives the median value of a set

    Args:
        set = Input set given by user
    
    Returns:
        Median value of the input set.
        None if the input is not valid or any error occurs.
    """
    temp = []   # this new list will be used to take out all elements as float number.
    try : 
        set_len = len(inp_set)

        if set_len == 0 : 
            print('Error : Set should not be empty.')
            return None
    except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None
    try : 
        for element in inp_set : 
            checker = float(element)
            temp.append(checker)
    except ValueError : 
        print('Error : Please enter a valid number(Integer or Float).')
        return None
    except Exception as error :
        print(f'Error : An unexpected error happened : {error}')
        return None
    
    # trying to order the list if not. 
    # here 'bubble sort' is used, maybe i should use sort() function. 
    # actually i dont know how to use sort() function
    try : 
        for counter in range(1, set_len+1) : 
            for ele_index in range(set_len - counter) : 
                if temp[ele_index] > temp[ele_index + 1] :
                    temp[ele_index], temp[ele_index + 1] = temp[ele_index + 1], temp[ele_index]

    except Exception as error : 
        print(f'Error : An unexpected error happened : {error}')
        return None
    
    # if the set have odd element count, like 1, 3, 5, 7, 9 etc
    if set_len % 2 == 1 :       
        try : 
            middle_index = (set_len // 2) + 1       # for example, if we have a set with 5 element then (set_len // 2) will be 2 and plus one 3
            return temp[middle_index - 1]       # python's 0-based indexing
        except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None
    
    # if the set have even element count, like 2, 4, 6, 8 etc
    if set_len % 2 == 0 :
        try : 
            first_middle_index = set_len // 2
            second_middle_index = first_middle_index + 1

            middle_avg = (temp[first_middle_index - 1] + temp[second_middle_index - 1]) / 2  # python's 0-based indexing
            return middle_avg
        
        except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None

def mode(inp_set) : 
    """
    Gives the mode value of a set

    Args:
        set = Input set given by user
    
    Returns:
        Mode value of the input set.
        None if the input is not valid or any error occurs.
    """
    # mode function can be used for any data type.
    try : 
        set_len = len(inp_set)
        if set_len == 0 : 
            print('Error : Set should not be empty.')
            return None
    except Exception as error : 
            print(f'Error : An unexpected error happened : {error}')
            return None
    
    # trying to get the total number of times a element appeared in the set
    try : 
        processed_elements_list = []
        element_details = []

        for i in range(set_len) : 
            current_element = inp_set[i]
            already_done = False

            for processed_element in processed_elements_list :
                if current_element == processed_element :
                    already_done = True 
                    break
            
            if not already_done : 
                count = 0
                for j in range(set_len) :
                    if current_element == inp_set[j] :
                        count += 1
                
                element_details.append([current_element, count])
                processed_elements_list.append(current_element)
    
    except Exception as error :
        print(f'Error : An unexpected error happened : {error}')
        return None
    
    # now sending the mode data
    try : 
        if not element_details: # Handle case where element_details might be empty (e.g., if inp_set was empty, though handled earlier)
            return None

        highest_count = 0
        for i in range(len(element_details)) :
            if element_details[i][1] > highest_count :
                highest_count = element_details[i][1]
        
        highest_count_element = []
        for i in range(len(element_details)) :
            if element_details[i][1] == highest_count :
                highest_count_element.append(element_details[i][0])

        return highest_count_element, highest_count
    
    except Exception as error :
        print(f'Error : An unexpected error happened : {error}')
        return None


# the end