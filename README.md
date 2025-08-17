# Advanced Math Utilities

A comprehensive Python package for various mathematical and financial calculations. This package includes modules for:
- **Finance**: Compound interest
- **Number Theory**: Prime checking, factorial, permutation, combination
- **String Manipulation**: String reversal
- **Matrix Operations**: Addition, multiplication, transpose, determinant
- **Statistics**: Mean, median, mode
- **Geometry**: Area of triangle

[![PyPI version](https://img.shields.io/pypi/v/adpkg.svg)](https://pypi.org/project/adpkg/)
[![Python](https://img.shields.io/pypi/pyversions/adpkg.svg)](https://pypi.org/project/adpkg/)
[![License](https://img.shields.io/github/license/notamitgamer/adpkg)](https://github.com/notamitgamer/adpkg/blob/main/LICENSE)

---

## 📦 Installation

Install from PyPI:
```bash
pip install adpkg
```

Verify installation:
```bash
python -m pip show adpkg
```

---

## 🚀 Usage

Here is the **detailed documentation** for each module and function, with examples, expected results, and edge cases.

---

### 💰 Finance Module (`finance.py`)

#### Function: `interest(prime_amount, time_duration_str, number_of_times_interest_will_compound_per_year, rate_of_interest)`

Calculates compound interest.

**Examples:**
```python
from adpkg import finance

# 1 year, monthly compounding
i1 = finance.interest(1000, "1y", 12, 5)
print(i1)  # 51.161

# 5 years, quarterly compounding
i2 = finance.interest(2000, "5y", 4, 7)
print(i2)  # 816.622

# 2 years 6 months, daily compounding
i3 = finance.interest(500, "2y6m", 365, 4.5)
print(i3)  # 61.446

# Edge cases
print(finance.interest(-1000, "1y", 12, 5))   # None (negative principal)
print(finance.interest(1000, "abc", 12, 5))   # None (invalid time format)
print(finance.interest(1000, "1y", 0, 5))     # None (zero compounding)
```

---

### 🔢 AdCustom Module (`adcustom.py`)

#### Number Theory

##### `check_prime(inp)`
```python
from adpkg import adcustom
print(adcustom.check_prime(17))   # 1
print(adcustom.check_prime(10))   # 0
print(adcustom.check_prime(-5))   # None
print(adcustom.check_prime("a")) # None
```

##### `factorial(inp)`
```python
print(adcustom.factorial(5))   # 120
print(adcustom.factorial(0))   # 1
print(adcustom.factorial(-2))  # None
print(adcustom.factorial("x"))# None
```

##### `permutation(total_item, chosen_item)`
```python
print(adcustom.permutation(5, 2))   # 20
print(adcustom.permutation(6, 3))   # 120
print(adcustom.permutation(4, -1))  # None
print(adcustom.permutation("a", 2))# None
```

##### `combination(total_item, chosen_item)`
```python
print(adcustom.combination(5, 2))    # 10
print(adcustom.combination(6, 3))    # 20
print(adcustom.combination(4, -1))   # None
print(adcustom.combination("a", 3)) # None
```

---

#### String Manipulation

##### `string_reverse(string)`
```python
print(adcustom.string_reverse("hello"))   # 'olleh'
print(adcustom.string_reverse("adpkg"))   # 'gkpda'
print(adcustom.string_reverse(""))        # ''
print(adcustom.string_reverse(123))        # None (invalid input)
```

---

#### Matrix Operations

##### `matrix_addition(matrix1, matrix2)`
```python
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(adcustom.matrix_addition(mat1, mat2))  # [[6, 8], [10, 12]]

# Edge case: mismatched dimensions
mat3 = [[1, 2, 3], [4, 5, 6]]
print(adcustom.matrix_addition(mat1, mat3))  # None
```

##### `matrix_multiplication(matrix1, matrix2)`
```python
print(adcustom.matrix_multiplication(mat1, mat2))  # [[19, 22], [43, 50]]

# Edge case: incompatible dimensions
mat_bad = [[1, 2, 3]]
print(adcustom.matrix_multiplication(mat1, mat_bad))  # None
```

##### `matrix_transpose(matrix)`
```python
mat = [[1, 2, 3], [4, 5, 6]]
print(adcustom.matrix_transpose(mat))  # [[1, 4], [2, 5], [3, 6]]

# Edge case: empty matrix
print(adcustom.matrix_transpose([]))   # None
```

##### `determinant_value(matrix)`
```python
print(adcustom.determinant_value([[1, 2], [3, 4]]))  # -2
print(adcustom.determinant_value([[1, 2, 3], [0, 1, 4], [5, 6, 0]]))  # 1

# Edge case: >3x3 matrix
big_mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(adcustom.determinant_value(big_mat))  # None
```

---

#### Statistics

##### `mean(inp_set)`
```python
data = [1, 2, 3, 4, 5]
print(adcustom.mean(data))  # 3.0
print(adcustom.mean([]))    # None
print(adcustom.mean("x"))  # None
```

##### `median(inp_set)`
```python
data = [1, 3, 2, 5, 4]
print(adcustom.median(data))  # 3

data_even = [1, 2, 3, 4]
print(adcustom.median(data_even))  # 2.5

# Edge case: invalid input
print(adcustom.median("abc"))  # None
```

##### `mode(inp_set)`
```python
data = [1, 2, 2, 3, 4, 4, 4, 5]
print(adcustom.mode(data))  # ([4], 3)

single_mode = [10, 10, 20, 30]
print(adcustom.mode(single_mode))  # ([10], 2)

multi_mode = [1, 1, 2, 2, 3]
print(adcustom.mode(multi_mode))  # ([1, 2], 2)

# Edge case: empty list
print(adcustom.mode([]))  # None
```

---

### 🔺 Triangle Module (`triangle.py`)

#### `areaoftriangle(len_a, len_b, len_c, unit='')`
```python
from adpkg import triangle

print(triangle.areaoftriangle(3, 4, 5))             # 6.0
print(triangle.areaoftriangle(3, 4, 5, "sq cm"))   # '6.0 sq cm'
print(triangle.areaoftriangle(7, 8, 9, "m^2"))    # '26.833 m^2'

# Edge cases
print(triangle.areaoftriangle(1, 2, 3))     # None (degenerate triangle)
print(triangle.areaoftriangle(-3, 4, 5))    # None (negative side)
print(triangle.areaoftriangle("a", 4, 5))  # None (invalid input)
```

---

## 🧪 Running Tests

Tests available: `test1.py` – `test5.py`

Run one test:
```bash
python test1.py
```

Run all:
```bash
python -m unittest discover -s . -p "test*.py"
```

---

## 🛠️ Contributing

If you’d like to contribute to this project, here’s how you can help:

- **Fork the repository** → Make your own copy of this project on GitHub.
- **Create a new branch** → Work on a separate branch for your changes (e.g., `feature/new-function`).
- **Add your feature or bug fix with tests** → Write the code and include tests to ensure it works correctly.
- **Open a Pull Request (PR)** → Submit your changes so they can be reviewed and merged into the main project.
---

## 🗺️ Roadmap
- ✅ Implemented: Finance, number theory, strings, matrices, stats, triangles
- 🔜 Coming: Probability, calculus, polynomials, advanced linear algebra
- 📊 Future: Machine learning helpers, symbolic algebra, optimization

---

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
