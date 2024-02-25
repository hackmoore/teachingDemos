import hashlib
from urllib.request import urlopen
import time
 
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
 
 
def wordlistAttack(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        hash_guess = hash(guess_password)
        if hash_guess == actual_password_hash:
            print("Your password is:", guess_password)
            exit()
        else:
            if print_failure:
                print("Guessing passowrd: ", guess_password)
            if slow:
                time.sleep(0.1)
 
############# append the below code ################

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'cooldude' # examples: sunshine or cooldude
actual_password_hash = hash(actual_password)
slow = False
print_failure = True
 
wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
 
# Running the Brute Force attack
wordlistAttack(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")
