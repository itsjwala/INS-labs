N = 256
plain_text = input("Enter plain text:")
key = input("Enter key:")

keylen = len(key)
plain_text_length = len(plain_text)

S = []
# store all permutation in S of 8 bit (2^8 = 256)
for i in range(N):
    S.append(i)

# Key-scheduling algorithm (KSA)
j = 0
for i in range(N):
    j = (j + S[i] + ord(key[i % keylen])) % N
    S[i], S[j] = S[j], S[i]


# Pseudo-random generation algorithm (PRGA)
i = j = 0
cipher_text = []
for c in range(plain_text_length):
    i = (c + 1) % N
    j = (j + S[i]) % N
    S[i], S[j] = S[j], S[i]
    # generating key stream
    z = S[(S[i] + S[j]) % N]
    # generating cipher text
    cipher_text.append((z ^ ord(plain_text[c])) % N)

print("Cipher text :{}".format(''.join([format(i, 'X') for i in cipher_text])))
