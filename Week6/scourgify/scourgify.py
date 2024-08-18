import csv
import sys
names = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:

        with open(f"{sys.argv[1]}") as file:

            reader = csv.DictReader(file)

            for row in reader:
                last ,first = row["name"].split(",")
                first = first.strip()
                last = last.strip()

                names.append({"first": first, "last":last, "house":row["house"]})





        with open(f"{sys.argv[2]}","w") as file:
            writer = csv.DictWriter(file,fieldnames=["first","last","house"])
            writer.writeheader()
            for name in names:
                writer.writerow({"first":name["first"], "last":name["last"], "house":name["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
