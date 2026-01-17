from strong_image_cipher import encrypt_image, decrypt_image


def get_key():
    while True:
        try:
            return int(input("Enter secret key (number): "))
        except ValueError:
            print("❌ Enter a valid number")


def main():
    while True:
        print("\n🔐 STRONG IMAGE ENCRYPTION TOOL")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("Choose (1/2/3): ")

        if choice in ["1", "2"]:
            image_name = input("Image filename: ")
            key = get_key()

            try:
                if choice == "1":
                    out = encrypt_image(image_name, key)
                else:
                    out = decrypt_image(image_name, key)

                print(f"✅ Output saved at: {out}")

            except Exception as e:
                print("❌ Error:", e)

        elif choice == "3":
            print("👋 Exiting")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
