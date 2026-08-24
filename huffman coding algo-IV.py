import heapq

class node:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self,other):
        return self.freq<other.freq

def huffman(text):
    freq={}

    for char in text:
        freq[char]=freq.get(char,0)+1

    heap=[]
    for ch,f in freq.items():
        heapq.heappush(heap,node(ch,f))

    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)

        new=node(None,right.freq+left.freq)
        new.left=left
        new.right=right

        heapq.heappush(heap,new)

    root=heap[0]
    codes={}

    def generate(node,code=""):
        if node.char is not None:
            codes[node.char]=code

            return 
        generate(node.left,code+"0")
        generate(node.right,code+"1")
    generate(root)
    return codes

text="AABBBCDD"
codes=huffman(text)
print("HUFFMAN CODES:")
for ch,r in codes.items():
    print(ch,":",r)

encoded=""
for ch in text:
    print(encoded+codes[ch],end=" ")