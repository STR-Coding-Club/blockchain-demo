from hash import hash
from random import seed
from random import randint
import time

def proof_of_work(block):
    seed(1)
    ans = 0
    # print('Looking for value that will make the hash 0:')
    while (hash(block, ans) % 5) != 0:
        #print(f'Trying {ans}...', end="")
        ans = randint(0, 256)
    print(f'\nValue found: {ans}')
    time.sleep(0.5)
    return ans
