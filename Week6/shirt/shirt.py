import sys
import PIL
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        inputfile = sys.argv[1].split(".")
        outputfile = sys.argv[2].split(".")


        if len(inputfile) == 1 and len(outputfile) == 1:
            sys.exit("Invalid input")
        else:
            if inputfile[1] != outputfile[1]:
                sys.exit("Input and output have different extensions")

    except IndexError:
        sys.exit("Input and output have different extensions")

    try:
        toy_image = Image.open(sys.argv[1])

        shirt_image = Image.open("shirt.png")


        resized_toy_image = ImageOps.fit(toy_image, (600, 600))


        resized_toy_image.paste(shirt_image, (0, 0),shirt_image)
        resized_toy_image.save(f"{sys.argv[2]}")
    except FileNotFoundError:
        sys.exit("Input does not exist")
