from tkinter import *

#consts to change grid row and columns quicker
#nm..........lol
rot13 = "global"

#caesar encode function
def caesarencode():  #need to define
    inpValue = int(txtentrybox3.get())
    if inpValue < 1 and inpValue > 13:
        inpValue = 9
        rot13 = 9
        int(rot13)
    else:
        rot13 = inpValue
        int(rot13)
        inpMessage = txtentrybox1.get()  #get text from txtentrybox1
        txtentrybox1.delete(0, END)      #clear the text box
        codedMessage = ""
        for ch in inpMessage:  #<-------Need to figure out how to handle capitals
            if ch == " ":
                codedMessage += " "
            else:
                codedMessage += chr((ord(ch) - 97 + inpValue) % 26 + 97)
        txtoutputbox1.insert(0, codedMessage)  #retrun message to output text box

#caesar decode function
def caesardecode():
    inpValue = int(txtentrybox3.get())
    int(inpValue)
    if inpValue < 1 and inpValue > 13:
        inpValue = 9
        rot13 = 9
        int(rot13)
    else:
        inpMessage = txtoutputbox1.get()  #get text from txtoutputbox1
        txtoutputbox1.delete(0, END)      #clear the text box
        decodedMessage = ""
        for ch in inpMessage:   #<-------Need to figure out how to handle capitals
            if ch == " ":
                decodedMessage += " "
            else:
                decodedMessage += chr((ord(ch) - 97 - inpValue) % 26 + 97)
        txtentrybox1.insert(0, decodedMessage)
    
# This function returns the  
# encrypted text generated  
# with the help of the key 
def vigenereencode():
    #def cipherText(string, key):
    key = txtentrybox4.get()
    string = txtentrybox2.get() 
    txtentrybox2.delete(0, END)      #clear the text box
    cipher_text = "" 
    for i in range(len(string)): 
        if i == " ":
            cipher_text += " "
        else:
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A') 
        cipher_text += chr(x) 
    txtoutputbox2.insert(0, cipher_text)  #return message to output text box
    #return("" . join(cipher_text)) 

      
# This function decrypts the  
# encrypted text and returns  
# the original text 
def vigeneredecode(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 




#create the window object
window = Tk()
window.title("Crytpo v2")
window.configure(background="black")

#create a label to ask for message to encode
#caesar
Label(window, text="CAESAR", bg="black", fg="lime green", font="terminal").grid(row=1, column=1)
Label(window, text="Message to encode:", bg="black", fg="lime green", font="terminal").grid(row=2, column=1)
#blank label to space out different labels
Label(window, bg="black", width=5).grid(row=0, column=0)
Label(window, bg="black", width=5).grid(row=0, column=2)#<----------------
Label(window, bg="black", width=5).grid(row=0, column=4)
#vigenere
Label(window, text="VIGENERE", bg="black", fg="lime green", font="terminal").grid(row=1, column=3)
Label(window, text="Message to encode:", bg="black", fg="lime green", font="terminal").grid(row=2, column=3)

#create a text entry box
#caesar
txtentrybox1 = Entry(window, width=30, bg="dim gray", fg="black", font="terminal")
txtentrybox1.grid(row=3, column=1, columnspan=1)
#vigenere
txtentrybox2 = Entry(window, width=30, bg="dim gray", fg="black", font="terminal")
txtentrybox2.grid(row=3, column=3, columnspan=1)

#buttons to encode/decode the message
#caesar
Button(window, text="ENCODE", width=6, command=caesarencode).grid(row=4, column=1, sticky=W)
Button(window, text="DECODE", width=6, command=caesardecode).grid(row=4, column=1, sticky=E)
#vigenere
Button(window, text="ENCODE", width=6, command=vigenereencode).grid(row=4, column=3, sticky=W)
Button(window, text="DECODE", width=6, command=vigeneredecode).grid(row=4, column=3, sticky=E)
#key
#caesar
Label(window, text="  ROT(1-13):", bg="black", fg="lime green", font="terminal").grid(row=5, column=1, sticky=W)
txtentrybox3 = Entry(window, width=2, bg="dim gray", fg="red", font="terminal")
txtentrybox3.grid(row=5, column=1, columnspan=1)
#vigenere
Label(window, text="key entry:", bg="black", fg="lime green", font="terminal").grid(row=5, column=3, sticky=W)
txtentrybox4 = Entry(window, width=10, bg="dim gray", fg="red", font="terminal")
txtentrybox4.grid(row=5, column=3, columnspan=1)

#create a label to display the encoded message
#caesar
Label(window, text="Message to encode:", bg="black", fg="lime green", font="terminal").grid(row=6, column=1)
#vignere
Label(window, text="Message to encode:", bg="black", fg="lime green", font="terminal").grid(row=6, column=3)

#create a text box to display the encoded messge
#caesar
txtoutputbox1 = Entry(window, width=30, bg="dim gray", fg="black", font="terminal")
txtoutputbox1.grid(row=7, column=1, columnspan=1)
#vigenere
txtoutputbox2 = Entry(window, width=30, bg="dim gray", fg="black", font="terminal")
txtoutputbox2.grid(row=7, column=3, columnspan=1)

#label at the bottom to pad the area since pdx doesnt work
Label(window, bg="black", width=5).grid(row=8, column=1)



#run the mainloop
window.mainloop()