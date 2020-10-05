import PIL.Image


def main(new_width=100):
    path = input("enter relative image path:\n")

    image = load_image(path)
    resized = resize(image)
    greyscaled = greyscale(resized)
    ascii_image_data = pixel_to_ascii(greyscaled)
    ascii_image = image_to_ascii(ascii_image_data, new_width)

    save_to_txt(ascii_image)


def load_image(path):
    try:
        image = PIL.Image.open(path)
    except:
        image = ""
        print(path, "is not a valid image")
    return image


def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def greyscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixel_to_ascii(image):
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    pixels = image.getdata()
    chars = "".join([ascii_chars[pixel // 25] for pixel in pixels])
    return chars


def image_to_ascii(ascii_image_data, new_width):
    pixel_count = len(ascii_image_data)
    ascii_image = "\n".join(ascii_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    print(ascii_image)
    return ascii_image


def save_to_txt(ascii_image):
    with open("output/ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()
