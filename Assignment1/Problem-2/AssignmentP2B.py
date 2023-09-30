
from passlib.hash import hex_md5

from tqdm import tqdm
import itertools

def Assign1P2A(f,f3):
    wordList = list(f3)
    for line in f:
        splitLine = line.split(':')
        user = splitLine[0]
        salt = splitLine[1]
        hashedPass = splitLine[2]
        hashedPass = hashedPass.replace('\n',"")
        hashedPass = salt + ':' + hashedPass
        crackHash(user, salt, hashedPass, wordList)

def crackHash(user, salt, hashedPass, f2):
    isFound = False
    numList = ['0','1','2','3','4','5','6','7','8','9']
    maxLen = 10
    checkNum = False

    print(f'Cracking password for {user}...')

    for word in tqdm(f2):
        word = word.strip()
        word = word.replace('\n',"")
        if checkWord(word, user, salt, hashedPass, isFound):
            isFound = True
            break
        elif checkNumList(user, word, salt, hashedPass, numList, isFound, maxLen):
            isFound = True
            break
        elif checkNum == False:
            checkNum = True
            if checkNumCombo(user, salt, numList, hashedPass, isFound):
                isFound = True
                break
        elif checkCombo(user, word, salt, hashedPass,f2, isFound):
            isFound = True
            break
    # if whole list is searched and the password is never found, then print that
    if(isFound == False):
        print(f'Password for {user} not in file')

# Method to check the word list
def checkWord(word, user, salt, hashedPass, isFound):
    if(len(word)>=5):
        hashedWord =  hex_md5.hash(salt+word)
        hashedWord = salt + ':' + hashedWord
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {word}')

            #write to text file
            writeText(user, word,'crackedPasswordsP2B.txt')
            return isFound
    return isFound

# Method to check the combination of the word and the number list
def checkNumList(user, word,salt, hashedPass, numList, isFound, maxLen):
    if len(word)>5 and len(word)<=maxLen:
        diff = maxLen-len(word)
        if diff != 0:
            combo = list(itertools.combinations(numList, diff))
            for i in combo:
                x = convert(i)
                temp = word+x
                hashedWord = hex_md5.hash(salt+temp)
                hashedWord = salt + ':' + hashedWord
                if(hashedWord == hashedPass):
                    isFound= True
                    print(f'Password for {user} is {temp}')
                    #write to text file
                    writeText(user, temp, 'crackedPasswordsP2B.txt')
                    return isFound
    return isFound

# Method to check the combination of the number list
def checkNumCombo(user, salt, numList, hashedPass, isFound):
    fullCombo = list(itertools.permutations(numList,8))
    for num in fullCombo:
        temp = convert(num)
        hashedWord = hex_md5.hash(salt+temp)
        hashedWord = salt + ':' + hashedWord
        if(temp == '16083058'):
            raise Exception('Found')
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {temp}')
            #write to text file
            writeText(user, temp, 'crackedPasswordsP2B.txt') 

            return isFound
   
    return isFound

# Method to check the combination of the word and the common password file
def checkCombo(user, word, salt, hashedPass, f2, isFound):
    for j in f2:
        temp = word+j
        hashedWord = hex_md5.hash(salt+temp)
        hashedWord = salt + ':' + hashedWord

        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {temp}')
            #write to text file
            writeText(user, temp, 'crackedPasswordsP2B.txt')
            return isFound
    return isFound

# Method to write to text file crackedPasswords
def writeText(user, word,file):    
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
    
    Assign1P2A(f2, f3)