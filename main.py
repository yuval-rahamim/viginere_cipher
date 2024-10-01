import sys
import string

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
def encrypt(msg, key, upper=False):
    if upper:
        msg = msg.upper()
        key = key.upper()
    else:
        msg = msg.lower()
        key = key.lower()

    encrypted = ""
    l = 0

    for i in range(len(msg)):
        if msg[i].isalpha():  # Only encrypt alphabetic characters
            encrypted += chr((ord(msg[i]) - ord('a') + (ord(key[l % len(key)]) - ord('a'))) % 26 + ord('a'))
            l += 1
        else:
            encrypted += msg[i]

    return encrypted.upper() if upper else encrypted.lower()


def decrypt(msg, key, upper=False):
    if upper:
        msg = msg.upper()
        key = key.upper()
    else:
        msg = msg.lower()
        key = key.lower()

    decrypted = ""
    l = 0

    for i in range(len(msg)):
        if msg[i].isalpha():  # Only decrypt alphabetic characters
            decrypted += chr((ord(msg[i]) - ord('a') - (ord(key[l % len(key)]) - ord('a'))) % 26 + ord('a'))
            l += 1
        else:
            decrypted += msg[i]

    return decrypted.upper() if upper else decrypted.lower()

def remove_non_letters(s):
    return ''.join(char for char in s if char.isalpha())

def crackTheCode(msg): #פריצה לצופן
    global englishLetterFreq

    msg = remove_non_letters(msg)
    dup = msg
    max_size = 0
    for i in range(1, len(msg)):
        size = 0
        for j in range(i, len(msg)-i):
            if msg[j] == dup[i+j]:
                size += 1
        if size > max_size:
            max_size = size
    print(max_size)

    for j in range(max_size):
        lis = []
        i = j
        while i < len(msg):
            lis.append(msg[i])  # Append character to the list
            i += max_size
        print(f"Characters at interval {j}: {''.join(lis)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hi, what do you want to do?")
    need = input("Type 'enc' for encrypt, 'dec' for decrypt, 'crack' to crack the msg, or 'exit' to close the program: ").lower()
    while need != "exit":
        if need == "enc":
            msg = input("please enter the msg you want to encrypt: ")
            key = input("please enter your key: ")
            upperString = input("is your msg and key are upper? press true or false (anything else will be lower): ").lower()
            upper = False
            if upperString == "true":
                upper = True
            print("your encrypted msg is: ",encrypt(msg, key,upper))
        elif need == "dec":
            msg = input("please enter the msg you want to decrypt: ")
            key = input("please enter your key: ")
            upperString = input("is your msg and key are upper? press true or false (anything else will be lower): ").lower()
            upper = False
            if upperString == "true":
                upper = True
            print("your encrypted msg is: ",encrypt(msg, key,upper))
        elif need == "crack":
            msg = input("please enter the msg: ")
            crackTheCode(msg)
        else:
            print("bad input.")
        need = input("Type 'enc' for encrypt, 'dec' for decrypt, 'crack' to crack the msg, or 'exit' to close the program: ").lower()
    sys.exit()