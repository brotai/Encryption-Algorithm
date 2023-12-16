import os
import lzma

def generate_one_time_pad(length):
    return bytearray(os.urandom(length))

def chunk_text(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def save_key_to_file(key, key_file):
    with open(key_file, 'wb') as keyfile:
        keyfile.write(bytes(key))

def encrypt_file(input_file, output_file, chunk_size=3):
    with open(input_file, 'r', encoding='utf-8') as infile:
        plaintext = infile.read()

    # Use lzma compression
    compressed_data = lzma.compress(plaintext.encode('utf-8'))
    one_time_pad = generate_one_time_pad(len(compressed_data))

    # Split the compressed data and one-time pad into trigraphs
    compressed_trigraphs = chunk_text(compressed_data, chunk_size)
    key_trigraphs = chunk_text(one_time_pad, chunk_size)

    encrypted_data = bytearray((byte + key_byte) % 256 for trigraph, key_trigraph in zip(compressed_trigraphs, key_trigraphs)
                               for byte, key_byte in zip(trigraph, key_trigraph))

    with open(output_file, 'wb') as outfile:
        outfile.write(bytes(encrypted_data))

    key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "key.bin")
    save_key_to_file(one_time_pad, key_file)
    print(f"File '{input_file}' encrypted and saved to '{output_file}'.")
    print(f"One-time pad key saved to '{key_file}'.")

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text.txt")
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_trigraph_lzma.txt")

    encrypt_file(input_file, output_file)
