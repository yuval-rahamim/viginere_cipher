import sys


def encrypt(msg, key, upper=False):
    if upper:
        msg = msg.upper()
        key = key.upper()
    else:
        msg = msg.lower()
        key = key.lower()

    encrypted = ""
    for i in range(len(msg)):
        encrypted += chr((ord(msg[i])-ord("a") + ord(key[i % len(key)]) - ord("a")) % 26 + ord("a"))
    return encrypted.upper()

def decrypt(msg, key, upper=False):
    if upper:
        msg = msg.upper()
        key = key.upper()
    else:
        msg = msg.lower()
        key = key.lower()

    decrypted = ""
    for i in range(len(msg)):
        decrypted += chr((ord(msg[i])-ord("a") - (ord(key[i % len(key)]) - ord("a"))) % 26 + ord("a"))
    return decrypted


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hi, what do you want to do?")
    need = input("type enc for encrypt or dec for decrypt and exit to close the program: ").lower()
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
        else:
            print("bad input.")
        need = input("type enc for encrypt or dec for decrypt and exit to close the program: ")
    sys.exit()