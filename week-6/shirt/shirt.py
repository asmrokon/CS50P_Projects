import sys
from PIL import Image, ImageOps


def main():
    format = ["png", "jpg", "jpeg"]
    try:
        if len(sys.argv) == 3:
            if all(arg.endswith(tuple(format)) for arg in sys.argv[1:]):
                name1, extension1 = sys.argv[1].split(".")
                name2, extension2 = sys.argv[2].split(".")
                if extension1 == extension2:
                    with Image.open(f"{sys.argv[1]}") as bg:
                        shirt = Image.open("shirt.png")
                        refined = ImageOps.fit(bg, shirt.size)
                        refined.paste(shirt, (0, 0), mask=shirt)
                        refined.save(f"{sys.argv[2]}")
                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            raise IndexError

    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("Input does not exist")


main()
