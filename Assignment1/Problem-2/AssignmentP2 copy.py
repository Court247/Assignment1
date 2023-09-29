from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

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
    numList = [0,1,2,3,4,5,6,7,8,9]
    maxLen = 10
    checkNum = False
    for word in tqdm(f2):
        print(word)
        word = word.strip()
        word = word.strip('\n')
        if(len(word)>=5):
            print('first If')
            hashedWord = md5_crypt.hash(word)
            if(hashedWord == hashedPass):
                isFound= True
                print(f'Password for {user} is {temp}')
                #break

        elif len(word)>=5 and len(word)<=maxLen:
            print('second If')
            diff = maxLen-len(word)
            combo = list(itertools.combinations(numList, diff))
            for i in combo:
                temp = word+str(i)
                print(temp)
                hashedWord = md5_crypt.hash(temp)
                if(hashedWord == hashedPass):
                    isFound= True
                    print(f'Password for {user} is {temp}')
                    #break
        elif checkNum:
            checkedNum = True
            print(' in else')
            fullCombo = list(itertools.combinations(numList,8))
            for num in tqdm(fullCombo):
                temp = str(num)
                hashedWord = md5_crypt.hash(temp)
                
                if(hashedWord == hashedPass):
                    isFound= True
                    print(f'Password for {user} is {temp}')
                    #break
        for j in tqdm(f2):
            temp = word+j
            print(temp)
            hashedWord = md5_crypt.hash(temp)
            if(hashedWord == hashedPass):
                isFound= True
                print(f'Password for {user} is {temp}')
                #break
        
    # if whole list is searched and the password is never found, then print that
    if(isFound == False):
        print('here')
        print('Password not in file')




if __name__ == '__main__':
    
    file = 'Assignment1/Problem-2/UnsaltedPassTable.txt'
    file2 = 'Assignment1/Problem-2/SaltedPassTable.txt'
    file3 = 'Assignment1/Problem-2/words.txt'
    
    f = open(file, 'r', encoding="utf8")
    f2 = open(file2, 'r', encoding="utf8")
    f3 = open(file3, 'r', encoding="utf8")
    
    Assign1P2A(f, f3)