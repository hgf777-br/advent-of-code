import hashlib

data = 'ckczppom'

n = 1

while(True):
    hash = hashlib.md5((data + str(n)).encode())
    if hash.hexdigest().startswith('000000'):
        print(hash.hexdigest(), n)
        break
    n += 1