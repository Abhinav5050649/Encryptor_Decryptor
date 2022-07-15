'''
Programmer: Abhinav Sharma
This is just an exploratory project to explore cryptography
'''
'''CLI Based Encryptor Decryptor'''

import hashlib
from cryptography.fernet import Fernet
import rsa

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
        rsa_privateKey = privateKey
        rsa_publicKey = publicKey        
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
        norm_key = input("Enter the key: ")
        norm_fern_output_text = fernet_decrypt(norm_fern_input_text, norm_key)
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
    morse_char_dict = {
        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        '0': '----- ',
        ' ': '/ ',
        '.': '.-.-.- ',
        ',': '--..-- ',
        '?': '..--.. ',
        "'": '.----. ',
        '!': '-.-.-- ',
        '/': '-..-. ',
        '(': '-.--. ',
        ')': '-.--.- ',
        '&': '.-... ',
        ':': '---... ',
        ';': '-.-.-. ',
        '=': '-...- ',
        '+': '.-.-. ',
        '-': '-....- ',
        '_': '..--.- ',
        '"': '.-..-. ',
        '$': '...-..- ',
        '@': '.--.-. ',
        '¿': '..-.- ',
        '¡': '--...- ',
    }

    morse_chars = ""
    for i in range(len(a)):
        if (a[i] != '\n'):
            morse_chars += morse_char_dict[a[i]]
        else:
            morse_chars += a[i]

    return morse_chars

def normal_lookup(a):
    char_dict = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...' :'7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '/': ' ',
        '.-.-.-': '.',
        '--..--': ',',
        '..--..': '?',
        '.----.': '"',
        '-.-.--': '!',
        '-..-.': '/',
        '-.--.': '(',
        '-.--.-': ')',
        '.-...': '&',
        '---...': ':',
        '-.-.-.': ';',
        '-...-': '=',
        '.-.-.': '+',
        '-....-': '-',
        '..--.-': '_',
        '.-..-.': '"',
        '...-..-': '$',
        '.--.-.': '@',
        '..-.-': '¿',
        '--...-': '¡',
    }

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
    choice = input("Press Y if you want fernet to generate key. Else, press N if you want to generate key: ")

    if (choice == 'Y'):
        key = Fernet.generate_key()
        print("Your fernet key(remember this!!!) is: ", key)
        fernet = Fernet(key)
        f_encrypted = fernet.encrypt(input_text.encode())
        return f_encrypted
    else:
        key = input("Enter key: ")
        fernet = Fernet(key)
        f_encrypted = fernet.encrypt(input_text.encode())
        return f_encrypted

def fernet_decrypt(input_text, key):
    fernet = Fernet(key)
    f_decrypt = fernet.decrypt(input_text).decode()
    return f_decrypt

"""Need to resolve OverflowError of messages"""
def rsa_encrypt(rsa_input_text, publicKey):
    rsa_encrypted = rsa.encrypt(rsa_input_text.encode(), publicKey)
    return rsa_encrypted

def rsa_decrypt(norm_rsa_input_text, privateKey):
    rsa_decrypted = rsa.decrypt(norm_rsa_input_text, privateKey).decode()
    return rsa_decrypted
class edcli:
    def __init__(self):
        self.main()