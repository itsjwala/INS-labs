def convert_to_matrix(message, m, n):
    cipher_matrix = []
    c = 0
    for row in range(m):
        cipher_matrix.append(list())
        for col in range(n):
            if c < len(message):
                cipher_matrix[row].append(message[c])
                c += 1
            else:
                cipher_matrix[row].append(' ')
    return cipher_matrix


def print_matrix(mat):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            print(mat[row][col], end=" ")
        print()


def transform(mat, key):
    transformed = []
    for i in list(map(int, key.strip().split(' '))):
        i -= 1
        transformed.append(mat[i])

    return transformed


def mat_to_str(mat):
    text = ""
    for row in range(len(mat)):
        text += "".join(mat[row])

    return text.strip()


message = input("Enter message : ")
m = int(input("Enter number of rows : "))
n = int(input("Enter number of columns : "))
cipher_matrix = convert_to_matrix(message, m, n)
print("Cipher matrix =>")
print_matrix(cipher_matrix)

key = input("Enter key : ")

try:
    opt = int(input("1. Encryption  2. Decryption : "))
except Exception as e:
    pass

if opt == 1:
    transformed_mat = transform(cipher_matrix, key)
    cipher = mat_to_str(transformed_mat)
    print('Encrypted message '{}''.format(cipher))

elif opt == 2:
    text = mat_to_str(transform(cipher_matrix, key))
    print("Decrypted message '{}'".format(text))
else:
    print("Enter correct option")
