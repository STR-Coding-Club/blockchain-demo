from hash import hash
import block
from random import seed
from random import randint

def proof_of_work(block):
    seed(1)
    ans = 0;
    while(((hash(block)+ans)%256)!=0):
        ans = randint(0,256)
    return ans


