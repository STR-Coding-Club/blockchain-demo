import hashlib, json

# def hash(to_hash):
#     h = hashlib.md5()
#     h.update(bytes(str(to_hash), 'utf-8'))
#     return h.hexdigest()

def hash(to_hash, proof_of_work):
    s = ''.join(str(_) for _ in (to_hash[:2])) #Add block number and previous hash to string
    s += ''.join(str(_) for _ in (to_hash[2])) #Add list of transactions to string

    if proof_of_work:
        #if the hash function is a proof of work
        s += str(proof_of_work)
    hash = 32
    for c in s:
        hash = (hash+ord(c)) % 256
    return hash



