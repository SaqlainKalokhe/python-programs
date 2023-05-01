# Get input values for p, q, no (plaintext), and e (encryption key)
p = int(input('Enter the value of p = '))
q = int(input('Enter the value of q = '))
no = int(input('Enter the value of text = '))
e = int(input('Enter the value of e = '))

# Calculate n and phi
n = p*q
phi = (p-1)*(q-1)

# Find the value of d (decryption key) using e and phi
for i in range(1, 10):
    x = 1 + i*phi
    if x % e == 0:
        d = int(x/e)
        break

# Calculate cipher text (ct) using no (plaintext) and e (encryption key)
ctt = pow(no, e)
ct = ctt % n

# Calculate decrypted text (dt) using ct (cipher text) and d (decryption key)
dtt = pow(ct, d)
dt = dtt % n

# Print the results
print('n:', n)
print('Encryption key is:', e)
print('Phi is:', phi)
print('Decryption key is:', d)
print('Cipher Text:', ct)
print('Decrypted Text:', dt)

'''
The code is a simple implementation of RSA (Rivest–Shamir–Adleman) algorithm for encryption and decryption. 
Here are some comments for the individual lines:

p = int(input('Enter the value of p = ')): Gets the input value for p (a prime number).
q = int(input('Enter the value of q = ')): Gets the input value for q (a prime number).
no = int(input('Enter the value of text = ')): Gets the input value for no (plaintext).
e = int(input('Enter the value of e = ')): Gets the input value for e (encryption key).
n = p*q: Calculates the value of n (modulus).
phi = (p-1)*(q-1): Calculates the value of phi (Euler's totient function).
for i in range(1,10):: Loops through the range from 1 to 9 (inclusive).
x = 1 + i*phi: Calculates the value of x for each i.
if x % e == 0:: Checks if x is divisible by e.
d = int(x/e): Calculates the value of d (decryption key) using x and e.
ctt = pow(no,e): Calculates the ciphertext (ctt) using no (plaintext) and e (encryption key).
ct = ctt % n: Calculates the value of ct (cipher text) using ctt and n.
dtt = pow(ct,d): Calculates the decrypted text (dtt) using ct (cipher text) and d (decryption key).
dt = dtt % n: Calculates the value of dt (decrypted text) using dtt and n.
print('n:',n): Prints the value of n (modulus).
print('Encryption key is:',e): Prints the value of e (encryption key).
print('Phi is:',phi): Prints the value of phi (Euler's totient function).
print('Decryption key is:',d): Prints the value of d (decryption key).
print('Cipher Text:',ct): Prints the value of ct (cipher text).
print('Decrypted Text:',dt):
'''
