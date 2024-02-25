import hashlib
from urllib.request import urlopen
import time

MODIFICATION_NONE = 0
MODIFICATION_REVERSE = 1
MODIFICATION_DOUBLE = 2
MODIFICATION_LOWERCASE = 3
MODIFICATION_UPPERCASE = 4
MODIFICATION_SUBS = 5
MODIFICATION_NUMS = 6
 
def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile
 
 
def hash(wordlistpassword):
    return wordlistpassword #disable hashing - we don't need it

    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()

def modification(password, mod):
    if mod == MODIFICATION_NONE:
        return [password]
    if mod == MODIFICATION_REVERSE:
        return [password[::-1]]
    elif mod == MODIFICATION_DOUBLE:
        return [password+password]
    elif mod == MODIFICATION_LOWERCASE:
        return [password.lower()]
    elif mod == MODIFICATION_UPPERCASE:
        return [password.upper()]
    elif mod == MODIFICATION_SUBS:
        # TODO
        return [password]
    elif mod == MODIFICATION_SUBS:
        return [password+'1']
    else:
        print("Unknown mod")
 
 
def wordlistAttack(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        for mod in range(0, 6):
            print(guess_password)
            passwords = modification(guess_password, mod)

            for gPassword in passwords:
                hash_guess = hash(gPassword)
                if hash_guess == actual_password_hash:
                    print("Your password is:", guess_password)
                    exit()
                else:
                    if print_failure:
                        print("Guessing password: ", guess_password)
                    if slow:
                        time.sleep(0.1)

 
############# append the below code ################
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'sunshine' # examples: sunshine or cooldude or moose6
actual_password_hash = hash(actual_password)
slow = True
print_failure = True
 
wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
 
# Running the Brute Force attack
wordlistAttack(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")
