from tkinter import *
from tkinter import ttk

from click import command
import edcli
import edf


from rsa import encrypt

def encryptKaro():
    edcli.main

def decryptKaro():
    edf.main
    
root=Tk()
root.title("Security")

encrypt=ttk.Label(root,text="     Encrypt  ")
encrypt.grid(row=3,column=0,sticky='snew',ipadx=60,ipady=40)
encryptBTN=ttk.Button(root,text="         Encrypt  ",command=encryptKaro())
encryptBTN.grid(row=4,column=0,sticky='snew',ipadx=10,ipady=20)

decrypt=ttk.Label(root,text="       Decrypt     ")
decrypt.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)
decryptBTN=ttk.Button(root,text="    Decrypt     ",command=decryptKaro())
decryptBTN.grid(row=4,column=2,sticky='snew',ipadx=10,ipady=20)


res=ttk.Button(root,text='Quit',command=root.quit)
res.grid(row=5,column=1,sticky='snew',ipadx=10,ipady=20)





root.mainloop()