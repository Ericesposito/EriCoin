from time import time

from utility.printable import Printable


class Block(Printable):
    """Class constructor for individual blocks of the blockchain.

    Attributes:
        :index: The index of this block
        :previous_hash: The hash of the previous block in the blockchain
        :transactions: A list of transactions in the block
        :proof: The proof of work value for this block
        :timestamp: Automatically generated timestamp of the blocks
    """

    def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if timestamp is None else timestamp
        self.transactions = transactions
        self.proof = proof
