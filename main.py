import block
from hash import hash
import miner

def main():
    genesis_transactions = ("A sent B 123 STR", "B sent A 133 STR", " B sent C 324 STR")
    genesis_block = block.create_block(0, 0, genesis_transactions)
    block1_transactions = ("A sent C 123 STR", "D sent F 133 STR", " B sent C 34 STR")
    block1 = block.create_block(1, miner.proof_of_work(genesis_block), block1_transactions)
    print(genesis_block)
    print(hash(genesis_block))
    print(miner.proof_of_work(genesis_block))
    print(block1)
    print(hash(block1))
    print(miner.proof_of_work(block1))


if __name__ == "__main__":
    main()