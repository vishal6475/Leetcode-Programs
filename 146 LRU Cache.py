# Definition for an LRU cache node.
class Node(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.itemsMap = dict()
        self.front = None # to remove least recently used nodes
        self.back = None # to add nodes
        
    def printNodes(self):
        print()
        print('Printing Nodes: Capacity is-', len(self.itemsMap), 'Front:', self.front.value , 'Back:', self.back.value, self.front.prev, self.front.next, self.back.prev, self.back.next)
        for k in self.itemsMap:
            print(k, ':', self.itemsMap[k].value, end=", ")
        print()
        print('ListL')
        ptr = self.front
        while ptr:
            print(ptr.value, end=' ')
            ptr = ptr.next
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print()
        print("Getting item:", key)
        
        if key in self.itemsMap:
            curr = self.itemsMap[key]    
            if curr.prev == None and curr.next != None:
                self.front = curr.next
                self.front.prev = None
            elif curr.prev != None and curr.next != None:     
                curr.prev.next = curr.next       
                
            self.back.next = curr
            curr.prev = self.back
            curr.next = None
            self.back = curr            
            
            return self.itemsMap[key].value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print()
        print()
        if key in self.itemsMap: # item already in cache
            print('Updaing item:', key, value, "(", self.itemsMap[key].value, ")")
            curr = self.itemsMap[key]            
            curr.value = value
            if curr.next != None:
                if curr.prev == None:
                    self.front = curr.next
                    self.front.prev = None
                elif curr.prev != None:     
                    curr.prev.next = curr.next       
                    
                self.back.next = curr
                curr.prev = self.back
                curr.next = None
                self.back = curr
                #self.itemsMap[key] = curr
        elif len(self.itemsMap) < self.capacity: # insert item, cache is NOT full
            print('Inserting new item:', key, value)
            n = Node(key, value)
            if len(self.itemsMap) == 0:
                self.front = n
                self.back = n
            else:
                self.back.next = n
                n.prev = self.back
                self.back = n
            self.itemsMap[key] = n
        else: # insert item, cache IS full
            print('Deleting to insert new:', key, value)
            if self.capacity == 1:
                del self.itemsMap[self.front.key]
                self.front.key = key
                self.front.value = value
                self.itemsMap[key] = self.front
            else:
                del self.itemsMap[self.front.key]
                self.front = self.front.next
                self.front.prev = None            
                
                n = Node(key, value)
                self.back.next = n
                n.prev = self.back
                n.next = None
                self.back = n
                    
                self.itemsMap[key] = n
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(10)

do = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
for it in do:
    input()
    if len(it) == 2:
        obj.put(it[0], it[1])
        obj.printNodes()
    else:

        print(obj.get(it[0]))
        obj.printNodes()
        
        
