from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

##As others have said, the hash function can't be reversed.
# So how can chrome use it?
# The hashes are stored, then when you enter a password that password is hashed, 
# then that hash is compared with the stored hashes. 
# Chrome never reverses a hash.

def Assign1(f,f2, f3):
    for line in f.readlines():
        splitLine = line.strip()
        splitLine = line.replace("\n","").split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        if hashedPass not in ['x', '*', '!']:
            crackHash(user, hashedPass, f2, f3)
        else:
            print('Pass verification not available')

def crackHash(user, hashedPass, f2,f3):
    isFound = False
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]
    password = cryptedPass[3]
    saltIn = "$" + hashFormat + '$' + salt + "$"
    print(f" Finding password for: {user}")
    
    if hashFormat == '1':
        for word in f2:
            word.strip()
            word.strip('\n')
            print(f'2. MD5 {word}')
            print(f'3. MD5 {hashedWord}')

            hashedWord = md5_crypt.using(salt=salt).hash(word)
            if(hashedWord == hashedPass):
                isFound= True
                print(f'Password for {user} is {word}')
                break
        if(isFound == False):
            print("Password not found in dictionary file")
    elif hashFormat == '6':
        for word in f2:
            word.strip()
            word.strip('\n')
            hashedWord = sha512_crypt.using(rounds = 5000, salt = salt).hash(word)
            print(f'2. SHA512 {word}')
            print(f'3. SHA512 {hashedWord}')
            if(hashedWord == hashedPass):
                isFound= True
                print(f'Password for {user} is {word}')
                break
        if(isFound == False):
            print("Password not found in dictionary file")




if __name__ == '__main__':

    file = 'Assignment1/Problem-1/shadowfile.txt'
    file2 = 'Assignment1/Problem-1/commonPasswdFile.txt'
    file3 = 'Assignment1/Problem-1/commonPasswordFile2.txt'
    f = open(file, 'r', encoding="utf8")
    f2 = open(file2, 'r', encoding="utf8")
    f3 = open(file3, 'r', encoding="utf8")
    Assign1(f, f2, f3)


    








