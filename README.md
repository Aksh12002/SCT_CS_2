# 🖼️ Task 02 – Image Encryption Using Pixel Manipulation

## 📌 Overview
This project is developed as **Task 02** of the **Cyber Security Internship**.  
It implements a **strong image encryption and decryption system** using **pixel manipulation techniques** combined with **key-based scrambling**.

The objective of this task is to demonstrate how image data can be protected by modifying both:
- Pixel values, and
- Pixel positions

---

## 🎯 Objectives
- Understand how images are stored as pixel data
- Implement reversible image encryption
- Improve encryption strength beyond basic pixel XOR
- Use a secret key to control encryption and decryption
- Build a safe, ethical, and internship-appropriate security project

---

## 🔐 Encryption Technique Used

### 🔒 Enhanced Pixel-Based Image Encryption
This project uses a **multi-layer encryption approach**:

1. **Pixel Value Encryption**
   - Each pixel’s RGB values are encrypted using XOR with a secret key

2. **Pixel Position Scrambling**
   - All pixels are shuffled using a key-based random sequence
   - This removes visible image patterns and structure

3. **Key-Based Deterministic Decryption**
   - Using the same key restores both pixel values and positions
   - Without the correct key, decryption is impossible

This approach makes the encrypted image **visually unrecognizable** and significantly more secure than simple XOR encryption.

---

## 🧱 Project Structure
```

SCT_CS_2/
│
├── main.py                     # Menu-driven main program
├── strong_image_cipher.py      # Strong image encryption logic
│
├── input_image/
│   └── sample.png              # Original image
│
└── output_image/
├── encrypted_sample.png    # Encrypted image
└── decrypted_sample.png    # Decrypted image

````

---

## 🛠 Technologies Used
- Python 3
- Pillow (PIL)
- NumPy
- Standard Python libraries

---

## ⚙ Installation & Setup

### 🔹 Step 1: Install Required Libraries
```bash
python -m pip install pillow numpy
````

Verify installation:

```bash
python -c "from PIL import Image; import numpy; print('OK')"
```

---

### 🔹 Step 2: Run the Program

```bash
python main.py
```

---

## ▶ How to Use

### 🔐 Encrypt an Image

1. Place an image inside the `input_image` folder
2. Run the program
3. Choose **Encrypt Image**
4. Enter a numeric secret key
5. Encrypted image is saved in `output_image`

---

### 🔓 Decrypt an Image

1. Place the encrypted image back into the `input_image` folder
2. Choose **Decrypt Image**
3. Enter the **same secret key**
4. Original image is restored

⚠ Using an incorrect key will not restore the image.

---

## 🔒 Security Notes

* Pixel scrambling removes visible patterns from encrypted images
* Encryption is fully reversible only with the correct key
* This method is designed for **educational purposes**
* It demonstrates the importance of both **data and positional encryption**

