from PIL import Image

# Function to encrypt image using XOR operation
def encrypt_image(image, key):
    encrypted_image = Image.new(image.mode, image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple([(p ^ key) for p in pixel])
            encrypted_image.putpixel((x, y), encrypted_pixel)

    return encrypted_image

# Function to decrypt image using XOR operation
def decrypt_image(image, key):
    decrypted_image = Image.new(image.mode, image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            decrypted_pixel = tuple([(p ^ key) for p in pixel])
            decrypted_image.putpixel((x, y), decrypted_pixel)

    return decrypted_image

# Load an image
image_path = "vegita.jpg"
im = Image.open(image_path)

# Define encryption key
encryption_key = 128

# Encrypt the image
encrypted_im = encrypt_image(im, encryption_key)
encrypted_im.save("encrypted_image.jpg")

# Decrypt the image
decrypted_im = decrypt_image(encrypted_im, encryption_key)
decrypted_im.save("decrypted_image.jpg")

print("Pixel manipulation for image encryption completed.")