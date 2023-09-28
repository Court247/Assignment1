import crypt

##As others have said, the hash function can't be reversed.
# So how can chrome use it?
# The hashes are stored, then when you enter a password that password is hashed, 
# then that hash is compared with the stored hashes. 
# Chrome never reverses a hash.

def Assign1(f,f2):
    i = 0
    for line in f:
        splitLine = line.strip()
        splitLine = line.replace("\n","").split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        if hashedPass not in ['x', '*', '!']:
            i = i+1
            crackHash(user, hashedPass, f2)
            print(f'{i} it enters')
        else:
            print('Pass verification not available')

def crackHash(user, hashedPass, f2):
    isFound = False
    i=0
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]
    password = cryptedPass[3]
    saltIn = "$" + hashFormat + '$' + salt + "$"

    print(f" Finding password for: {user}")

    for word in f2:
        print(f'{i} it enters here too\n')
        word = word.strip()
        word = word.strip('\n')
        hashedWord = crypt.crypt(word, saltIn)
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {word}')
            break
        i = i+1
    if(isFound == False):
        print(f'{i} it came here\n')
        print('Password not in file')
        




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


    








