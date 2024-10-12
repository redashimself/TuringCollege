import sys

try:
    if len(sys.argv) > 2 or ".py" not in sys.argv[1]:
        sys.exit("Something went wrong")

    fileToOpen = sys.argv[1]

    with open(fileToOpen) as file:
        lines = file.readlines()

    lineCount = 0

    for line in lines:
        if line.strip().startswith("#") or len(line.strip()) == 0:
            lineCount += 0
        else:
            lineCount += 1

    file.close()

    print(lineCount)

except FileNotFoundError:
    sys.exit("File not found")
