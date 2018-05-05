class MinHeap:
    
    """ binární halda, implementovaná pomocí metod """
    def __init__(self):
        self.heap = [] # indexujeme od nuly
 
    def bubble_up(self,i):
        """ probublá prvek 'i', zajistí splnění vlastnosti haldy """
        while i>0:
            j=(i-1)//2 # index rodiče  
      
            if self.heap[i] >= self.heap[j]:
                break
        
            self.heap[j],self.heap[i]=self.heap[i],self.heap[j]
            i = j
 
    def insert(self,k):
        self.heap+=[k]
        self.bubble_up(len(self.heap)-1)
 
    def peek(self):
        """ vrátí nejmenší prvek """
        return self.heap[0]
 
    def size(self):
        return len(self.heap)
 
    
    def is_empty(self):
      return self.size()==0 
 
    def bubble_down(self,i):
        n=self.size()
    
        while 2*i+1 < n:
            
            j=2*i+1 # zjisti index menšího syna
            
            if j+1 < n and self.heap[j] > self.heap[j+1]:
                j+=1
            if self.heap[i]>self.heap[j]:
                self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
            i=j

    def pop(self):
        """ odeber a vrať nejmenší prvek """
        element=self.heap[0]
        self.heap[0]=self.heap.pop() # smaž poslední prvek
        self.bubble_down(0)
        return element

    def delete( self, i ):
        if ( len(self.heap) == 0 ) or (i > len(self.heap)-1):
            return

        element = self.heap[i]    
        self.heap[i] = self.heap.pop()

        self.bubble_down( i )

        return element

pole=[10,21,7,11,31,6,1,-11,31,42,-12,80,25,-7,-12,9,14]
min_heap = MinHeap()

for element in pole:
    min_heap.insert( element )

print( min_heap.heap )
min_heap.delete( 2 )
print( min_heap.heap )
        
