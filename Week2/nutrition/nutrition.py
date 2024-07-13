Fruits = [


    {
        "Item":"Avocado",
        "Calorie":50,
    },
    {
        "Item":"Banana",
        "Calorie":110,
    },
    {
        "Item":"Cantaloupe",
        "Calorie":50,
    },
    {
        "Item":"Grapefruit",
        "Calorie":60,
    },
    {
        "Item":"Grapes",
        "Calorie":90,
    },
    {
        "Item":"Honeydew Melon",
        "Calorie":50,
    },
    {
        "Item":"Kiwifruit",
        "Calorie":90,
    },
    {
        "Item":"Lemon",
        "Calorie":15,
    },
    {
        "Item":"Lime",
        "Calorie":20,
    },
    {
        "Item":"Nectarine",
        "Calorie":60,
    },
    {
        "Item":"Orange",
        "Calorie":80,
    },
    {
        "Item":"Peach",
        "Calorie":60,
    },
    {
        "Item":"Pear",
        "Calorie":100,
    },
    {
        "Item":"Pineapple",
        "Calorie":50,
    },
    {
        "Item":"Plums",
        "Calorie":70,
    },
    {
        "Item":"Strawberries",
        "Calorie":50,
    },
    {
        "Item":"Sweet Cherries",
        "Calorie":100,
    },
    {
        "Item":"Tangerine",
        "Calorie":50,
    },
    {
        "Item":"Watermelon",
        "Calorie":80,
    },
    {
        "Item":"Apple",
        "Calorie":130,
    }
    ,
        
        ]

userinput = input("Item: ")

for Fruit in Fruits:
    if Fruit["Item"].lower() == userinput.lower():
        print("Calories:",Fruit["Calorie"])
