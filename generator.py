from PIL import Image

thresholdsPerChar = {
    255: " ",
    204: ".",
    153: "-",
    102: "/",
    51: "%",
    1: "@",
    0: "#"
}

def grayscale(rgb):
    if type(rgb) is int: # For single band images reverse the values, because then white returns 0
        return 255 - rgb
    elif len(rgb) > 3 and rgb[3] == 0: # If the pixel is transparent treat it like it's white
        return 255
    else: # Otherwise average the rgb values
        return sum(rgb[:3]) // 3

def generate(imageName):
    image = Image.open(imageName)
    imageSize = image.size

    # Iterate through all pixels
    output = ""
    for y in range(imageSize[1]):
        for x in range(imageSize[0]):
            for key, value in thresholdsPerChar.items():
                if grayscale(image.getpixel([x, y])) >= key: # Grayscale them and print the corresponding character
                    output += value
                    break
        output += "\n"
    return output
