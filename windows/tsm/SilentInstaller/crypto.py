from cryptography.fernet import Fernet
import argparse, os, json

def write_key(output):
    key = Fernet.generate_key()
    with open(output, "wb") as key_file:
        key_file.write(key)

def load_key(file):
    return open(file, "rb").read()

def encrypt(key, input, output):
    f = Fernet(key)

    with open(input, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)

    with open(output, 'wb') as file:
        file.write(encrypted_data)

def decrypt(key, input, output=None):
    f = Fernet(key)

    with open(input, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    if output is not None:
        with open(output, 'wb') as file:
            file.write(decrypted_data)
