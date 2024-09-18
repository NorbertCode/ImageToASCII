import sys
from PIL import Image

def grayscale(rgb):
    if type(rgb) is int: # For single band images reverse the values, because then white returns 0
        return 255 - rgb
    elif len(rgb) > 3 and rgb[3] == 0: # If the pixel is transparent treat it like it's white
        return 255
    else: # Otherwise average the rgb values
        return sum(rgb[:3]) // 3

thresholdsPerChar = {
    255: " ",
    204: ".",
    153: "-",
    102: "/",
    51: "%",
    1: "@",
    0: "#"
}

if __name__ == "__main__":
    # Read the image
    imageName = ""
    if len(sys.argv) > 1: # So if there's an argument given
        imageName = sys.argv[1]
    else:
        imageName = input("Please enter image path: ")

    image = Image.open(imageName)
    imageSize = image.size

    # Iterate through all pixels
    for y in range(imageSize[1]):
        for x in range(imageSize[0]):
            for key, value in thresholdsPerChar.items():
                if grayscale(image.getpixel([x, y])) >= key: # Grayscale them and print the corresponding character
                    print(value, end='')
                    break
        print("\n", end='')
