from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

##As others have said, the hash function can't be reversed.
# So how can chrome use it?
# The hashes are stored, then when you enter a password that password is hashed, 
# then that hash is compared with the stored hashes. 
# Chrome never reverses a hash.

def Assign1(f,f2):
    passList=list(f2)

    for line in f:
        splitLine = line.strip()
        splitLine = line.replace("\n","").split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        if hashedPass not in ['x', '*', '!']:
            if len(passList) == 0:
                raise ValueError('Length is 0')
            else:
                crackHash(user, hashedPass, passList)
        else:
            print('Pass verification not available')

def crackHash(user, hashedPass, f2):
    i =0
    isFound = False
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]
    password = cryptedPass[3]
    saltIn = "$" + hashFormat + '$' + salt + "$"
    print(f" Finding password for: {user}")
    
    while(i < len(f2)):
        word = f2[i].strip()
        word = word.strip('\n')
        if hashFormat == '1':
            hashedWord = md5_crypt.using(salt=salt).hash(word)
            if(hashedWord == hashedPass):
                isFound= True
                break
        if hashFormat == '6':
            hashedWord = sha512_crypt.using(rounds = 5000, salt = salt).hash(word)
            if(hashedWord == hashedPass):
                isFound= True
                break
        i = i+1
    if(isFound == False):

        print("Password not found in dictionary file")
    else:
        print(f'Password for {user} is {word}')





if __name__ == '__main__':

    file = 'Assignment1/Problem-1/shadowfile.txt'
    file2 = 'Assignment1/Problem-1/commonPasswdFile.txt'
    file3 = 'Assignment1/Problem-1/commonPasswordFile2.txt'
    file4 = 'Assignment1/Problem-1/Test1.txt'
    file5 = 'Assignment1/Problem-1/Test2.txt'
    f = open(file, 'r', encoding="utf8")
    f2 = open(file2, 'r', encoding="utf8")
    f3 = open(file3, 'r', encoding="utf8")
    f4 = open(file4, 'r', encoding="utf8")
    f5 = open(file5, 'r', encoding="utf8")

    Assign1(f, f2)


    








