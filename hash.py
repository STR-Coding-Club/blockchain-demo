import hashlib, json

def hash(to_hash):
    h = hashlib.md5()
    h.update(bytes(str(to_hash), 'utf-8'))
    return h.hexdigest()

