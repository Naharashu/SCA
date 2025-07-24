import rlea

# Declarations

global str, cbm
str = 'AAAAABBCCCCC666668990000'
cbm = {}

class TreeNode:
    def __init__(self,freq, data, left, right):
        self.freq = freq
        self.data = data
        self.left = left
        self.right = right
        
    
def genTree(mapping):
    keyset = mapping.keys()
    priorityQ = []
    
    for c in keyset:
        node = TreeNode(mapping[c], c, None,None)
        priorityQ.append(node)
        priorityQ = sorted(priorityQ, key= lambda x:x.freq)
        
    while len(priorityQ) > 1:
        first = priorityQ.pop(0)
        second = priorityQ.pop(0)
        mergeNode = TreeNode(first.freq + second.freq, '-', first, second)
        
        priorityQ.append(mergeNode)
        priorityQ = sorted(priorityQ, key= lambda x:x.freq)
    
    return priorityQ.pop()

def setBinCode(node, str):
    if not node is None:
        if node.left is None and node.right is None:
            cbm[node.data] = str
        
        str += '0'
        setBinCode(node.left, str)
        str = str[:-1]
        
        str += '1'
        setBinCode(node.right, str)
        str = str[:-1]

          
def encode(str):
    mapping = {}
    for c in str:
        if not c in mapping:
            mapping[c] = 1
        else:
            mapping[c]+=1
    root = genTree(mapping)
    
    setBinCode(root, '')
    
    print(' char | code ')
    for char in mapping:
        print(' %-4r |%12s' % (char, cbm[char]))
        
    s= ''
    for c in str:
        s += cbm[c]
    return s

def pack(data):
    while len(data) % 8 != 0:
        data += '0'
    bdata = bytearray()
    for i in range(0, len(data)):
        byte = data[i:i+8]
        bdata.append(int(byte, 2))
    return bytes(bdata)

def unpack(data):
    return ''.join(f'{byte:08b}' for byte in data)
        
data = encode(rlea.rle_encode(str))
print(pack(data))
print(str)
        
        
