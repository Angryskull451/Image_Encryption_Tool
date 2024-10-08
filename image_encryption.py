from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Load the image
    image = Image.open(input_image_path)
    data = np.array(image)

    # Apply a simple encryption method by shifting pixel values
    encrypted_data = (data + key) % 256  # Wrap around at 256 for pixel values

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Load the encrypted image
    encrypted_image = Image.open(input_image_path)
    data = np.array(encrypted_image)

    # Decrypt by reversing the encryption process
    decrypted_data = (data - key) % 256  # Wrap around at 256 for pixel values

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Example usage
encrypt_image('input_image.png', 'encrypted_image.png', 50)  # Replace with your image path and key
decrypt_image('encrypted_image.png', 'decrypted_image.png', 50)  # Replace with your encrypted image path and key

