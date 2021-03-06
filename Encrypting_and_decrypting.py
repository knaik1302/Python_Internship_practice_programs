'''
You might have heard about Cyptography, haven't you? 
Sending confidential messages with clean encoding and decoding.
It has great importance especially in cyber intelligence as well as defence ministry.
There are many kinds of encyphering techniques prevailing now. 


 Have you hear about Caesar's encypher?
This is an ancient and simple encypher method. 
 Look at this encoded message  : L ORYH BRX 
When decoded, it looks this way : I LOVE YOU 


Wondering how?
In the previous encoding we used an alphabet right shift of 3. 
It means every alphabet will be considered with third corresponding alphabet when encoded. 


Finally we will have,

Shift value: 3 
Actual     : A B C D E F G ...... U V W X Y Z 
Encoded : C D E F G H I ........ X Y Z A B C 


So, now write a Python program for Caesar's encypher that can accept any input and shift value from user and perform the encypher operation.
Nevertheless, proceed with decypher operation if some encoded message is given as input.
'''

def Encrpytingchar(char):
    if(char!=" "):
        return chr((((ord(char)+3)+65)%26)+65)
    return " "
    

def CaesorEncrypter(a):
    encrypted_msg=""
    for i in range(0,len(a)):
        encrypted_msg+=Encrpytingchar(a[i])
    return encrypted_msg

def Decrpytingchar(char):
    if(char!=" "):
        return chr((((ord(char)-3)+65)%26)+65)
    return " "
    

def CypherDycrypter(a):
    decrypted_msg=""
    for i in range(0,len(a)):
        decrypted_msg+=Decrpytingchar(a[i])
    return decrypted_msg


msg=input("Enter the Message").upper()
Encrpyted_msg=CaesorEncrypter(msg)
print(Encrpyted_msg)
Decrypted_msg=CypherDycrypter(Encrpyted_msg)
print(Decrypted_msg)
