import os
import lzma

def load_key_from_file(key_file):
    with open(key_file, 'rb') as keyfile:
        return bytearray(keyfile.read())

def chunk_text(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def decrypt_file(input_file, output_file, key_file, chunk_size=3):
    key = load_key_from_file(key_file)

    with open(input_file, 'rb') as infile:
        encrypted_data = infile.read()

    # Split the encrypted data and key into trigraphs
    encrypted_trigraphs = [encrypted_data[i:i + chunk_size] for i in range(0, len(encrypted_data), chunk_size)]
    key_trigraphs = [key[i:i + chunk_size] for i in range(0, len(key), chunk_size)]

    decrypted_data = bytearray((byte - key_byte) % 256 for trigraph, key_trigraph in zip(encrypted_trigraphs, key_trigraphs)
                               for byte, key_byte in zip(trigraph, key_trigraph))

    # Decompress using lzma
    decompressed_text = lzma.decompress(bytes(decrypted_data)).decode('utf-8')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(decompressed_text)

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_trigraph_lzma.txt")
    decrypted_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decrypted_output_lzma.txt")
    key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "key.bin")

    decrypt_file(input_file, decrypted_file, key_file)
    print(f"File '{input_file}' decrypted and saved to '{decrypted_file}'.")
