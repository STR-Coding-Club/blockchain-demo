import hashlib, json

# def hash(to_hash):
#     h = hashlib.md5()
#     h.update(bytes(str(to_hash), 'utf-8'))
#     return h.hexdigest()

def hash(to_hash):
    s = ''.join(str(to_hash))
    hash = 32;
    for c in s:
        hash = (hash+ord(c))%256
    return hash



