from Crypto.Cipher import AES,DES
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad, unpad
import os


#fonction pour chiffrer un fichier avc AES
def encrypt_file_aes(file_path, key):
     cipher=AES.new(key, AES.MODE_ECB)
     with open(file_path, "rb") as file:
        plaintext=file.read()
        ciphertext=cipher.encrypt(pad(plaintext,AES.block_size))
        with open(file_path +".enc", "wb") as file:
         file.write(ciphertext)

#fonction pour dechiffrer un fichier avc AES
def decrypt_file_aes(file_path, key):
     cipher=AES.new(key, AES.MODE_ECB)
     with open(file_path, "rb") as file:
        ciphertext=file.read()
        plaintext=unpad(cipher.decrypt(ciphertext),AES.block_size)
     with open(file_path[:-4], "wb") as file:
         file.write(plaintext)

#fonction pour chiffrer un fichier avc DES
def encrypt_file_des(file_path, key):
     cipher=DES.new(key, DES.MODE_ECB)
     with open(file_path, "rb") as file:
        plaintext=file.read()
        ciphertext=cipher.encrypt(pad(plaintext,DES.block_size))
        with open(file_path +".enc", "wb") as file:
         file.write(ciphertext)

#fonction pour dechiffrer un fichier avc DES
def decrypt_file_des(file_path, key):
     cipher=DES.new(key, DES.MODE_ECB)
     with open(file_path, "rb") as file:
        ciphertext=file.read()
        plaintext=unpad(cipher.decrypt(ciphertext),DES.block_size)
     with open(file_path[:-4], "wb") as file:
         file.write(plaintext)


#fonction pour echanger des fichiers de maniere securisee
def secure_file_exchange():
    while  True:
        print("==echange de fichier securise==")
        print("1.chiffrer un fichier avec AES")
        print("2.dechiffrer un fichier avec AES")
        print("3.chiffrer un fichier avec DES")
        print("4.dechiffrer un fichier avec DES")
        print("5.quitter")


        choice=input("votre choix :")

        if choice== "1":
            file_path=input("chemin vers le fichier a chiffrer: ")
            key=get_random_bytes(16) #generer une cle AES de 16octets
            encrypt_file_aes(file_path, key)
            print("fichier chiffrer avec succes")
            print("cle de chiffrerement:", key.hex())
        elif choice=="2":
            file_path=input("chemin vers le fichier a dechiffrer: ")
            key=bytes.fromhex(input("cle de chiffrement: "))
            decrypt_file_aes(file_path, key)
            print("fichier dechiffrer avec succes")
        elif choice=="3":
            file_path=input("chemin vers le fichier a chiffrer: ")
            key=get_random_bytes(8) #generer une cle DES de 8octets
            encrypt_file_des(file_path, key)
            print("fichier chiffrer avec succes")
            print("cle de chiffrerement:", key.hex())
        elif choice=="4":
            file_path=input("chemin vers le fichier a dechiffrer: ")
            key=bytes.fromhex(input("cle de chiffrement: "))
            decrypt_file_des(file_path, key)
            print("fichier dechiffrer avec succes")
        elif choice==("5"):
            print("quitter")
            break
        else: 
            print("Sorry choix invalide.")

#execution de l'application
if_name_=="_main_":secure_file_exchange()