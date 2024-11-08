# Calculator Module

## Introduction

This Calculator module provides a simple, memory-based calculator implemented in Python. It supports basic arithmetic
operations (addition, subtraction, multiplication, division) as well as nth root calculations. The calculator maintains
a single value in memory which is modified by these operations. The module supports method chaining for more concise
calculations.

## Installation

To use this calculator module, follow these steps:

1. Ensure you have Python 3.6 or later installed on your system.
2. Download the `calculator.py` file to your project directory.
3. In your Python script, import the Calculator class:

```python
from calculator import Calculator

# Create a new Calculator instance
calc = Calculator()

# Basic usage
calc.add(5)
calc.multiply(2)
calc.subtract(3)
result = calc.divide(2)
print(f"Result: {result}")  # Output: Result: 3.5

# Calculate a root
calc.add(16)
root_result = calc.root(2)
print(f"Square root: {root_result}")  # Output: Square root: 4.0

# Method chaining
result = calc.reset().add(10).multiply(2).subtract(5).divide(3).add(4).root(2).number_in_memory  # Output: 3.0
print(f"Result of chained operations: {result}")
```

Note: Operations are performed in the order they are called, not following standard mathematical order of operations.
Users should be aware of this when chaining multiple operations.
