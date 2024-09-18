import sys
import generator

if __name__ == "__main__":
    # Read the image
    imageName = ""
    if len(sys.argv) > 1:  # So if there's an argument given
        imageName = sys.argv[1]
    else:
        imageName = input("Please enter image path: ")

    print(generator.generate(imageName))
