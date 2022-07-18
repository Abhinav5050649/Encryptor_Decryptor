'''
Programmer: Abhinav Sharma
This is just an exploratory project to explore cryptography
'''
'''CLI Based Encryptor Decryptor'''

import hashlib
from cryptography.fernet import Fernet
import rsa
from morse_char_dict import morse_char_dict
from char_dict import char_dict

rsa_publicKey, rsa_privateKey, ferNet_Key = "", "", ""

def main():
    print("Welcome to the Encryption-Decryption Project!!!")

    e_or_d = -1
    while (e_or_d != 0):
        e_or_d = int(input("Enter 1 for encryption and 2 for decryption. Enter 0 to exit: "))

        if (e_or_d == 1):
            encrypter()
        elif (e_or_d == 2):
            decrypter()        

def encrypter():
    en_ch = int(input("Press:\n1: Morse Code\n2:SHA256\n3:Fernet:\n4:RSA\n\nEnter choice:-"))

    if (en_ch == 1):

        sentences = input("Enter a string: ")
        sentences = sentences.upper()
        morse_word = morse_lookup(sentences)
        print(morse_word)

    elif (en_ch == 2):

        sha_input_text = input("Enter string you wish to encrypt using SHA256 algorithm: ")
        sha_output_text = sha_encrypt(sha_input_text)
        print(sha_output_text)

    elif (en_ch == 3):

        fernet_input_text = input("Enter string you wish to encrypt using Fernet: ")
        fernet_output_text = fernet_encrypt(fernet_input_text)
        print("Enrypted Text: ")
        print(fernet_output_text)

    elif (en_ch == 4):
        
        rsa_input_text = input("Enter string you wish to encrypt using RSA:")
        print("\n\n")
        length = int(input("Enter length of rsa keys (Minimum length = 16): "))
        publicKey, privateKey = rsa.newkeys(length)     
        rsa_publicKey, rsa_privateKey = publicKey, privateKey
        rsa_output_text = rsa_encrypt(rsa_input_text, publicKey)
        print("Encrypted Text: ")
        print(rsa_output_text)

def decrypter():
    de_ch = int(input("Press:\n1: Morse Code\n2:Fernet:\n3:RSA\n\nEnter choice:-"))

    if (de_ch == 1): 
        morse_sentences = input("Enter string in Morse Code: ")
        morse_sentences = morse_sentences.upper()
        normal_word = normal_lookup(morse_sentences)
        print(normal_word)

    elif (de_ch == 2):
        norm_fern_input_text = input("Enter string you wish to decrypt using Fernet: ")
        bytes(norm_fern_input_text, 'utf-8')
        norm_key_file = input("Enter file in which key is stored: ")
        norm_fern_output_text = fernet_decrypt(norm_fern_input_text, norm_key_file)
        print("Decrypted Text: ")
        print(norm_fern_output_text)

    elif (de_ch == 3):
        question = input("Have you used this program to encrypt a string using RSA before?[Y/N]: ")
        
        if (question == 'Y'):
            norm_rsa_input_text = input("Enter string you wish to decrypt using RSA: ")
            norm_privateKey = input("Enter private key of RSA: ")
            if (norm_privateKey == rsa_privateKey):
                norm_rsa_output_text = rsa_decrypt(norm_rsa_input_text, norm_privateKey)
                print("Decrypted Text: ")
                print(norm_rsa_output_text)
            else:
                print("Wrong RSA private key!!!")    
        else:
            print("You MUST first use this program to ENCRYPT a string using RSA before trying to decrypt the string!!!")

def morse_lookup(a):
   
    morse_chars = ""
    for i in range(len(a)):
        if (a[i] != '\n'):
            morse_chars += morse_char_dict[a[i]]
        else:
            morse_chars += a[i]

    return morse_chars

def normal_lookup(a):

    chars = ""
    a = a.split()
    for i in range(len(a)):
        temp_char = ""
        if (a[i] != '\n'):
            temp_char += a[i]
            chars += char_dict[temp_char]
        elif (a[i] == '\n'):
            chars += a[i]

    return chars
    
def sha_encrypt(sha_input):
    encrypted = hashlib.sha256(sha_input.encode('utf-8')).hexdigest()
    return encrypted

"""Need to resolve Fernet Issues"""
def fernet_encrypt(input_text):
    
    key = Fernet.generate_key()
    filename = input("Enter name of file in which you want to store the key(without any extensions): ")
    fname = filename + '.key'
    file = open(fname, 'wb')
    file.write(key)
    file.close()
    fernet = Fernet(key)
    encoded = input_text.encode()
    f_encrypted = fernet.encrypt(encoded)
    return f_encrypted

'''Resolve decryption based on CLI'''
def fernet_decrypt(input_text, norm_key_file):
    file = open(norm_key_file, 'rb')
    key2 = file.read()
    file.close()
    fernet = Fernet(key2)
    f_decrypt = fernet.decrypt(input_text)
    fd = f_decrypt.decode()
    return fd

"""Need to resolve OverflowError of messages"""
def rsa_encrypt(rsa_input_text, publicKey):
    rsa_encrypted = rsa.encrypt(rsa_input_text.encode(), publicKey)
    return rsa_encrypted

def rsa_decrypt(norm_rsa_input_text, privateKey):
    rsa_decrypted = rsa.decrypt(norm_rsa_input_text, privateKey).decode()
    return rsa_decrypted

main()