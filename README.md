# Advanced Math Utilities (adpkg)

Welcome! 👋 This package gives you a bunch of handy tools for math, finance, and geometry in Python. You don’t need to be a math expert—just import and use!

It includes modules for:
- **Finance**: Calculate compound interest easily
- **Number Theory**: Check primes, factorials, permutations and combinations
- **Strings**: Reverse words or phrases
- **Matrices**: Add, multiply, transpose, and find determinants
- **Statistics**: Mean, median, mode
- **Geometry**: Triangle area with Heron’s formula

[![PyPI version](https://img.shields.io/pypi/v/adpkg.svg)](https://pypi.org/project/adpkg/)
[![Python](https://img.shields.io/pypi/pyversions/adpkg.svg)](https://pypi.org/project/adpkg/)
[![License](https://img.shields.io/github/license/notamitgamer/adpkg)](https://github.com/notamitgamer/adpkg/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/adpkg)](https://pepy.tech/project/adpkg)
[![Last Commit](https://img.shields.io/github/last-commit/notamitgamer/adpkg)](https://github.com/notamitgamer/adpkg/commits/main)
[![Contributors](https://img.shields.io/github/contributors/notamitgamer/adpkg)](https://github.com/notamitgamer/adpkg/graphs/contributors)

---

## 📑 Table of Contents
- [📦 Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [💰 Finance Module](#-finance-module)
  - [interest](#interestprime_amount-time_duration_str-n-rate)
- [🔢 AdCustom Module](#-adcustom-module)
  - [Number Theory](#number-theory)
    - [check_prime](#check_primen)
    - [factorial](#factorialn)
    - [permutation](#permutationn-r)
    - [combination](#combinationn-r)
  - [Strings](#strings)
    - [string_reverse](#string_reverses)
  - [Matrices](#matrices)
    - [matrix_addition](#matrix_additiona-b)
    - [matrix_multiplication](#matrix_multiplicationa-b)
    - [matrix_transpose](#matrix_transposea)
    - [determinant_value](#determinant_valuea)
  - [Statistics](#statistics)
    - [mean](#meandata)
    - [median](#mediandata)
    - [mode](#modedata)
- [🔺 Triangle Module](#-triangle-module)
  - [areaoftriangle](#areaoftrianglea-b-c-unit)
- [🧪 Running Tests](#-running-tests)
- [🛠️ Contributing](#-contributing)
- [🗺️ Roadmap](#-roadmap)
- [📜 License](#-license)

---

## 📦 Installation

Install from PyPI (make sure you have Python installed):
```bash
pip install adpkg
```

Check if it worked:
```bash
python -m pip show adpkg
```

---

## 🚀 Quick Start

Here are simple examples to get you started. More detailed examples are below.

```python
from adpkg import finance, adcustom, triangle

# Calculate compound interest
print(finance.interest(1000, "1y", 12, 5))

# Factorial
print(adcustom.factorial(5))

# Reverse a string
print(adcustom.string_reverse("hello"))

# Area of a triangle
print(triangle.areaoftriangle(3, 4, 5))
```

---

## 💰 Finance Module

### `interest(prime_amount, time_duration_str, n, rate)`
- Calculates compound interest based on years/months.
- Duration formats: `"2y"`, `"6m"`, or `"1y6m"`.

```python
from adpkg import finance
print(finance.interest(1000, "1y", 12, 5))   # 51.161
print(finance.interest(2000, "5y", 4, 7))   # 816.622

# Edge case: invalid input
print(finance.interest(1000, "abc", 12, 5))  # None
```

---

## 🔢 AdCustom Module

### Number Theory

#### `check_prime(n)` → 1 if prime, 0 if not, None if invalid.
```python
print(adcustom.check_prime(17))  # 1
print(adcustom.check_prime(10))  # 0
```

#### `factorial(n)`
```python
print(adcustom.factorial(5))   # 120
print(adcustom.factorial(-2))  # None
```

#### `permutation(n, r)`
```python
print(adcustom.permutation(5, 2))  # 20
```

#### `combination(n, r)`
```python
print(adcustom.combination(5, 2))  # 10
```

### Strings

#### `string_reverse(s)`
```python
print(adcustom.string_reverse("hello"))  # "olleh"
```

### Matrices

#### `matrix_addition(a, b)`
```python
print(adcustom.matrix_addition([[1,2],[3,4]], [[5,6],[7,8]]))
# [[6,8],[10,12]]
```

#### `matrix_multiplication(a, b)`
```python
print(adcustom.matrix_multiplication([[1,2],[3,4]], [[5,6],[7,8]]))
# [[19,22],[43,50]]
```

#### `matrix_transpose(a)`
```python
print(adcustom.matrix_transpose([[1,2,3],[4,5,6]]))
# [[1,4],[2,5],[3,6]]
```

#### `determinant_value(a)`
```python
print(adcustom.determinant_value([[1,2],[3,4]]))  # -2
```

### Statistics

#### `mean(data)`
```python
print(adcustom.mean([1,2,3,4,5]))  # 3.0
```

#### `median(data)`
```python
print(adcustom.median([1,3,2,5,4]))  # 3
```

#### `mode(data)`
```python
print(adcustom.mode([1,2,2,3,4,4,4,5]))  # ([4], 3)
```

---

## 🔺 Triangle Module

### `areaoftriangle(a, b, c, unit='')`
- Uses Heron’s formula.
```python
print(triangle.areaoftriangle(3, 4, 5))           # 6.0
print(triangle.areaoftriangle(3, 4, 5, "sq cm")) # "6.0 sq cm"
```

---

## 🧪 Running Tests

We included some test files (`test1.py` – `test5.py`).

Run one test:
```bash
python test1.py
```

Run all tests at once:
```bash
python -m unittest discover -s . -p "test*.py"
```

---
## 🛠️ Contributing

Want to help? Awesome! Here’s how:
1. **Fork this repo** → Make your own copy on GitHub.
2. **Create a branch** → Work on your changes in a separate branch.
3. **Add your code and tests** → Make sure it works!
4. **Open a Pull Request** → Propose your changes.

---

## 🗺️ Roadmap
- ✅ Current: Finance, number theory, strings, matrices, stats, triangles
- 🔜 Next: Probability, calculus, polynomials, advanced linear algebra
- 📊 Future: Machine learning helpers, symbolic algebra, optimization

---

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 📬 Contact

[![Author](https://img.shields.io/badge/Author-Amit%20Dutta-blue)](https://github.com/notamitgamer)  
[![Email](https://img.shields.io/badge/Email-amitdutta4255%40gmail.com-red)](mailto:amitdutta4255@gmail.com)  
[![GitHub](https://img.shields.io/badge/GitHub-notamitgamer-black)](https://github.com/notamitgamer)  
[![PyPI](https://img.shields.io/badge/PyPI-adpkg-green)](https://pypi.org/project/adpkg/)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-notamitgamer-0A66C2)](https://linkedin.com/in/notamitgamer)  
[![Twitter](https://img.shields.io/badge/Twitter-@notamitgamer-1DA1F2)](https://twitter.com/notamitgamer)  
[![Instagram](https://img.shields.io/badge/Instagram-notamitgamer-E4405F)](https://instagram.com/notamitgamer)

