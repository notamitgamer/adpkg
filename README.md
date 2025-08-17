# Advanced Math Utilities

A comprehensive Python package for various mathematical and financial calculations. This package includes modules for compound interest, number theory (prime checking, factorial, permutation, combination), string manipulation, matrix operations, and basic statistics (mean, median, mode).

[![PyPI version](https://img.shields.io/pypi/v/adpkg.svg)](https://pypi.org/project/adpkg/)
[![Python](https://img.shields.io/pypi/pyversions/adpkg.svg)](https://pypi.org/project/adpkg/)
[![License](https://img.shields.io/github/license/notamitgamer/adpkg)](https://github.com/notamitgamer/adpkg/blob/main/LICENSE)

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install adpkg
```

Verify installation:
```bash
python -m pip show adpkg
```

---

## 🚀 Usage

Here are detailed module descriptions, parameters, return values, and examples.

---

### 💰 Finance Module (`finance.py`)

**`interest(prime_amount, time_duration_str, number_of_times_interest_will_compound_per_year, rate_of_interest)`**

Calculates the compound interest.

**Parameters:**
- `prime_amount` (float or int): Initial principal amount (P).
- `time_duration_str` (str): Duration of investment, must be in short-hand formats:
  - `XyYm` (e.g., `5y6m`, `1y8m`)
  - `Xm` (e.g., `15m`, `6m`)
  - `Xy` (e.g., `5y`, `1y`)
- `number_of_times_interest_will_compound_per_year` (int): Compounding frequency (2=half-yearly, 4=quarterly, 12=monthly, 365=daily).
- `rate_of_interest` (float): Annual nominal rate in percentage.

**Returns:**
- `float`: Compound interest amount (3 decimals).
- `None`: If invalid.

**Example:**
```python
from adpkg import finance

# $1000 at 5% compounded monthly for 1 year
i = finance.interest(1000, "1y", 12, 5)
print(f"Compound interest: ${i}")
```

---

### 🔢 AdCustom Module (`adcustom.py`)

#### Number Theory

**`check_prime(inp)`**
- Input: integer
- Returns: `1` (prime), `0` (not prime), `None` (invalid)

```python
from adpkg import adcustom
print(adcustom.check_prime(17))  # 1
print(adcustom.check_prime(10))  # 0
```

**`factorial(inp)`**
- Input: integer ≥ 0
- Returns: factorial

```python
print(adcustom.factorial(5))  # 120
```

**`permutation(total_item, chosen_item)`**
- Input: n, k
- Returns: P(n, k)

```python
print(adcustom.permutation(5, 2))  # 20
```

**`combination(total_item, chosen_item)`**
- Input: n, k
- Returns: C(n, k)

```python
print(adcustom.combination(5, 2))  # 10
```

---

#### String Manipulation

**`string_reverse(string)`**
- Input: string
- Returns: reversed string

```python
print(adcustom.string_reverse("hello"))  # 'olleh'
```

---

#### Matrix Operations

**`matrix_addition(matrix1, matrix2)`**
- Adds two matrices
- Returns: resulting matrix as string

**`matrix_multiplication(matrix1, matrix2)`**
- Multiplies two matrices
- Returns: product as string

**`matrix_transpose(matrix)`**
- Transposes a matrix
- Returns: result as string

**`determinant_value(matrix)`**
- Calculates determinant (supports ≤3x3)
- Returns: determinant value

```python
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]

print(adcustom.matrix_addition(mat1, mat2))
print(adcustom.matrix_multiplication(mat1, mat2))
print(adcustom.matrix_transpose(mat1))
print(adcustom.determinant_value([[1, 2], [3, 4]]))
```

---

#### Statistics

**`mean(inp_set)`**, **`median(inp_set)`**, **`mode(inp_set)`**

```python
data = [1, 2, 2, 3, 4]
print(adcustom.mean(data))    # 2.4
print(adcustom.median(data))  # 2
print(adcustom.mode(data))    # ([2], 2)
```

---

### 🔺 Triangle Module (`triangle.py`)

**`areaoftriangle(len_a, len_b, len_c, unit='')`**

Calculates the area using **Heron's Formula**.

```python
from adpkg import triangle

print(triangle.areaoftriangle(3, 4, 5))            # 6.0
print(triangle.areaoftriangle(3, 4, 5, "sq cm"))  # '6.0 sq cm'
```

---

## 🧪 Running Tests

The repo includes `test1.py`–`test5.py`, each focusing on specific modules.

Run tests individually:
```bash
python test1.py
python test2.py
python test3.py
```

Run all with unittest:
```bash
python -m unittest discover -s . -p "test*.py"
```

---

## 🛠️ Contributing

- Fork the repo
- Create a branch
- Add new utilities / bug fixes
- Submit a pull request

Please include **tests** for new features.

---

## 🗺️ Roadmap
- ✅ Current: Number theory, finance, matrices, statistics, triangles
- 🔜 Upcoming: Probability, calculus helpers, polynomial tools, advanced linear algebra
- 📊 Long-term: Machine learning helpers, symbolic algebra, optimization functions

---

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
