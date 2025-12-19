from PIL import Image

def hide_text(image_path, secret_text, save_path):
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    secret_text += "|STOP|"
    binary_text = ''.join(format(ord(c), '08b') for c in secret_text)

    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(binary_text):
                r, g, b = pixels[x, y]
                r = (r & 254) | int(binary_text[index])
                pixels[x, y] = (r, g, b)
                index += 1
            else:
                image.save(save_path)
                print("✔ Message hidden successfully.")
                return

    print("❌ Image too small for the message.")
