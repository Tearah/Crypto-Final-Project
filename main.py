from steg_encode import hide_text
from steg_decode import reveal_text

def show_menu():
    print("\n===== Image Steganography System =====")
    print("1. Hide secret message")
    print("2. Extract secret message")
    print("=====================================")

def main():
    show_menu()
    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        image_path = input("Enter image path: ")
        secret = input("Enter secret message: ")
        output = input("Enter output image name: ")
        hide_text(image_path, secret, output)

    elif choice == "2":
        image_path = input("Enter encoded image path: ")
        message = reveal_text(image_path)
        print("\nHidden message:", message)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
