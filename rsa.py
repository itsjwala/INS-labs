def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


def fast_expo(a, b, mod):
    res = 1
    while b > 0:
        if(b & 1):
            res = (res * a) % mod
        a = (a * a) % mod
        b = b >> 1

    return res

# p=10**9+7
# q=10**9+9


p = int(input("Enter p:"))
q = int(input("Enter q:"))

n = p * q


phi = (p - 1) * (q - 1)

e = 2

while(e < phi):
    if(gcd(e, phi) == 1):
        break
    e += 1

print("public key is ( {} , {} )".format(e, n))
d = mod_inverse(e, phi)

print("private key is ( {} , {} )".format(d, n))

message = int(input('enter message :'))

# Encryption , encrypted_data=(message^e)%n

encrypted_data = fast_expo(message, e, n)

print("Encrypted data is :{}".format(encrypted_data))

# Decryption , decrypted_data = (encrypted_data ^ d) % n

decrypted_data = fast_expo(encrypted_data, d, n)

print("Decrypted data is :{}".format(decrypted_data))
