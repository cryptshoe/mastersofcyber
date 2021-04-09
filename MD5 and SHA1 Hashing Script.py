# This script was designed to complete 2 main functions. 1) Encode MD5 and SHA1. 2) Brute-force MD5 and SHA1
# The Brute-force function runs off a wordlist of 10000 words, these are the most popular words used for passwords.
# If the hash you have used is not Brute-forced then it would not be in the list. As this script was designed for
# educational purposes, a 10000 word wordlist was deemed large enough, but can be easily swapped out with any text
# based wordlist.

# If you want to test it, try 'password', or anything else you want.

# Import the libraries
from urllib.request import urlopen, hashlib

# Menu Functions. This displays the menu and returns your choice.
def menu():
    print('1.Encode MD5')
    print('2.Encode SHA1')
    print('3.Brute-force MD5')
    print('4.Brute-force SHA1')
    hashchoice = input('Please input your choice.\n')
    return int(hashchoice)

# MD5 Hash function. This creates a MD5 hash from the string input and prints the hash. At the end of the function it
# provides the user with the option to go back to the menu to select another option
def md5_hash(md5_hashed_string):
    hash_object = hashlib.md5(md5_hashed_string.encode())
    print(hash_object.hexdigest())
    back2menu = input('\nDo you want to choose another option: y/n\n')
    if back2menu == 'y':
        return
    else:
        quit()

# This function is the same as the MD5 function, but encodes the string input into a SHA1 hash.
def sha1_hash(sha1_hashed_string):
    hash_object = hashlib.sha1(sha1_hashed_string.encode())
    print(hash_object.hexdigest())
    back2menu = input('\nDo you want to choose another option: y/n\n')
    if back2menu == 'y':
        return
    else:
        quit()

# This Function is used to brute-force a MD5 hash. First it pulls a text file from the URL. Then for each entry in the
# list it hashed the string. It then compares the newly hashed string with the hash inputted by the user. If the hashes
# do not match then it moves to the next word in the list. if it finds a match, then it will display the plain text
# string. This function will also allow the user to return to the main menu.

def md5_crack(md5_string) :
    plist = str(urlopen('https://raw.githubusercontent.com/cryptshoe/mastersofcyber/main/wordlist.txt').read(), 'utf-8')
    for guess in plist.split('\n'):
        hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == md5_string:
            print("\nCongratulations!! The password is ", str(guess))
            back2menu = input('\nDo you want to choose another option: y/n\n')
            if back2menu == 'y':
                return
            else:
                quit()
        elif hashedGuess != md5_string:
            print("Password guess ",str(guess)," does not match, trying next...")
    print("Password not in list. Please try another")
    back2menu = input('\nDo you want to choose another option: y/n\n')
    if back2menu == 'y':
        return
    else:
        quit()

# This function will do the same as the MD5 crack, however this will crack a SHA1 hash.

def sha1_crack(sha1_string) :
    plist = str(urlopen('https://raw.githubusercontent.com/cryptshoe/mastersofcyber/main/wordlist.txt').read(), 'utf-8')
    for guess in plist.split('\n'):
        hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == sha1_string:
            print("\nCongratulations!! The password is ", str(guess))
            back2menu = input('\nDo you want to choose another option: y/n\n')
            if back2menu == 'y':
                return
            else:
                quit()
        elif hashedGuess != sha1_string:
            print("Password guess ",str(guess)," does not match, trying next...")
    print("Password not in list. Please try another")
    back2menu = input('\nDo you want to choose another option: y/n\n')
    if back2menu == 'y':
        return
    else:
        quit()


# The main logic of the script.

loop = 1
while True:
    hashchoice = menu()

    if hashchoice == 1:
        string = input("Please input a string to hash with MD5:\n")
        md5_hash(string)
    if hashchoice == 2:
        string = input("Please input a string to hash with SHA1:\n")
        sha1_hash(string)
    if hashchoice == 3:
        hashed = input("Please input a MD5 hash to crack.\n>")
        md5_crack(hashed)
    elif hashchoice == 4:
        hashed = input("Please input a SHA1 hash to crack.\n>")
        sha1_crack(hashed)
