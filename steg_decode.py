from PIL import Image

def reveal_text(image_path):
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    bits = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)

    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        char = chr(int(byte, 2))
        message += char
        if message.endswith("|STOP|"):
            return message.replace("|STOP|", "")

    return "No hidden message found."
