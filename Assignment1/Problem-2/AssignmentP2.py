
from passlib.hash import hex_md5

from tqdm import tqdm
import itertools

def Assign1P2A(f,f3):
    
    # Convert the word list to a list
    wordList = list(f3)
    
    # Iterate through the file
    for line in f:
        
        # Split the line into user and hashed password
        splitLine = line.split(':')
        user = splitLine[0]
        hashedPass = splitLine[1]
        
        # Remove the new line character
        hashedPass = hashedPass.replace('\n',"")
        
        # Call the crackHash method
        crackHash(user, hashedPass, wordList)

def crackHash(user, hashedPass, f2):
    isFound = False
    numList = ['0','1','2','3','4','5','6','7','8','9']
    maxLen = 10
    checkNum = False
    
    print(f'Cracking password for {user}...')
    
    # Iterate through the word list
    for word in tqdm(f2):
        
        # Strip the word and remove the new line character
        word = word.strip()
        word = word.replace('\n',"")
        
        # Call the checkWord method to check the word list
        if checkWord(word, user, hashedPass, isFound):
            isFound = True
            break
        
        # Call the checkNumList method to check the combination of the word and the number list
        elif checkNumList(user, word, hashedPass, numList, isFound, maxLen):
            isFound = True
            break
        
        # Call the checkNumCombo method to check the combination of the number list
        elif checkNum == False:
            checkNum = True
            if checkNumCombo(user, numList, hashedPass, isFound):
                isFound = True
                break
            
        # Call the checkCombo method to check the combination of the word and the common password file
        if checkCombo(user, word, hashedPass,f2, isFound):
            isFound = True
            break
        
    # if whole list is searched and the password is never found, then print that
    if(isFound == False):
        print(f'Password for {user} not in file')

# Method to check the word list
def checkWord(word, user, hashedPass, isFound):
    
    # Check if the word is greater than 5 characters
    if(len(word)>=5):
        
        # Hash the word
        hashedWord =  hex_md5.hash(word)
        
        # Check if the hashed word is equal to the hashed password
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {word}')

            #write to text file
            writeText(user, word,'crackedPasswordsP2A.txt')
            return isFound
    return isFound

# Method to check the combination of the word and the number list
def checkNumList(user, word, hashedPass, numList, isFound, maxLen):
    
    # Check if the length of the word is greater than 5 and less than or equal to 10
    if len(word)>5 and len(word)<=maxLen:
        
        # Find the difference between the length of the word and 10
        diff = maxLen-len(word)
        
        # Check if the difference is not equal to 0
        if diff != 0:
            
            # Find the combination of the number list
            combo = list(itertools.permutations(numList, diff))
            
            # Iterate through the combination
            for i in combo:
                
                # Convert the tuple to string
                x = convert(i)
                
                # Concatenate the word and the number list
                temp = word+x
                
                # Hash the word
                hashedWord = hex_md5.hash(temp)
                
                # Check if the hashed word is equal to the hashed password
                if(hashedWord == hashedPass):
                    isFound= True
                    print(f'Password for {user} is {temp}')
                    
                    #write to text file
                    writeText(user, temp, 'crackedPasswordsP2A.txt')
                    return isFound
    return isFound

# Method to check the combination of the number list
def checkNumCombo(user, numList, hashedPass, isFound):
    
    # Find the combination of the number list
    fullCombo = list(itertools.permutations(numList,8))
    
    # Iterate through the combination
    for num in fullCombo:
        
        # Convert the tuple to string
        temp = convert(num)
        
        # Hash the word
        hashedWord = hex_md5.hash(temp)
        
        # Check if the hashed word is equal to the hashed password
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {temp}')
            
            #write to text file
            writeText(user, temp, 'crackedPasswordsP2A.txt') 
            
            return isFound
   
    return isFound

# Method to check the combination of the word and the common password file
def checkCombo(user, word, hashedPass, f2, isFound):
    
    # Iterate through the common password file
    for j in f2:
        
        # Concatenate the word and the common password word
        temp = word+j
        
        # Hash the word
        hashedWord = hex_md5.hash(temp)
        
        # Check if the hashed word is equal to the hashed password
        if(hashedWord == hashedPass):
            isFound= True
            print(f'Password for {user} is {temp}')
            
            #write to text file
            writeText(user, temp, 'crackedPasswordsP2A.txt')
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
    
    Assign1P2A(f, f3)