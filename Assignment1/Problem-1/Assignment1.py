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
            print(f'1: it enters')
        else:
            print(f'Pass verification for {user} not available')

def crackHash(user, hashedPass, f2):
    isFound = False
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]
    password = cryptedPass[3]
    saltIn = "$" + hashFormat + '$' + salt + "$"
    word = ''

    print(f"Finding password for: {user}")
    print(f'2: It is here {isFound}')
    print(f'Word Before Loop: {word}')
    for word in f2:
        
        print(f'3: it enters here too')
        word = word.strip()
        word = word.strip('\n')
        print(f'Word: {word}')
        hashedWord = crypt.crypt(word, saltIn)
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {word}')
            f2.seek(0)
            break
    if(isFound == False):
        print(f'4: it came here')
        print('Password not in file')
        f2.seek(0)




if __name__ == '__main__':

    file = 'shadowfile.txt'
    file2 = 'commonPasswdFile.txt'
    file3 = 'commonPasswordFile2.txt'
    file4 = 'Test1.txt'
    file5 = 'Test2.txt'
    f = open(file, 'r')
    f2 = open(file2, 'r')
    f3 = open(file3, 'r')
    f4 = open(file4, 'r')
    f5 = open(file5, 'r')
    Assign1(f, f5)


    








