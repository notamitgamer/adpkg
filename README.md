# Advanced Math Utilities

A comprehensive Python package for various mathematical and financial calculations. This package includes modules for compound interest, number theory (prime checking, factorial, permutation, combination), string manipulation, matrix operations, and basic statistics (mean, median, mode).

## Installation

You can install this package using pip:

```bash
pip install adpkg
```

## Usage

Here are some examples of how to use the functions provided in this package:

### Finance Module (`finance.py`)

This module provides a function to calculate compound interest.

**`interest(prime_amount, time_duration_str, number_of_times_interest_will_compound_per_year, rate_of_interest)`**

Calculates the compound interest.

* `prime_amount` (float or int): The initial principal amount (P).

* `time_duration_str` (str): The duration for which the interest is calculated, **must be in specific short-hand formats**:

  * "XyYm" (e.g., "5y6m", "1y8m" for 1 year 8 months)

  * "Xm" (e.g., "15m", "6m" for 15 months, 6 months)

  * "Xy" (e.g., "5y", "1y" for 5 years, 1 year)
    Where X and Y are whole numbers.

* `number_of_times_interest_will_compound_per_year` (float or int): The number of times interest is compounded per year (n) (e.g., 2 for half-yearly, 4 for quarterly, 12 for monthly, 365 for daily).

* `rate_of_interest` (float or int): The annual nominal interest rate (as a percentage, e.g., 5 for 5%).

**Returns:**

* `float`: The compound interest amount earned, rounded to 3 decimal places.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import finance

# Calculate interest for $1000 at 5% compounded monthly for 1 year
interest_earned = finance.interest(1000, "1y", 12, 5)
print(f"Compound interest: ${interest_earned}")
```

### AdCustom Module (`adcustom.py`)

This module contains various utility functions for number theory, string manipulation, matrix operations, and statistics.

#### Number Theory

**`check_prime(inp)`**

Checks if the input integer is a Prime number.

* `inp` (int): The non-negative integer to check.

**Returns:**

* `1`: If the input integer is Prime.

* `0`: If the input integer is not Prime.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

print(f"Is 17 prime? {adcustom.check_prime(17)}")
print(f"Is 10 prime? {adcustom.check_prime(10)}")
```

**`factorial(inp)`**

Calculates the factorial of a given non-negative integer.

* `inp` (int): A non-negative integer.

**Returns:**

* `int`: The factorial of the non-negative integer.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

print(f"Factorial of 5: {adcustom.factorial(5)}")
```

**`permutation(total_item, chosen_item)`**

Calculates the number of permutations P(n, k).

* `total_item` (int): The total number of distinct items in the set (n).

* `chosen_item` (int): The number of items to be arranged or chosen from the set at a time (k).

**Returns:**

* `int`: The number of permutations.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

print(f"Permutations of 5 items taken 2 at a time: {adcustom.permutation(5, 2)}")
```

**`combination(total_item, chosen_item)`**

Calculates the number of combinations C(n, k).

* `total_item` (int): The total number of distinct items in the set (n).

* `chosen_item` (int): The number of items to be arranged or chosen from the set at a time (k).

**Returns:**

* `int`: The number of combinations.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

print(f"Combinations of 5 items taken 2 at a time: {adcustom.combination(5, 2)}")
```

#### String Manipulation

**`string_reverse(string)`**

Reverses the given string.

* `string` (str): The input string.

**Returns:**

* `str`: The reversed string.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

print(f"Reversed string 'hello': {adcustom.string_reverse('hello')}")
```

#### Matrix Operations

**`matrix_addition(matrix1, matrix2)`**

Adds two input matrices.

* `matrix1` (list of lists): The first matrix.

* `matrix2` (list of lists): The second matrix.

**Returns:**

* `str`: A string representation of the resulting matrix.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print("Matrix Addition:")
print(adcustom.matrix_addition(mat1, mat2))
```

**`matrix_multiplication(matrix1, matrix2)`**

Multiplies one input matrix with another input matrix.

* `matrix1` (list of lists): The first matrix.

* `matrix2` (list of lists): The second matrix.

**Returns:**

* `str`: A string representation of the resulting matrix.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print("Matrix Multiplication:")
print(adcustom.matrix_multiplication(mat1, mat2))
```

**`matrix_transpose(matrix)`**

Transposes a matrix (row becomes column, column becomes row).

* `matrix` (list of lists): The input matrix.

**Returns:**

* `str`: A string representation of the transposed matrix.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

mat = [[1, 2, 3], [4, 5, 6]]
print("Matrix Transpose:")
print(adcustom.matrix_transpose(mat))
```

**`determinant_value(matrix)`**

Calculates the determinant value of a given matrix. Currently supports matrices up to 3x3.

* `matrix` (list of lists): The input matrix.

**Returns:**

* `int` or `float`: Determinant value of the given matrix.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

mat_2x2 = [[1, 2], [3, 4]]
print(f"Determinant of 2x2 matrix: {adcustom.determinant_value(mat_2x2)}")

mat_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Determinant of 3x3 matrix: {adcustom.determinant_value(mat_3x3)}")
```

#### Statistics

**`mean(inp_set)`**

Calculates the mean value of a set.

* `inp_set` (list or tuple): The input set of numbers.

**Returns:**

* `float`: Mean value of the input set.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

data = [1, 2, 3, 4, 5]
print(f"Mean of {data}: {adcustom.mean(data)}")
```

**`median(inp_set)`**

Calculates the median value of a set.

* `inp_set` (list or tuple): The input set of numbers.

**Returns:**

* `float`: Median value of the input set.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

data_odd = [1, 3, 2, 5, 4]
print(f"Median of {data_odd}: {adcustom.median(data_odd)}")

data_even = [1, 2, 3, 4]
print(f"Median of {data_even}: {adcustom.median(data_even)}")
```

**`mode(inp_set)`**

Calculates the mode value(s) and their count(s) of a set.

* `inp_set` (list or tuple): The input set.

**Returns:**

* `tuple`: A tuple containing a list of mode(s) and the highest count.

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import adcustom

data_mode = [1, 2, 2, 3, 4, 4, 4, 5]
mode_values, count = adcustom.mode(data_mode)
print(f"Mode(s) of {data_mode}: {mode_values} (occurred {count} times)")
```

### Triangle Module (`triangle.py`)

This module calculates the area of a triangle using Heron's formula.

**`areaoftriangle(len_a, len_b, len_c, unit='')`**

Calculates the area of a triangle using Heron's formula: $\\sqrt{s(s-a)(s-b)(s-c)}$

* `len_a` (float or int): A positive number as length of side 'a'.

* `len_b` (float or int): A positive number as length of side 'b'.

* `len_c` (float or int): A positive number as length of side 'c'.

* `unit` (str, optional): Unit of the area (e.g., "sq cm", "m^2"). Defaults to "".

**Returns:**

* `float`: Area of the triangle, rounded to 3 decimal places (if no unit is provided).

* `str`: Area of the triangle with the specified unit (e.g., "12.345 sq cm").

* `None`: If the input is not valid or any error occurs.

**Example:**

```python
from adpkg import triangle

# Calculate area of a 3-4-5 right triangle
area = triangle.areaoftriangle(3, 4, 5, unit="sq cm")
print(f"Area of triangle: {area}")
```

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
