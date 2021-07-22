from collections import deque
import art as at

print(at.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Call back function for repeating the cipher over again until a no is typed
def call_back():
    Yes_or_no = input("Type yes if you want to go again, otherwise type no: ").lower()

    if Yes_or_no == "yes":
        direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text1 = input("Type your message:\n").lower()
        shift1 = int(input("Type the shift number:\n"))

        Caesar_Encryption(text1, shift1, direction1)
    elif Yes_or_no == "no":
        print("Good Bye !!!!")
        exit()

def Caesar_Encryption(plain_text,shift_key,Direction_input):
    #Creat a list to take the index of the of the text in the alphabets
    word = []
    encrypted_word = []

    #Setting the variable alphabet from local to global
    global alphabet

    #Writing an if statement for encoding or decoding
    if Direction_input == "encode":
        #Getting the index of the text in the alphabets list
        #Looping through the text and saving the indexes into a list
        for char in plain_text:
        #checking if a selected char is in the alphabet list
        #Appending the index of the the selected char in the alphabet list to the word list
            if char in alphabet:
                word.append(alphabet.index(char))
            elif char not in alphabet:
                word.append(char)
        #Rotating or shiftig words to the left
        alphabet = deque(alphabet)
        alphabet.rotate(-shift_key)
        alphabet = list(alphabet)

    elif Direction_input == "decode":
        for char in plain_text:
            #checking if a selected char is in the alphabet list
            #Appending the index of the the selected char in the alphabet list to the word list
            if char in alphabet:
                word.append(alphabet.index(char))
            elif char not in alphabet:
                word.append(char)
        #Rotating or shiftig words to the right
        alphabet = deque(alphabet)
        alphabet.rotate(shift_key)
        alphabet = list(alphabet)
    else:
        print("Select decode or encode")

    #checking the type of element in list 
    #if is an integer is compared to the shifted list
    #if not is left untouched
    for index in word:
        if type(index) == str:
            encrypted_word.append(index)
        elif type(index) == int:
            encrypted_word.append(alphabet[index])
    
    print("Here's the results: " + ''.join(encrypted_word))
    
    #Calling the call back function
    call_back()

Caesar_Encryption(text, shift, direction)
