import block
from hash import hash
import miner


def main():
    genesis_transactions = ["A sent B 124 STR", "B sent A 233 STR", " B sent C 324 STR"]
    genesis_block = block.create_block(0, 0, genesis_transactions)

    block1_transactions = ["A sent C 123 STR", "D sent F 133 STR", " B sent C 34 STR"]
    block1 = block.create_block(1, miner.proof_of_work(genesis_block), block1_transactions)

    print(f'Genesis Block: {genesis_block}')
    print(f'Genesis Block Hash: {hash(genesis_block, False)}')

    print(f'Block 1: {block1}')
    print(f'Block 1 Hash: {hash(block1, False)}')

    print(f'Block 1 proof of work value: {miner.proof_of_work(block1)}')


if __name__ == "__main__":
    main()