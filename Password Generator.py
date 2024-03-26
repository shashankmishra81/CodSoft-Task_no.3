import random, string
from tkinter import *
import pyperclip
 
 
#Initialize Window
 
root =Tk()
root.geometry("400x400") #size of the window by default
 
#Title of our window
root.title("Password Generator")
 
# -------------------  Random Password generator function
 
output_pass = StringVar()
 
combination = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters
 
def random_password():
    password = "" # to store password
    for y in range(Length.get()):
        char_type = random.choice(combination)   #to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)
     
    output_pass.set(password)
 
# ----------- Copy to clipboard function
 
def copyPass():
    pyperclip.copy(output_pass.get())
 
#-----------------------Front-end Designing (GUI)
 
pass_head = Label(root, text = 'Password Length', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
Length = IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(root, from_ = 4, to = 32 , textvariable = Length, width = 24, font='Segoe_UI').pack()
 
#Generate password button
 
Button(root, command = random_password, text = "Generate Password", font="Segoe_UI", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
pass_label = Label(root, text = 'Generated Password', font = 'Segoe_UI').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, font='Segoe_UI').pack()
 
#Copy to clipboard button
 
Button(root, text = 'Copy to Clipboard', command = copyPass, font="Segoe_UI", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
root.mainloop() 