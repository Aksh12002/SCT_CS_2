from PIL import Image
import numpy as np
import os
import random

INPUT_DIR = "input_image"
OUTPUT_DIR = "output_image"


def ensure_dirs():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def encrypt_image(image_name, key):
    ensure_dirs()

    img = Image.open(os.path.join(INPUT_DIR, image_name)).convert("RGB")
    data = np.array(img)
    h, w, c = data.shape

    flat = data.reshape(-1, 3)

    # Key-based shuffle
    random.seed(key)
    indices = list(range(len(flat)))
    random.shuffle(indices)
    shuffled = flat[indices]

    # XOR encryption with key
    encrypted = shuffled ^ (key % 256)

    encrypted_img = encrypted.reshape(h, w, 3)
    out_path = os.path.join(OUTPUT_DIR, "encrypted_" + image_name)
    Image.fromarray(encrypted_img.astype("uint8")).save(out_path)

    return out_path


def decrypt_image(image_name, key):
    ensure_dirs()

    img = Image.open(os.path.join(INPUT_DIR, image_name)).convert("RGB")
    data = np.array(img)
    h, w, c = data.shape

    flat = data.reshape(-1, 3)

    # Reverse XOR
    unxor = flat ^ (key % 256)

    # Reverse shuffle
    random.seed(key)
    indices = list(range(len(unxor)))
    random.shuffle(indices)

    original = np.zeros_like(unxor)
    for i, idx in enumerate(indices):
        original[idx] = unxor[i]

    decrypted_img = original.reshape(h, w, 3)
    out_path = os.path.join(OUTPUT_DIR, "decrypted_" + image_name)
    Image.fromarray(decrypted_img.astype("uint8")).save(out_path)

    return out_path
