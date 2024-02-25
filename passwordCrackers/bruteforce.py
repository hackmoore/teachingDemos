import hashlib
import string
import time
from itertools import product
 
def hash(password):
    return password #disable hashing - we don't need it
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def product_loop(password, generator):
    for p in generator:
        guess_password = hash(''.join(p))
        if guess_password == password:
            print("Your password is:", guess_password)
            exit()
        if print_failure:
            print("Guessing passowrd: ", guess_password)
        if slow:
            time.sleep(0.1)
    return False
 
 
def bruteforce(password, max_nchar=8):
    all_char = string.digits + string.ascii_letters + string.punctuation

    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(all_char, repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p

 
############# append the below code ################
actual_password = 'sunshine'
actual_password_hash = hash(actual_password)
slow = False
print_failure = False
 
# Running the Brute Force attack
bruteforce(actual_password_hash)
 
# If the password can't be found
print("I couldn't guess this password :(")
