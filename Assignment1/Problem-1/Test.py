from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

def Assign(crackPass, crackUser):
    for line in crackUser:
        splitLine = line.strip()
        splitLine = line.replace("\n","").split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        if hashedPass not in ['x', '*', '!']:
            crackHash(user, hashedPass, crackPass)
        else:
            print('Pass verification not available')

def crackHash(user, hashedPass, crackPass):
    i =0
    isFound = False
    cryptedPass = hashedPass.split("$")
    hashFormat = cryptedPass[1]
    salt = cryptedPass[2]
    password = cryptedPass[3]
    saltIn = "$" + hashFormat + '$' + salt + "$"
    print(f" Finding password for: {user}")
    
    if hashFormat == '1':
        for word in crackPass:
            word = word.strip()
            word = word.strip('\n')
            hashedWord = md5_crypt.using(salt=salt).hash(word)
            print(i)
            print(f'2. MD5 {word}')
            print(f'3. MD5 {hashedWord}')
            print(hashedPass)

            if(hashedWord == hashedPass):
                isFound= True
                break
            i = i+1
        if(isFound == False):
            print("Password not found in dictionary file")
        else:
            print(f'Password for {user} is {word}')
    elif hashFormat == '6':
        for word in crackPass:
            word = word.strip()
            word = word.strip('\n')
            hashedWord = sha512_crypt.using(rounds = 5000, salt = salt).hash(word)
            print(i)
            print(f'2. SHA512 {word}')
            print(f'3. SHA512 {hashedWord}')
            print(hashedPass)

            if(hashedWord == hashedPass):
                isFound= True
                break
            i = i+1
        if(isFound == False):
            print("Password not found in dictionary file")
        else:
            print(f'Password for {user} is {word}')



if __name__ == '__main__':
    crackUser = ['crack01:$1$l3RgvDgR$.jp4EA47X38Yny8reSbi71:17783:0:99999:7:::', 'crack02:$1$EuD4fxOr$2KnCjWcoZjf0MNnVtw0lI0:17783:0:99999:7:::', 'crack03:$1$oeHzBJRr$Z2f.5MJMsnSEv7x.hQfEM.:17783:0:99999:7:::', 'crack04:$1$oxZ07lmK$dGj1Y1U8EFv/srVLQ8Rcm/:17783:0:99999:7:::', 'crack05:$1$HP8u2rW.$vBhiITjbs5LptdM99g1Ga/:17783:0:99999:7:::']
    crackPass = ['Bailey*1',
'qu1nt3r0',
'chocobo7',
'rafaels9',
'karelbol102',
'cf6ddc0d',
'Cooldude1',
'Beatfabrik1',
'123456',
'phantom6',
'paul2008',
'123amhlr0m',
'abclsd123',
'mariosunshine64',
'allmess2009',
'fdtdlove4ever',
'lacoste94',
'Pacman9195',
'1701e1007',
'lvn?you',
'Stella01',
'lmck2096',
'balint15vp']

Assign(crackPass, crackUser)