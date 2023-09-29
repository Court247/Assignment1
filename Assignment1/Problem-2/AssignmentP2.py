from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt
from passlib.hash import hex_md5

from tqdm import tqdm
import itertools

def Assign1P2A(f,f3):
    wordList = list(f3)
    for line in f:
        splitLine = line.split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        crackHash(user, hashedPass, wordList)

def crackHash(user, hashedPass, f2):
    isFound = False
    numList = ['0','1','2','3','4','5','6','7','8','9']
    maxLen = 10
    checkNum = False
    for word in tqdm(f2):
        word = word.strip()
        word = word.strip('\n')
        
        if checkWord(word, user, hashedPass, isFound):
            isFound = True
            break
        elif checkNumList(user, word, hashedPass, numList, isFound, maxLen):
            isFound = True
            break
        
        elif checkNum == False:
            checkNum = True
            if checkNumCombo(user, numList, hashedPass, isFound):
                isFound = True
                break
        
        elif checkCombo(user, word, hashedPass,f2, isFound):
            isFound = True
            break
    # if whole list is searched and the password is never found, then print that
    if(isFound == False):
        print('here')
        print('Password not in file')

def checkWord(word, user, hashedPass, isFound):
    if(len(word)>=5):
        hashedWord =  hex_md5.hash(word)
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {word}')

            #write to text file
            writeText(user, word)
            return isFound
    return isFound

def checkNumList(user, word, hashedPass, numList, isFound, maxLen):
    if len(word)>5 and len(word)<=maxLen:
        diff = maxLen-len(word)
        combo = list(itertools.combinations(numList, diff))
        for i in combo:
            x = convert(i)
            temp = word+x
            hashedWord = hex_md5.hash(temp)
            if(temp == 'revenge234'):
                raise ValueError('here')
            if(hashedWord == hashedPass):
                isFound= True
                print(f'Password for {user} is {temp}')
                #write to text file
                writeText(user, temp)
                return isFound
    return isFound

def checkCombo(user, word, hashedPass, f2, isFound):
    for j in f2:
        temp = word+j
        hashedWord = hex_md5.hash(temp)
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {temp}')
            #write to text file
            writeText(user, temp)
            return isFound
    return isFound

def checkNumCombo(user, numList, hashedPass, isFound):
    fullCombo = list(itertools.combinations(numList,8))
    for num in fullCombo:
        temp = convert(num)
        hashedWord = hex_md5.hash(temp)
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {temp}')
            #write to text file
            writeText(user, temp)
            return isFound
    return isFound

# Method to write to text file crackedPasswords 
def writeText(user, word):
    file = 'crackedPasswordsP2A.txt'
    open(file, 'a').write(f'{user}:{word}\n')

#Method to convert the tuple to string
def convert(tup):
        # initialize an empty string
    str = ''
    for i in tup:
        str = str + i
    return str


if __name__ == '__main__':
    
    file = 'Assignment1/Problem-2/UnsaltedPassTable.txt'
    file2 = 'Assignment1/Problem-2/SaltedPassTable.txt'
    file3 = 'Assignment1/Problem-2/words.txt'
    
    f = open(file, 'r', encoding="utf8")
    f2 = open(file2, 'r', encoding="utf8")
    f3 = open(file3, 'r', encoding="utf8")
    
    Assign1P2A(f, f3)