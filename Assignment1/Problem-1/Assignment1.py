import crypt

##As others have said, the hash function can't be reversed.
# So how can chrome use it?
# The hashes are stored, then when you enter a password that password is hashed, 
# then that hash is compared with the stored hashes. 
# Chrome never reverses a hash.

def Assign1(f,f2):
    for line in f:
        splitLine = line.strip()
        splitLine = line.replace("\n","").split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        if hashedPass not in ['x', '*', '!']:
            crackHash(user, hashedPass, f2)
        else:
            print('Pass verification not available')

def crackHash(user, hashedPass, f2):
    isFound = False
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]
    password = cryptedPass[3]
    saltIn = "$" + hashFormat + '$' + salt + "$"
    print(f" Finding password for: {user}")

    for word in f2:
        word.strip()
        word.strip('\n')
        hashedWord = crypt.crypt(word, saltIn)
        if(hashedWord == cryptedPass):
            isFound= True
            print(f'Password for {user} is {word}')
            break
    if(isFound == False):
        print("Password not found in dictionary file")



if __name__ == '__main__':

    file = 'Problem-1/shadowfile.txt'
    file2 = 'Problem-1/commonPasswdFile.txt'
    file3 = 'Problem-1/commonPasswordFile2.txt'
    f = open(file, 'r')
    f2 = open(file2, 'r')
    f3 = open(file3, 'r')
    Assign1(f, f2)


    








