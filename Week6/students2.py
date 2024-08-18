import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)  #you can also use DictReader if you want to get dictionary instead of list.
    for row in reader:
        students.append({"name":row["name"], "home":row["home"]})



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

for student in sorted(students, key=lambda student: student["home"]) :
    print(f"{student['name']} is in {student['home']}")
