def create_block(block_num: int,
                 previous_hash: str,
                 transactions: tuple):

    block = (block_num, previous_hash, transactions)
    return block
