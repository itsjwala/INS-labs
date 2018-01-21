key = int(input("Enter key :"))

message = input("Enter message :")

print(f"message is '{message}'")
opt = None

try:
    opt = int(input("1. Encryption  2. Decryption : "))
except Exception as e:
    pass

if opt == 1:
    encrypted = ""
    for c in message:
        if c != ' ':
            encrypted += chr(((ord(c) - ord('a') + key) % 26) + ord('a'))
        else:
            encrypted += ' '
    print(f"Encrypted message is '{encrypted.upper()}'")
elif opt == 2:
    decrypted = ""
    for c in message:
        decrypted += chr(((ord(c) - ord('a') - key) % 26) + ord('a'))

    print(f"Decrypted message is '{decrypted}'")
else:
    print("Enter correct option")
