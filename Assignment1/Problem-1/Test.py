import hashlib

hash = input('Enter Hash: ')
print(hash)

h = hashlib.md5(hash.encode('utf-8')).digest()
print(h)