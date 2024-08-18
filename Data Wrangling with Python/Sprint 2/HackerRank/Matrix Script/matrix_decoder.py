import re


def decode_matrix(n, m, matrix):
    # Transpose the matrix
    transposed = [''.join(row) for row in zip(*matrix)]

    # Join the characters
    decoded = ''.join(transposed)

    # Replace symbols between alphanumeric characters with a space
    final_decoded = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)

    return final_decoded


def main():
    # Read input from file
    with open('input.txt', 'r') as file:
        n, m = map(int, file.readline().split())
        matrix = [file.readline().strip() for _ in range(n)]

    # Decode the matrix
    result = decode_matrix(n, m, matrix)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
