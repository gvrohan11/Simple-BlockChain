'''

NeuralCoin (NC)

t1: Anna sends Bob 2 NC # Changing the transaction of one will change the hash code of that transaction, which changes the whole linked list
t2: Bob sneds Daniel 4.3 NC
t3: Mark sends Charlie 3.2 NC

SHA256

B1 ("AAA", t1, t2, t3) -> 76fd89, B2 (76fd89, t4, t5, t6) -> 8923ff, B3 (8923ff, t7)

NeuralHash()

'''

import hashlib

class NeuralCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Robert sends 2 NC to Michael"
t2 = "Phoebe sends 4.1 NC to Michael" # Changing the amount sent will generate a new hash
t3 = "Bob sends .3 NC to Phoebe"
t4 = "Rachel sends .024 NC to Robert"
t5 = "Michael sends 10 NC to Chuck"
t6 = "Michael sends 4 NC to David"

initial_block = NeuralCoinBlock("Initial String", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)


second_block = NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)
