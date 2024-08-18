import sys
lines = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
file_name = sys.argv[1]
try:
    name,extension = file_name.split(".")

    if extension != "py":
        sys.exit("Not a python file.")
except ValueError:
    sys.exit("Not a python file")
try:
    with open(f"{file_name}") as file:
        for line in file:
            line = line.rstrip()
            line = line.replace(" ","")
            comment = line.lstrip()

            if line == "" or "#" in comment[0]:
                continue
            else:
                lines.append(line)


except FileNotFoundError:
    sys.exit("File does not exist")

print(len(lines), end="")
