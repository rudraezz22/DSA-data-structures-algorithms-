class Hash:
    def __init__(self,size=5):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]

    def hashing(self,key):
        return hash(key)%self.size

    def insert(self,key,value):
        hash_key = self.hashing(key)
        for i in self.hash_table[hash_key]:
            if i[0]==key:
                i[1] = value
                return
        else:
            self.hash_table[hash_key].append([key,value])
    
    def get(self,key):
        hash_key = self.hashing(key)
        for i in self.hash_table[hash_key]:
            if i[0]==key:
                return i[1]
        else:
            return None
        
    def delete(self,key):
        hash_key = self.hashing(key)
        for i,j in enumerate(self.hash_table[hash_key]):
            if j[0]==key:
                del self.hash_table[hash_key][i]
                return True
        else:
            return False
        

    def display(self):
        for i,j in enumerate(self.hash_table):
            print(i,j)



h1 = Hash()
h1.insert("a",1)
h1.insert("b",2)
h1.insert("c",3)
h1.insert("d",4)
h1.insert("e",5)
h1.insert("f",6)
h1.insert("g",7)
h1.insert("h",8)
print(h1.get("c"))
h1.display()

h1.delete("a")
h1.display()