# Both the persons will be agreed upon the
# public keys q and p
p = int(input('Enter prime number p :'))
q = int(input('Enter prime number q :'))


# Alice will choose the private key a
a = 4
# a is the chosen private key
print("The private key a for Alice : {}".format(a))
x = q**a % p
# gets the generated key

# Bob will choose the private key b
b = 3
# b is the chosen private key
print("The private key b for Bob : {}".format(b))

y = q**b % p
# gets the generated key

# Generating the secret key after the exchange of keys
ka = y**a % p
# Secret key for Alice
kb = x**b % p
# Secret key for Bob

print("Secret key for the Alice is : {}".format(ka))
print("Secret Key for the Bob is : {}".format(kb))
