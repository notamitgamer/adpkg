import adcustom as c

print("--- Comprehensive Test Suite for custom module ---")

# --- Helper function to check test results ---
def check_test(test_name, result, expected, function_prints_error=False):
    """
    Checks the test result against the expected value.
    'function_prints_error' is set to True if the tested function is expected
    to print an error message to console instead of just returning None.
    """
    print(f"  Test Status: ", end="")
    if result == expected:
        print(f"PASS")
    else:
        print(f"FAIL - Expected {expected}, Got {result}")
    if function_prints_error:
        print("  (Note: The function may have printed an error message above)")

# --- Test Cases for check_prime() ---
print("\n--- Testing check_prime() function ---")
result_prime_1 = c.check_prime(7)
print(f"Test check_prime 1: 7")
print(f"Expected: 1")
print(f"Result: {result_prime_1}")
check_test("check_prime 1", result_prime_1, 1)

result_prime_2 = c.check_prime(10)
print(f"\nTest check_prime 2: 10")
print(f"Expected: 0")
print(f"Result: {result_prime_2}")
check_test("check_prime 2", result_prime_2, 0)

result_prime_3 = c.check_prime(2)
print(f"\nTest check_prime 3: 2 (edge case)")
print(f"Expected: 1")
print(f"Result: {result_prime_3}")
check_test("check_prime 3", result_prime_3, 1)

result_prime_4 = c.check_prime(1)
print(f"\nTest check_prime 4: 1 (not prime)")
print(f"Expected: 0")
print(f"Result: {result_prime_4}")
check_test("check_prime 4", result_prime_4, 0)

result_prime_5 = c.check_prime(-5)
print(f"\nTest check_prime 5: -5 (negative input)")
print(f"Expected: None")
print(f"Result: {result_prime_5}")
check_test("check_prime 5", result_prime_5, None, function_prints_error=True)

result_prime_6 = c.check_prime("abc")
print(f"\nTest check_prime 6: 'abc' (invalid input type)")
print(f"Expected: None")
print(f"Result: {result_prime_6}")
check_test("check_prime 6", result_prime_6, None, function_prints_error=True)

# --- Test Cases for factorial() ---
print("\n--- Testing factorial() function ---")
result_fact_1 = c.factorial(5)
print(f"Test factorial 1: 5")
print(f"Expected: 120")
print(f"Result: {result_fact_1}")
check_test("factorial 1", result_fact_1, 120)

result_fact_2 = c.factorial(0)
print(f"\nTest factorial 2: 0 (edge case)")
print(f"Expected: 1")
print(f"Result: {result_fact_2}")
check_test("factorial 2", result_fact_2, 1)

result_fact_3 = c.factorial(-3)
print(f"\nTest factorial 3: -3 (negative input)")
print(f"Expected: None")
print(f"Result: {result_fact_3}")
check_test("factorial 3", result_fact_3, None, function_prints_error=True)

# --- Test Cases for permutation() ---
print("\n--- Testing permutation() function ---")
result_perm_1 = c.permutation(5, 2)
print(f"Test permutation 1: P(5, 2)")
print(f"Expected: 20")
print(f"Result: {result_perm_1}")
check_test("permutation 1", result_perm_1, 20)

result_perm_2 = c.permutation(3, 3)
print(f"\nTest permutation 2: P(3, 3)")
print(f"Expected: 6")
print(f"Result: {result_perm_2}")
check_test("permutation 2", result_perm_2, 6)

result_perm_3 = c.permutation(5, 7)
print(f"\nTest permutation 3: P(5, 7) (k > n)")
print(f"Expected: None")
print(f"Result: {result_perm_3}")
check_test("permutation 3", result_perm_3, None, function_prints_error=True)

# --- Test Cases for combination() ---
print("\n--- Testing combination() function ---")
result_comb_1 = c.combination(5, 2)
print(f"Test combination 1: C(5, 2)")
print(f"Expected: 10")
print(f"Result: {result_comb_1}")
check_test("combination 1", result_comb_1, 10)

result_comb_2 = c.combination(3, 3)
print(f"\nTest combination 2: C(3, 3)")
print(f"Expected: 1")
print(f"Result: {result_comb_2}")
check_test("combination 2", result_comb_2, 1)

result_comb_3 = c.combination(5, 7)
print(f"\nTest combination 3: C(5, 7) (k > n)")
print(f"Expected: 0") # Your function returns 0 for k > n
print(f"Result: {result_comb_3}")
check_test("combination 3", result_comb_3, 0)

# --- Test Cases for string_reverse() ---
print("\n--- Testing string_reverse() function ---")
result_str_rev_1 = c.string_reverse("hello")
print(f"Test string_reverse 1: 'hello'")
print(f"Expected: 'olleh'")
print(f"Result: {result_str_rev_1}")
check_test("string_reverse 1", result_str_rev_1, "olleh")

result_str_rev_2 = c.string_reverse("")
print(f"\nTest string_reverse 2: '' (empty string)")
print(f"Expected: None")
print(f"Result: {result_str_rev_2}")
check_test("string_reverse 2", result_str_rev_2, None, function_prints_error=True)

# --- Test Cases for matrix_addition() ---
print("\n--- Testing matrix_addition() function ---")
mat_add_1 = [[1, 2], [3, 4]]
mat_add_2 = [[5, 6], [7, 8]]
expected_add_mat = "6 8 \n10 12 \n"
result_mat_add_1 = c.matrix_addition(mat_add_1, mat_add_2)
print(f"Test matrix_addition 1: Adding {mat_add_1} and {mat_add_2}")
print(f"Expected:\n{expected_add_mat}")
print(f"Result:\n{result_mat_add_1}")
check_test("matrix_addition 1", result_mat_add_1, expected_add_mat)

mat_add_incompatible_1 = [[1, 2]]
mat_add_incompatible_2 = [[1, 2, 3]]
result_mat_add_2 = c.matrix_addition(mat_add_incompatible_1, mat_add_incompatible_2)
print(f"\nTest matrix_addition 2: Incompatible dimensions {mat_add_incompatible_1} and {mat_add_incompatible_2}")
print(f"Expected: None")
print(f"Result: {result_mat_add_2}")
check_test("matrix_addition 2", result_mat_add_2, None, function_prints_error=True)

# --- Test Cases for matrix_multiplication() ---
print("\n--- Testing matrix_multiplication() function ---")
mat_mult_1 = [[1, 2], [3, 4]]
mat_mult_2 = [[5, 6], [7, 8]]
expected_mult_mat = "19 22 \n43 50 \n"
result_mat_mult_1 = c.matrix_multiplication(mat_mult_1, mat_mult_2)
print(f"Test matrix_multiplication 1: Multiplying {mat_mult_1} and {mat_mult_2}")
print(f"Expected:\n{expected_mult_mat}")
print(f"Result:\n{result_mat_mult_1}")
check_test("matrix_multiplication 1", result_mat_mult_1, expected_mult_mat)

mat_mult_incompatible_1 = [[1, 2]]
mat_mult_incompatible_2 = [[1], [2], [3]]
result_mat_mult_2 = c.matrix_multiplication(mat_mult_incompatible_1, mat_mult_incompatible_2)
print(f"\nTest matrix_multiplication 2: Incompatible dimensions {mat_mult_incompatible_1} and {mat_mult_incompatible_2}")
print(f"Expected: None")
print(f"Result: {result_mat_mult_2}")
check_test("matrix_multiplication 2", result_mat_mult_2, None, function_prints_error=True)

# --- Test Cases for matrix_transpose() ---
print("\n--- Testing matrix_transpose() function ---")
mat_trans_1 = [[1, 2, 3], [4, 5, 6]]
expected_trans_mat = "1 4 \n2 5 \n3 6 \n"
result_mat_trans_1 = c.matrix_transpose(mat_trans_1)
print(f"Test matrix_transpose 1: Transposing {mat_trans_1}")
print(f"Expected:\n{expected_trans_mat}")
print(f"Result:\n{result_mat_trans_1}")
check_test("matrix_transpose 1", result_mat_trans_1, expected_trans_mat)

mat_trans_2 = [[10]]
expected_trans_mat_2 = "10 \n"
result_mat_trans_2 = c.matrix_transpose(mat_trans_2)
print(f"\nTest matrix_transpose 2: Transposing {mat_trans_2}")
print(f"Expected:\n{expected_trans_mat_2}")
print(f"Result:\n{result_mat_trans_2}")
check_test("matrix_transpose 2", result_mat_trans_2, expected_trans_mat_2)


# --- Test Cases for determinant_value() ---
print("\n--- Testing determinant_value() function ---")
det_1 = [[5]]
result_det_1 = c.determinant_value(det_1)
print(f"Test determinant_value 1: 1x1 matrix {det_1}")
print(f"Expected: 5")
print(f"Result: {result_det_1}")
check_test("determinant_value 1", result_det_1, 5)

det_2 = [[1, 2], [3, 4]]
result_det_2 = c.determinant_value(det_2)
print(f"\nTest determinant_value 2: 2x2 matrix {det_2}")
print(f"Expected: -2") # (1*4 - 2*3) = 4 - 6 = -2
print(f"Result: {result_det_2}")
check_test("determinant_value 2", result_det_2, -2)

det_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_det_3 = c.determinant_value(det_3)
print(f"\nTest determinant_value 3: 3x3 matrix {det_3}")
print(f"Expected: 0")
print(f"Result: {result_det_3}")
check_test("determinant_value 3", result_det_3, 0)

det_non_square = [[1, 2], [3, 4], [5, 6]]
result_det_4 = c.determinant_value(det_non_square)
print(f"\nTest determinant_value 4: Non-square matrix {det_non_square}")
print(f"Expected: None")
print(f"Result: {result_det_4}")
check_test("determinant_value 4", result_det_4, None, function_prints_error=True)

# --- Test Cases for mean() ---
print("\n--- Testing mean() function ---")
test_mean_1 = [1, 2, 3, 4, 5]
result_mean_1 = c.mean(test_mean_1)
print(f"Test mean 1: {test_mean_1}")
print(f"Expected: 3.0")
print(f"Result: {result_mean_1}")
check_test("mean 1", result_mean_1, 3.0)

test_mean_2 = [10, 20, 30]
result_mean_2 = c.mean(test_mean_2)
print(f"\nTest mean 2: {test_mean_2}")
print(f"Expected: 20.0")
print(f"Result: {result_mean_2}")
check_test("mean 2", result_mean_2, 20.0)

test_mean_3 = []
result_mean_3 = c.mean(test_mean_3)
print(f"\nTest mean 3: Empty list {test_mean_3}")
print(f"Expected: None")
print(f"Result: {result_mean_3}")
check_test("mean 3", result_mean_3, None, function_prints_error=True)

# --- Test Cases for median() ---
print("\n--- Testing median() function ---")
test_median_odd = [5, 2, 8, 1, 9] # Sorted: [1, 2, 5, 8, 9] -> Median: 5
result_median_odd = c.median(test_median_odd)
print(f"Test median 1: Odd length list {test_median_odd}")
print(f"Expected: 5.0")
print(f"Result: {result_median_odd}")
check_test("median 1", result_median_odd, 5.0)

test_median_even = [5, 2, 8, 1, 9, 3] # Sorted: [1, 2, 3, 5, 8, 9] -> Median: (3+5)/2 = 4
result_median_even = c.median(test_median_even)
print(f"\nTest median 2: Even length list {test_median_even}")
print(f"Expected: 4.0")
print(f"Result: {result_median_even}")
check_test("median 2", result_median_even, 4.0)

test_median_empty = []
result_median_empty = c.median(test_median_empty)
print(f"\nTest median 3: Empty list {test_median_empty}")
print(f"Expected: None")
print(f"Result: {result_median_empty}")
check_test("median 3", result_median_empty, None, function_prints_error=True)

# --- Test Cases for mode() ---
# Re-using the test cases that were previously confirmed to work with your mode implementation
print("\n--- Testing mode() function ---")

# Test Case 1: Standard case with a clear mode
test_list_mode_1 = [1, 2, 3, 2, 1, 5, 1, 1, 2, 6, 5, 54, 52, 5]
print(f"\nTest mode 1: Standard list: {test_list_mode_1}")
result_mode_1 = c.mode(test_list_mode_1)
print(f"Expected: ([1], 4)")
print(f"Result: {result_mode_1}")
check_test("mode 1", result_mode_1, ([1], 4))

# Test Case 2: List with multiple modes
test_list_mode_2 = [10, 20, 30, 20, 10, 40, 50]
print(f"\nTest mode 2: List with multiple modes: {test_list_mode_2}")
result_mode_2 = c.mode(test_list_mode_2)
print(f"Expected: ([10, 20], 2)")
print(f"Result: {result_mode_2}")
check_test("mode 2", result_mode_2, ([10, 20], 2))

# Test Case 3: List with no repeating elements
test_list_mode_3 = [1, 2, 3, 4, 5]
print(f"\nTest mode 3: List with no repeating elements: {test_list_mode_3}")
result_mode_3 = c.mode(test_list_mode_3)
print(f"Expected: ([1, 2, 3, 4, 5], 1)")
print(f"Result: {result_mode_3}")
check_test("mode 3", result_mode_3, ([1, 2, 3, 4, 5], 1))

# Test Case 4: List with all same elements
test_list_mode_4 = [7, 7, 7, 7, 7]
print(f"\nTest mode 4: List with all same elements: {test_list_mode_4}")
result_mode_4 = c.mode(test_list_mode_4)
print(f"Expected: ([7], 5)")
print(f"Result: {result_mode_4}")
check_test("mode 4", result_mode_4, ([7], 5))

# Test Case 5: Empty list
test_list_mode_5 = []
print(f"\nTest mode 5: Empty list: {test_list_mode_5}")
result_mode_5 = c.mode(test_list_mode_5)
print(f"Expected: None")
print(f"Result: {result_mode_5}")
check_test("mode 5", result_mode_5, None, function_prints_error=True)

# Test Case 6: List with negative numbers and zeros
test_list_mode_6 = [-1, 0, -5, 0, -1, 10]
print(f"\nTest mode 6: List with negative numbers and zeros: {test_list_mode_6}")
result_mode_6 = c.mode(test_list_mode_6)
print(f"Expected: ([-1, 0], 2)")
print(f"Result: {result_mode_6}")
check_test("mode 6", result_mode_6, ([-1, 0], 2))

# Test Case 7: List with strings (checking versatility for different data types)
test_list_mode_7 = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(f"\nTest mode 7: List with strings: {test_list_mode_7}")
result_mode_7 = c.mode(test_list_mode_7)
print(f"Expected: (['apple'], 3)")
print(f"Result: {result_mode_7}")
check_test("mode 7", result_mode_7, (['apple'], 3))

# Test Case 8: Invalid input (integer) for mode
test_invalid_input_mode = 123
print(f"\nTest mode 8: Invalid input (integer): {test_invalid_input_mode}")
result_invalid_mode = c.mode(test_invalid_input_mode)
print(f"Expected: None")
print(f"Result: {result_invalid_mode}")
check_test("mode 8", result_invalid_mode, None, function_prints_error=True)


print("\n--- All tests completed. Review the 'Test Status' lines for results. ---")