student = ["Hermione", "Harry", "Ron","Draco"]

houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


students = {

	"Hermione":"Gryffindor",
	"Harry":"Gryffindor",
	"Ron": "Gryffindor",
	"Draco": "Slytherin",
}

for student in students:
	print(student,students[student],sep =", ")