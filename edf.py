'''
Programmer: Abhinav Sharma
This is just an exploratory project to explore cryptography
'''

'''File Encryptor '''

import hashlib
from cryptography.fernet import Fernet
import rsa

def main():
    print("Welcome to the File Encryption Project!!!")

    e_or_d = -1
    while (e_or_d != 0):
        
        e_or_d = int(input("Enter 1 for encryption and 2 for decryption. Enter 0 to exit: "))

        if (e_or_d == 0):
            break
        # e_or_d = int(input("Press 1 to continue. Press 0 to exit"))
        iofname = input("Enter name of input file: ")
        iof = open(iofname, "r")
        oofname = input("Enter name of output file: ")
        oof = open(oofname, "w")
        
        # encrypter(iof, oof)

        # e_or_d = int(input("Press 1 to continue. Press 0 to exit"))

        if (e_or_d == 1):
            encrypter(iof, oof)
        elif (e_or_d == 2):
            decrypter(iof, oof)        

def encrypter(iof, oof):
    en_ch = int(input("Press:\n1: Morse Code\n2:SHA256\n3:Fernet:\n4:RSA\n\nEnter choice:-"))

    if (en_ch == 1):
        
        for sentences in iof:
            sentences = sentences.upper()
            morse_word = morse_lookup(sentences)
            oof.write(morse_word)

    elif (en_ch == 2):
        for sha_input_text in iof:
            sha_output_text = sha_encrypt(sha_input_text)
            oof.write(sha_output_text)

    elif (en_ch == 3):
        choice = input("Press Y if you want fernet to generate key. Else, press N if you want to generate key: ")

        if (choice == 'Y'):
            key = Fernet.generate_key()
            print("Your fernet key(remember this!!!) is: ", key)
        else:
            key = input("Enter key: ")
        
        fernet_encrypt(iof, oof, key)

    elif (en_ch == 4):
        length = int(input("Enter length of rsa keys (Minimum length = 16): "))
        publicKey, privateKey = rsa.newKeys(length)
        
        print("Remember the following keys:\nRSA Public Key: ", publicKey, "\nRSA Private Key: ", privateKey, "\n")
        for rsa_input_text in iof:
            rsa_output_text = rsa_encrypt(rsa_input_text, publicKey)
            oof.write(rsa_output_text)

def decrypter(iof, oof):
    de_ch = int(input("Press:\n1: Morse Code\n2:Fernet:\n3:RSA\n\nEnter choice:-"))

    if (de_ch == 1): 
        
        for morse_sentences in iof:
            normal_word = normal_lookup(morse_sentences)
            oof.write(normal_word)

    elif (de_ch == 2):
        
        norm_key = input("Enter the key: ")
        
        for norm_fern_input_text in iof:
            norm_fern_output_text = fernet_decrypt(norm_fern_input_text, norm_key)
            oof.write(norm_fern_output_text)

    elif (de_ch == 3):

        norm_privateKey = input("Enter private key of RSA: ")
        
        for norm_rsa_input_text in iof:
            norm_rsa_output_text = rsa_decrypt(norm_rsa_input_text, norm_privateKey)
            oof.write(norm_rsa_output_text)    

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
        "\n": '..........---------- '
    }

    not_doubtful_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@', '¿', '¡', "\n"]
    
    morse_chars = ""
    for i in range(len(a)):
        if (a[i] in not_doubtful_chars):
            morse_chars += morse_char_dict[a[i]]
        else:
            morse_chars += a[i] + " "
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
        '..........----------' : '\n',
    }

    not_doubtful_chars = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
    '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '/', '-----', '.-.-.-',
    '--..--', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-',
    '.-..-.', '...-..-', '.--.-.', '..-.-', '--...-', '..........----------']
    chars = ""
    a = a.split()
    for i in range(len(a)):
            temp_char = ""
            if (a[i] in not_doubtful_chars):
                temp_char += a[i]
                chars += char_dict[temp_char]
            else:
                chars += a[i]
                
    return chars
    
def sha_encrypt(sha_input):
    encrypted = hashlib.sha256(sha_input.encode('utf-8')).hexdigest()
    return encrypted

def fernet_encrypt(iof, oof, key):
        # f_encrypted = fernet.encrypt(input_text.encode())
        # return f_encrypted
        
        fernet = Fernet(key)
        for fernet_input_text in iof:
            fernet_output_text = fernet.encrypt(fernet_input_text.encode())
            oof.write(fernet_output_text)

def fernet_decrypt(input_text, key):
    fernet = Fernet(key)
    f_decrypt = fernet.decrypt(input_text).decode()
    return f_decrypt

def rsa_encrypt(rsa_input_text, publicKey):
    
    rsa_encrypted = rsa.encrypt(rsa_input_text.encode(), publicKey)
    return rsa_encrypted

def rsa_decrypt(norm_rsa_input_text, privateKey):
    rsa_decrypted = rsa.decrypt(norm_rsa_input_text, privateKey).decode()
    return rsa_decrypted

main()