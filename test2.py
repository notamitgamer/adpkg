import adcustom as c

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number (integer or float).")

def get_list_of_numbers_input(prompt):
    while True:
        s = input(prompt)
        if not s.strip(): # Handle empty input for empty list
            return []
        try:
            # Attempt to convert each part to a float, allowing for integers as well
            return [float(x.strip()) for x in s.split(',')]
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers (e.g., 1, 2.5, 3).")

def get_general_list_input(prompt):
    while True:
        s = input(prompt)
        if not s.strip(): # Handle empty input for empty list
            return []
        # For general lists, we'll split by comma and strip spaces.
        # The function itself handles type conversion/validation.
        return [x.strip() for x in s.split(',')]

def get_matrix_input(prompt):
    matrix = []
    print(prompt + " (Enter rows separated by ';', elements by ',' e.g., '1,2;3,4')")
    while True:
        s = input("Enter matrix row(s) (or type 'done' to finish): ").strip()
        if s.lower() == 'done':
            break
        if not s:
            print("Row cannot be empty. Please enter elements or 'done'.")
            continue
        try:
            rows_str = s.split(';')
            current_matrix = []
            for row_str in rows_str:
                row_elements = [float(x.strip()) for x in row_str.split(',')]
                current_matrix.append(row_elements)

            # Basic validation for consistency of rows for the first row entered
            if not matrix and current_matrix: # If this is the first matrix input
                for r in current_matrix:
                    matrix.append(r)
            elif matrix and current_matrix: # If subsequent rows, check consistency
                if len(current_matrix[0]) != len(matrix[0]):
                    print("Error: All rows must have the same number of columns.")
                    matrix = [] # Clear and restart input for this matrix
                    raise ValueError("Inconsistent column count")
                for r in current_matrix:
                    matrix.append(r)
            else: # If s was empty or only whitespace, and not 'done'
                print("Invalid row input. Please enter comma-separated numbers.")
                continue
            return matrix
        except ValueError as e:
            if "Inconsistent column count" in str(e): # Handled above, restart loop
                continue
            print("Invalid matrix input. Ensure elements are numbers and rows are comma-separated.")
            print("Example: '1,2;3,4' for [[1,2],[3,4]]")
            matrix = [] # Clear and retry input if invalid format
            continue

    if not matrix:
        print("No valid matrix entered.")
        return None # Return None if no matrix was successfully entered or user exits without input
    return matrix


def run_interactive_test():
    print("--- Interactive Test for custom.py module ---")
    while True:
        print("\nSelect a function to test:")
        print("1. add(num1, num2)")
        print("2. check_prime(num)")
        print("3. factorial(num)")
        print("4. permutation(total, chosen)")
        print("5. combination(total, chosen)")
        print("6. string_reverse(text)")
        print("7. matrix_addition(mat1, mat2)")
        print("8. matrix_multiplication(mat1, mat2)")
        print("9. matrix_transpose(mat)")
        print("10. determinant_value(mat)")
        print("11. mean(data_list)")
        print("12. median(data_list)")
        print("13. mode(data_list)")
        print("0. Exit")

        choice = input("Enter your choice (0-13): ")

        if choice == '0':
            print("Exiting interactive test. Goodbye!")
            break
        elif choice == '1':
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = c.add(num1, num2)
            print(f"Result of add({num1}, {num2}): {result}")
        elif choice == '2':
            num = get_integer_input("Enter an integer to check if prime: ")
            result = c.check_prime(num)
            print(f"Result of check_prime({num}): {result} (1=Prime, 0=Not Prime, None=Error)")
        elif choice == '3':
            num = get_integer_input("Enter a non-negative integer for factorial: ")
            result = c.factorial(num)
            print(f"Result of factorial({num}): {result}")
        elif choice == '4':
            n = get_integer_input("Enter total items (n): ")
            k = get_integer_input("Enter chosen items (k): ")
            result = c.permutation(n, k)
            print(f"Result of permutation({n}, {k}): {result}")
        elif choice == '5':
            n = get_integer_input("Enter total items (n): ")
            k = get_integer_input("Enter chosen items (k): ")
            result = c.combination(n, k)
            print(f"Result of combination({n}, {k}): {result}")
        elif choice == '6':
            text = input("Enter a string to reverse: ")
            result = c.string_reverse(text)
            print(f"Result of string_reverse('{text}'): {result}")
        elif choice == '7':
            print("\n--- Input for Matrix 1 ---")
            mat1 = get_matrix_input("Matrix 1")
            print("\n--- Input for Matrix 2 ---")
            mat2 = get_matrix_input("Matrix 2")
            if mat1 is not None and mat2 is not None:
                print("\nCalculating Matrix Addition...")
                result = c.matrix_addition(mat1, mat2)
                print(f"Result of matrix_addition:\n{result}")
            else:
                print("Matrix input was invalid or incomplete. Cannot perform addition.")
        elif choice == '8':
            print("\n--- Input for Matrix 1 ---")
            mat1 = get_matrix_input("Matrix 1")
            print("\n--- Input for Matrix 2 ---")
            mat2 = get_matrix_input("Matrix 2")
            if mat1 is not None and mat2 is not None:
                print("\nCalculating Matrix Multiplication...")
                result = c.matrix_multiplication(mat1, mat2)
                print(f"Result of matrix_multiplication:\n{result}")
            else:
                print("Matrix input was invalid or incomplete. Cannot perform multiplication.")
        elif choice == '9':
            mat = get_matrix_input("\n--- Input for Matrix to Transpose ---")
            if mat is not None:
                print("\nCalculating Matrix Transpose...")
                result = c.matrix_transpose(mat)
                print(f"Result of matrix_transpose:\n{result}")
            else:
                print("Matrix input was invalid or incomplete. Cannot perform transpose.")
        elif choice == '10':
            mat = get_matrix_input("\n--- Input for Matrix to get Determinant Value ---")
            if mat is not None:
                print("\nCalculating Determinant Value...")
                result = c.determinant_value(mat)
                print(f"Result of determinant_value: {result}")
            else:
                print("Matrix input was invalid or incomplete. Cannot calculate determinant.")
        elif choice == '11':
            data_list = get_list_of_numbers_input("Enter comma-separated numbers for mean (e.g., 1,2,3.5): ")
            result = c.mean(data_list)
            print(f"Result of mean({data_list}): {result}")
        elif choice == '12':
            data_list = get_list_of_numbers_input("Enter comma-separated numbers for median (e.g., 1,2,3.5): ")
            result = c.median(data_list)
            print(f"Result of median({data_list}): {result}")
        elif choice == '13':
            # Mode can take mixed types
            data_list = get_general_list_input("Enter comma-separated values for mode (e.g., apple,banana,apple,1,2,1): ")
            result = c.mode(data_list)
            print(f"Result of mode({data_list}): {result}")
        else:
            print("Invalid choice. Please enter a number between 0 and 13.")

# Run the interactive test
if __name__ == "__main__":
    run_interactive_test()