import sys
import math


class Calculator:
    def __init__(self):
        self._number_in_memory = 0

    @property
    def number_in_memory(self):
        return self._number_in_memory

    @number_in_memory.setter
    def number_in_memory(self, number_in_memory):
        self._number_in_memory = number_in_memory

    def add(self, *numbers):
        for number in numbers:
            self._number_in_memory += number
        return self._number_in_memory

    def subtract(self, *numbers):
        for number in numbers:
            self._number_in_memory -= number
        return self._number_in_memory

    def multiply(self, *numbers):
        for number in numbers:
            self._number_in_memory *= number
        return self._number_in_memory

    def divide(self, *numbers):
        for number in numbers:
            if number != 0:
                self._number_in_memory /= number
                return self._number_in_memory
            else:
                raise ValueError("Cannot divide by zero")

    def root(self, n):
        if n == 0:
            raise ValueError("Cannot calculate 0th root")
        elif self._number_in_memory < 0 and n % 2 == 0:
            raise ValueError("Cannot calculate even root of a negative number")
        else:
            self._number_in_memory = math.pow(abs(self._number_in_memory), 1 / n) * (
                1 if self._number_in_memory >= 0 else -1)
        return self._number_in_memory

    def reset(self):
        self._number_in_memory = 0
        return self._number_in_memory


def parse_input(input_string):
    try:
        parts = input_string.split('(')
        command = parts[0].lower().strip()
        if len(parts) > 1:
            args = [float(arg.strip()) for arg in parts[1].rstrip(')').split(',')]
        else:
            args = []
        return command, args
    except:
        return None, None


def main():
    calculator = Calculator()
    print("Welcome to the Calculator!")
    print("Available commands:")
    print("  Add(N)       - Add N numbers to memory")
    print("  Subtract(N)  - Subtract N numbers to memory")
    print("  Multiply(N)  - Multiply memory by N numbers")
    print("  Divide(N)    - Divide memory by N")
    print("  Root(N)      - Take the Nth root of the number in memory")
    print("  Reset        - Reset memory to 0")
    print("  Memory       - Display current memory")
    print("  Exit         - Exit the calculator")

    while True:
        try:
            user_input = input("Enter command: ")
            if user_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                sys.exit(0)

            command, args = parse_input(user_input)

            if command == 'add':
                result = calculator.add(*args)
                print(f"Result: {result}")
            elif command == 'subtract':
                result = calculator.subtract(*args)
                print(f"Result: {result}")
            elif command == 'multiply':
                result = calculator.multiply(*args)
                print(f"Result: {result}")
            elif command == 'divide':
                if len(args) != 1:
                    print("Error: Divide requires exactly one argument")
                else:
                    try:
                        result = calculator.divide(args[0])
                        print(f"Result: {result}")
                    except ValueError as e:
                        print(f"Error: {str(e)}")
            elif command == 'root':
                if len(args) != 1:
                    print("Error: Root requires exactly one argument")
                else:
                    try:
                        result = calculator.root(args[0])
                        print(f"Result: {result}")
                    except ValueError as e:
                        print(f"Error: {str(e)}")
            elif command == 'reset':
                result = calculator.reset()
                print(f"Memory reset. Result: {result}")
            elif command == 'memory':
                print(f"Current memory: {calculator.number_in_memory}")
            else:
                print("Invalid command. Please try again.")

        except ValueError as e:
            print(f"Error: Invalid number input - {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
