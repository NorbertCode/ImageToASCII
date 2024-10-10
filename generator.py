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

def handle_exceptions(rgb):
    if type(rgb) is int: # For single band images reverse the values, because then white returns 0
        return 255 - rgb
    elif len(rgb) > 3 and rgb[3] == 0: # If the pixel is transparent treat it like it's white
        return 255
    else:
        return None

def average_method_grayscale(rgb):
    temp = handle_exceptions(rgb)
    if temp != None: return temp

    return sum(rgb[:3]) // 3
    
def luminosity_method_grayscale(rgb):
    temp = handle_exceptions(rgb)
    if temp != None: return temp
    
    return int(0.21 * rgb[0] + 0.72 * rgb[1] + 0.07 * rgb[2])

methods = {
    "average": average_method_grayscale,
    "luminosity": luminosity_method_grayscale
}

def generate(imageName, method="average"):
    image = Image.open(imageName)
    imageSize = image.size

    # Iterate through all pixels
    output = ""
    for y in range(imageSize[1]):
        for x in range(imageSize[0]):
            for key, value in thresholdsPerChar.items():
                if methods[method](image.getpixel([x, y])) >= key: # Grayscale them and print the corresponding character
                    output += value
                    break
        output += "\n"
    return output
