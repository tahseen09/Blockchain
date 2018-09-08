import hashlib #library for hashing
import pickle #to convert data to bytecode
#defining block
block={
    'transactions':[
        {
            'from':'A',
            'to':'B',
            'amount':10
        },
        {
            'from':'B',
            'to':'A',
            'amount':10
        },
    ],
}
n=hashlib.sha3_256()                     #calculating hash
n.update(pickle.dumps(block))
n.digest()
n.hexdigest()
#top_block will always be the last block
top_block={
    'transactions':[
        {
            'from':'A',
            'to':'B',
            'amount':10
        },
        {
            'from':'B',
            'to':'A',
            'amount':10
        },
    ],
    'last_block':n.hexdigest(),
    'nonce':0
}
o=hashlib.sha3_256()
o.update(pickle.dumps(top_block))
o.digest()
o.hexdigest()
difficulty=2   #increased difficulty in terms of mining
difficulty_string=''.join(['0' for x in range(0,difficulty)])
nonce=1
top_block['nonce']=nonce
p=hashlib.sha3_256()
while p.hexdigest()[:difficulty] != difficulty_string:
    nonce=nonce+1
    top_block['nonce']=nonce
    p.update(pickle.dumps(top_block))
    print(nonce, p.hexdigest())
    
    