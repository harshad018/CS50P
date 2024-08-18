import sys
import csv
from tabulate import TableFormat, tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        file = sys.argv[1].split(".")


        if file[1] != "csv":
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Not a CSV file")
    else:
        try:
            with open(f"{sys.argv[1]}") as file:
                reader = csv.reader(file)
                header = next(reader)

                data = list(reader)

                print(tabulate(data,headers=header,tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exists")
