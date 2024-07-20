import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) > 2 or ".csv" not in sys.argv[1]:
        sys.exit("Something went wrong")

    with open(sys.argv[1], "q") as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File not found")
