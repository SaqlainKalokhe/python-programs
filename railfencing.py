def encrypt(plainText, key):
    # the number of rows in the matrix
    r = key
    # the length of the plaintext
    len_plainText = len(plainText)
    # calculate the number of columns in the matrix
    c = len_plainText//key + (1 if len_plainText%key != 0 else 0)
    # initialize an empty matrix with r rows and c columns
    mat = [['' for j in range(c)] for i in range(r)]
    # a counter to keep track of the current index in the plaintext
    k = 0
    # loop through each column of the matrix
    for i in range(c):
        # loop through each row of the matrix
        for j in range(r):
            # if k is not equal to the length of the plaintext
            if k != len_plainText:
                # fill the matrix with the characters from the plaintext
                mat[j][i] = plainText[k]
                # increment the counter
                k += 1
            else:
                # fill the rest of the matrix with spaces
                mat[j][i] = ' '
    # return the ciphertext by concatenating each row of the matrix
    return ''.join(''.join(row) for row in mat)

def decrypt(cipherText, depth):
    # the number of columns in the matrix
    r = depth
    # the length of the ciphertext
    len_cipherText = len(cipherText)
    # calculate the number of rows in the matrix
    c = len_cipherText//depth
    # initialize an empty matrix with r columns and c rows
    mat = [['' for j in range(c)] for i in range(r)]
    # a counter to keep track of the current index in the ciphertext
    k = 0
    # loop through each row of the matrix
    for i in range(r):
        # loop through each column of the matrix
        for j in range(c):
            # fill the matrix with the characters from the ciphertext
            mat[i][j] = cipherText[k]
            # increment the counter
            k += 1
    # return the plaintext by concatenating each column of the matrix
    return ''.join(''.join(col) for col in zip(*mat))

if __name__ == '__main__':
    # get the plaintext from the user
    plainText = input("Enter string to encrypt: ")
    # get the key from the user
    key = int(input("Enter key: "))
    print("\nText :", plainText)
    print("Key :", key)
    # encrypt the plaintext
    cipherText = encrypt(plainText, key)
    print("Cipher:", cipherText)
    # decrypt the ciphertext
    print("Original string:", decrypt(cipherText, key))
