import itertools

def bruteForce(size):
    # Character set to generate the passwords
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # List of all the characters in the character set
    pass_list = [chars[i] for i in range(36)]
    
    # Generating all the possible password combinations
    password = [''.join(i) for i in itertools.product(pass_list, repeat=size)]

    # Iterating over all the possible password combinations
    for assemble in password:
        # Printing each password
        print(assemble)
        # Checking if the current password is the right one
        if assemble == 'ABZ':
            # If the password is found, returning the password
            return "Password is: " + assemble
    # If the password is not found, returning an empty string
    return ""

# Calling the bruteForce function with size 3
print(bruteForce(3))
