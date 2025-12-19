# Crypto-Final-Project

This project demonstrates how secret messages can be hidden inside digital images using image steganography. The message is embedded into image pixels using the Least Significant Bit (LSB) technique, making the image appear unchanged to the human eye.

---

## 📂 Project Structure


Crypto-Final-Project/
├── main.py
├── steg_encode.py
├── steg_decode.py
├── images/
│ └── hidden_output.png


---

## ⚙️ How It Works
1. The secret message is converted into binary
2. Binary bits are stored in image pixel values
3. A special end marker is used to detect message completion
4. The decoding process retrieves the original text

---

## 🚀 Features
- Hide text inside images
- Extract hidden messages
- Simple command-line interface
- No visible image distortion

---

## 🛠 Requirements
- Python 3.10+
- Pillow library

Install Pillow:
```bash
pip install pillow

▶️ Usage
1️⃣ Run the Program
python main.py

2️⃣ Choose an Option

Option 1: Hide a secret message inside an image

Option 2: Extract a hidden message from an image

3️⃣ Follow the Prompts

Enter image path

Enter secret message (for encoding)

Enter output image name

🎓 Academic Purpose

This project was developed as part of a cryptography and security course to understand practical steganography techniques and hidden data communication.

⚠️ Limitations

No encryption applied to the message

Message size depends on image size

Detectable using advanced steganalysis tools

🔒 Future Improvements

Add encryption before embedding data

Password-protected decoding

Multi-channel (RGB) encoding

Graphical User Interface (GUI)

📜 License

This project is open-source and intended for educational use.