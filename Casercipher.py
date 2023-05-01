# function to decrypt a given cipher text using Caesar Cipher
def decrypt(cipher, k):
    # string of all lowercase alphabets
    s = "abcdefghijklmnopqrstuvwxyz"
    p = ""
    # loop through all characters in the cipher text
    for i in range(len(cipher)):
        # find the index of the character in the alphabet string
        val = s.index(cipher[i])
        # calculate the decrypted character using the key
        res = (val - k) % 26
        # handle negative results
        if res < 0:
            res = len(s) + res
        # get the decrypted character from the alphabet string
        reval = s[res]
        # add the character to the decrypted message
        p += reval
    # return the decrypted message
    return p

# main function to get inputs, encrypt and decrypt the message
def main():
    # get the input string and convert it to lowercase
    a = input("Enter the input string: ").lower()
    # get the key
    k = int(input("Enter the key: "))
    # string of all lowercase alphabets
    s = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    # loop through all characters in the input string
    for i in range(len(a)):
        # find the index of the character in the alphabet string
        val = s.index(a[i])
        # calculate the encrypted character using the key
        res = (k + val) % 26
        # get the encrypted character from the alphabet string
        reval = s[res]
        # add the character to the encrypted message
        cipher += reval
    # print the encrypted message
    print("Encrypted message is:", cipher)
    # print the decrypted message
    print("Decrypted message is:", decrypt(cipher, k))

# run the main function if the script is being run as the main program
if __name__ == "__main__":
    main()

