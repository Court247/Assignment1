#   Author: Courtney Woods
#   Date: September 28, 2023
#   Teacher: Deepak Tosh
#   Class: CS 4351 Computer Security

from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

from tqdm import tqdm

##As others have said, the hash function can't be reversed.
# So how can chrome use it?
# The hashes are stored, then when you enter a password that password is hashed, 
# then that hash is compared with the stored hashes. 
# Chrome never reverses a hash.


# Method for traversing the shadowFile
def Assign1(f,f2):
    
    #Change [commonPasswordFile.txt] into a traversable list
    passList=list(f2)

    # Traverse shadow file
    for line in f:

        # remove white spaces
        splitLine = line.strip()

        #remove whitespaces, new lines, and then split with ':' as the delimiter which turns it into a list 
        splitLine = line.replace("\n","").split(':')

        # set the username
        user = splitLine[0]

        #set the hashed password
        hashedPass = splitLine[1]

        # check if theres any 'x', '*' or '!' if there is one in this variable, then password is not retrievable
        if hashedPass not in ['x', '*', '!']:

            #call the {crackHash} method
            crackHash(user, hashedPass, passList)
        else:
            print(f'Pass verification for {user} not available')

# Method that begins the cracking process
def crackHash(user, hashedPass, f2):

    # variable for if the password is found in the password list
    isFound = False

    # splits the hashed password with '$' as delimiter into a list that gives the hashFormat (MD5, SHA256 etc), the salt, and the hash of the password
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]

    print(f'Cracking password for {user}...')

    #Loop that traverses the commonPasswordFile list with loading bar to see progress.
    for word in tqdm(f2):

        # removes white space
        word = word.strip()

        # removes new line
        word = word.strip('\n')

        # Checks has format to determine how to hash.
        if hashFormat == '1':

            # Hashes {word} giving the salt variable
            hashedWord = md5_crypt.using(salt=salt).hash(word)

            # if the newly hashed word matches the hashed password we are trying to find, change isFound to true, then print the username and it's password
            if(hashedWord == hashedPass):
                isFound= True

            # break out the for loop
                break

        # Checks has format to determine how to hash.
        if hashFormat == '6':

            # Hashes {word} giving the salt variable
            hashedWord = sha512_crypt.using(rounds = 5000, salt = salt).hash(word)

            # if the newly hashed word matches the hashed password we are trying to find, change isFound to true, then print the username and it's password
            if(hashedWord == hashedPass):
                isFound= True

                #write to text file
                writeText(user, word)

                # break out the for loop
                break

    # if whole list is searched and the password is never found, then print that
    if(isFound == False):

        print("Password not found in dictionary file")
    else:
        print(f'Password for {user} is {word}')
        
        #write to text file
        writeText(user, word)



# Method to write to text file crackedPasswords 
def writeText(user, word):
    file = 'crackedPasswords2.txt'
    open(file, 'a').write(f'{user}:{word}\n')


if __name__ == '__main__':
    
    '''
        Instructions: All you have to do is set the relative path to the shadow file and the common password file, then run the program.
        If you want to change the common password file, just change the file path to the new file or change f2 to f3.
    '''

    # set the file path
    file = 'Assignment1/Problem-1/shadowfile.txt'
    file2 = 'Assignment1/Problem-1/commonPasswdFile.txt'
    file3 = 'Assignment1/Problem-1/commonPasswordFile2.txt'
    #file4 = 'Assignment1/Problem-1/Test1.txt'
    #file5 = 'Assignment1/Problem-1/Test2.txt'
    
    # open files
    f = open(file, 'r', encoding="utf8")
    f2 = open(file2, 'r', encoding="utf8")
    f3 = open(file3, 'r', encoding="utf8")
    #f4 = open(file4, 'r', encoding="utf8")
    #f5 = open(file5, 'r', encoding="utf8")

    # call assign method to start the process
    Assign1(f, f2)

    # close files
    f.close()
    f2.close()
    f3.close()
    #f4.close()
    #f5.close()
    








