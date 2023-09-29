import crypt
from tqdm import tqdm

def Assign1P2A(f, f3):
    wordList = list(f3)




if __name__ == '__main__':
    
    file = 'Assignment1\Problem-2\UnsaltedPassTable.txt'
    file2 = 'Assignment1\Problem-2\SaltedPassTable.txt'
    file3 = 'Assignment1\Problem-2\words.txt'
    
    f = open(file, 'r')
    f2 = open(file2, 'r')
    f3 = open(file3, 'r')
    
    Assign1P2A(f, f3)