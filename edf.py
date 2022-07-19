'''
Programmer: Abhinav Sharma
This is just an exploratory project to explore cryptography
'''

'''File Encryptor '''

import hashlib
from cryptography.fernet import Fernet
import rsa
from morse_char_dict import morse_char_dict
from char_dict import char_dict

def main():
    print("Welcome to the File Encryption Project!!!")

    e_or_d = -1
    while (e_or_d != 0):
        
        e_or_d = int(input("Enter 1 for encryption and 2 for decryption. Enter 0 to exit: "))

        if (e_or_d == 0):
            break
        elif (e_or_d == 1):
            encrypter()
        elif (e_or_d == 2):
            decrypter()        

def encrypter():
    en_ch = int(input("Press:\n1: Morse Code\n2:SHA256\n3:Fernet:\n4:RSA\n\nEnter choice:-"))

    if (en_ch == 1):
        
        iofname = input("Enter name of input file: ")
        iof = open(iofname, "r")
        oofname = input("Enter name of output file: ")
        oof = open(oofname, "w")

        sentences = iof.read()
        sentences = sentences.upper()
        morse_word = morse_lookup(sentences)
        oof.write(morse_word)

        iof.close()
        oof.close()

    elif (en_ch == 2):

        iofname = input("Enter name of input file: ")
        iof = open(iofname, "r")
        oofname = input("Enter name of output file: ")
        oof = open(oofname, "w")
        
        sha_input_text = iof.read() 
        sha_output_text = sha_encrypt(sha_input_text)
        oof.write(sha_output_text)

        iof.close()
        oof.close()

    elif (en_ch == 3):

        key = Fernet.generate_key()
        
        name = input("Enter name of file where you wish to store key(without extensions): ")
        fname = name + ".key"
        file = open(fname, 'wb')
        file.write(key)
        file.close()

        iofname = input("Enter name of input file: ")
        iof = open(iofname, 'r')
        oofname = input("Enter name of output file: ")
        oof = open(oofname, 'wb')

        fernet_encrypt(iof, oof, key)
        iof.close()
        oof.close()

    elif (en_ch == 4):

        iofname = input("Enter name of input file: ")
        iof = open(iofname, "r")
        oofname = input("Enter name of output file: ")
        oof = open(oofname, "wb")

        publicKey, privateKey = rsa.newkeys(1024)
        
        with open('public_key.pem', 'wb') as f:
            f.write(publicKey.save_pkcs1('PEM'))

        with open('private_key.pem', 'wb') as f:
            f.write(privateKey.save_pkcs1('PEM'))

        print(f"Public key is stored in: public_key.pem and Private key is stored in private_key.pem")

        rsa_input_text = iof.read()
        rsa_output_text = rsa_encrypt(rsa_input_text, publicKey)
        oof.write(rsa_output_text)

        iof.close()
        oof.close()

def decrypter():
    de_ch = int(input("Press:\n1: Morse Code\n2:Fernet:\n3:RSA\n\nEnter choice:-"))

    if (de_ch == 1): 
        
        iofname = input("Enter name of input file: ")
        iof = open(iofname, "r")
        oofname = input("Enter name of output file: ")
        oof = open(oofname, "w")

        morse_sentences = iof.read()
        normal_word = normal_lookup(morse_sentences)
        oof.write(normal_word)

        iof.close()
        oof.close()

    elif (de_ch == 2):
        
        norm_key_file = input("Enter the file containing the key: ")
        file = open(norm_key_file, 'rb')
        norm_key = file.read()
        file.close()

        iofname = input("Enter name of input file: ")
        iof = open(iofname, 'rb')
        oofname = input("Enter name of output file: ")
        oof = open(oofname, 'w')

        norm_fern_input_text = iof.read()
        norm_fern_output_text = fernet_decrypt(norm_fern_input_text, norm_key)
        oof.write(norm_fern_output_text)

        iof.close()
        oof.close()

    elif (de_ch == 3):

        iofname = input("Enter name of input file: ")
        iof = open(iofname, "rb")
        oofname = input("Enter name of output file: ")
        oof = open(oofname, "w")

        privateKeyRSAFile = input("Enter file containing Private Key used to encrypt file: ")
        with open(privateKeyRSAFile, 'rb') as f:
            norm_privateKey = rsa.PrivateKey.load_pkcs1(f.read())
            
        norm_rsa_input_text = iof.read()
        norm_rsa_output_text = rsa_decrypt(norm_rsa_input_text, norm_privateKey)
        oof.write(norm_rsa_output_text)   

        iof.close()
        oof.close() 

def morse_lookup(a):

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
        
        fernet = Fernet(key)
        fernet_input_text = iof.read()
        fernet_output_text = fernet.encrypt(fernet_input_text.encode())
        oof.write(fernet_output_text)

def fernet_decrypt(input_text, key):
    fernet = Fernet(key)
    f_decrypt = fernet.decrypt(input_text).decode()
    return f_decrypt

def rsa_encrypt(rsa_input_text, publicKey):
    
    rsa_encrypted = rsa.encrypt(rsa_input_text.encode('ascii'), publicKey)
    return rsa_encrypted

def rsa_decrypt(norm_rsa_input_text, privateKey):

    rsa_decrypted = rsa.decrypt(norm_rsa_input_text, privateKey).decode('ascii')
    return rsa_decrypted
class edf:
    def __init__(self):
        self.main()