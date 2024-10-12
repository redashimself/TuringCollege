# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import math
from itertools import combinations


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    letters = lines[1].split()
    K = int(lines[2])
    return N, letters, K


def calculate_probability(N, letters, K):
    total_combinations = math.comb(N, K)
    number_of_a = letters.count('a')
    number_of_not_a = N - number_of_a

    combinations_without_a = math.comb(number_of_not_a, K)

    prob_no_a = combinations_without_a / total_combinations

    prob_at_least_one_a = 1 - prob_no_a

    return prob_at_least_one_a


def main():
    # Input as a string
    input_str = """4
    a a c d
    2"""

    # Parse input
    N, letters, K = parse_input(input_str)

    # Calculate probability
    result = calculate_probability(N, letters, K)

    # Expected output
    expected_output = 0.833333333333

    # Compare result with expected output
    if abs(result - expected_output) < 1e-9:  # Using small epsilon for float comparison
        print("Test passed!")
    else:
        print(f"Test failed. Expected {expected_output}, but got {result}")


if __name__ == "__main__":
    main()
