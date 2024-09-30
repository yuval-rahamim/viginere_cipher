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
    return encrypted

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
    print(encrypt('prosper','bop'))
    print(decrypt(encrypt('prosper','bop'), 'bop'))
