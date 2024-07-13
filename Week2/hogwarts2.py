students = [
	{
		"name":"Hermione",
		"house":"Gryffindor",
		"patronus":"otter",
	},

	{
		"name":"Harry",
		"house":"Gryffindor",
		"patronus":"Stag",

	},

	{
		"name":"Draco",
		"house":"Slytherin",
		"patronus":None,

	}

]


for student in students:
	print(student["name"], student["house"], student["patronus"], sep= ", ")