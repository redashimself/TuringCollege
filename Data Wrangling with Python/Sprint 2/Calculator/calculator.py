import math


class Calculator:
    """
    A simple calculator class that maintains a memory value and performs basic arithmetic operations.

    This calculator can perform addition, subtraction, multiplication, division, and nth root calculations.
    It maintains a single value in memory which is modified by these operations.

    Attributes:
        _number_in_memory (float): The current value stored in the calculator's memory.
    """

    def __init__(self):
        """Initialize the calculator with a memory value of 0."""
        self._number_in_memory = 0

    @property
    def number_in_memory(self):
        """float: The current value stored in the calculator's memory."""
        return self._number_in_memory

    @number_in_memory.setter
    def number_in_memory(self, number_in_memory):
        """Set the value in the calculator's memory."""
        self._number_in_memory = number_in_memory

    def add(self, *numbers):
        """
        Add one or more numbers to the value in memory.

        Args:
            *numbers (float): One or more numbers to add.

        Returns:
            Calculator: The Calculator instance for method chaining.
        """
        for number in numbers:
            self._number_in_memory += number
        return self

    def subtract(self, *numbers):
        """
        Subtract one or more numbers from the value in memory.

        Args:
            *numbers (float): One or more numbers to subtract.

        Returns:
            Calculator: The Calculator instance for method chaining.
        """
        for number in numbers:
            self._number_in_memory -= number
        return self

    def multiply(self, *numbers):
        """
        Multiply the value in memory by one or more numbers.

        Args:
            *numbers (float): One or more numbers to multiply by.

        Returns:
            Calculator: The Calculator instance for method chaining.
        """
        for number in numbers:
            self._number_in_memory *= number
        return self

    def divide(self, *numbers):
        """
        Divide the value in memory by one or more numbers.

        Args:
            *numbers (float): One or more numbers to divide by.

        Returns:
            Calculator: The Calculator instance for method chaining.

        Raises:
            ValueError: If attempting to divide by zero.
        """
        for number in numbers:
            if number != 0:
                self._number_in_memory /= number
            else:
                raise ValueError("Cannot divide by zero")
        return self

    def root(self, n):
        """
        Calculate the nth root of the value in memory.

        Args:
            n (int): The root to calculate.

        Returns:
            Calculator: The Calculator instance for method chaining.

        Raises:
            ValueError: If n is 0 or if attempting to calculate an even root of a negative number.
        """
        if n == 0:
            raise ValueError("Cannot calculate 0th root")
        elif self._number_in_memory < 0 and n % 2 == 0:
            raise ValueError("Cannot calculate even root of a negative number")
        else:
            self._number_in_memory = math.pow(abs(self._number_in_memory), 1 / n) * (
                1 if self._number_in_memory >= 0 else -1)
        return self

    def reset(self):
        """
        Reset the calculator's memory to 0.

        Returns:
            Calculator: The Calculator instance for method chaining.
        """
        self._number_in_memory = 0
        return self
