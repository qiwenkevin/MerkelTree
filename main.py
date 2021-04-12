import hashlib

with open('block.in', 'r') as reader:
    block = reader.readlines()

num_transactions = int(block[0].rstrip().split(":")[1])
merkle_root = block[4].rstrip().split(":")[1]
transactions = []
for i in range(num_transactions):
    transactions.append(block[12 + i].rstrip().split(":"))
merkle_tree = ["" for j in range(num_transactions * 4)]
num_layers = 0
while num_transactions > 2 ** num_layers:
    num_layers += 1
    for i in range(num_transactions):
        merkle_tree[2 ** num_layers + i] = hashlib.sha256((transactions[i][0] + transactions[i][1] + transactions[i][2]).encode()).hexdigest()
    for i in range(2 ** num_layers - 1, 0, -1):
        merkle_tree[i] = hashlib.sha256((merkle_tree[2*i]+merkle_tree[2*i+1]).encode()).hexdigest()
if merkle_root == merkle_tree[1]:
    print("Correct")
else:
    print("Tampered")

