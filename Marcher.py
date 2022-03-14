


class Heap():
    '''minheap'''

    def __init__(self):
        self.minheap = []
        
        
        
    def insert(self, val):
        self.minheap.append(val)
        last_leaf = len(self.minheap) - 1
        p_index = (last_leaf - 1) // 2
        while last_leaf > 0 and self.minheap[p_index][2] > self.minheap[last_leaf][2]:
            (self.minheap[p_index], self.minheap[last_leaf]) = (self.minheap[last_leaf], self.minheap[p_index])
            last_leaf = p_index
            p_index = (last_leaf - 1) // 2
    
    
    def heapify(self, i, size):
        maxi = i
        if(2 * i + 1 < size and self.minheap[2*i+1][2] < self.minheap[i][2]):
            maxi = 2 * i + 1
        if(2 * i + 2 < size and self.minheap[2 * i + 2][2] < self.minheap[maxi][2]):
            maxi = 2 * i + 2
        if (maxi != i):
            self.minheap[i], self.minheap[maxi] = self.minheap[maxi], self.minheap[i]
            self.heapify(maxi, size)
        
        
    def decrease_priority(self, index, P):
        if P > self.minheap[index][2]:
            return
        self.minheap[index][2] = P
        
        while self.minheap[(index-1) // 2][2] > self.minheap[index][2] and index != 0:
            self.minheap[(index-1) // 2], self.minheap[index] = self.minheap[index], self.minheap[(index-1) // 2]
            index = (index-1) // 2
            
            
    def extract_min(self):

        ret = self.minheap[0]

        last = self.minheap.pop()

        if (len(self.minheap) > 0):
            self.minheap[0] = last
            self.heapify(0, len(self.minheap))
        return ret




class Marcher:

    @staticmethod
    def findPath(mp, weight):
        """
        Input: 




                                                        (x, y-1)
                                                            ^
                                                            |
                                        (x-1, y) <------ (x, y) ------> (x+1, y)
                                                            |
                                                            v
                                                        (x, y+1)


           




        """
        PQ = Heap()
        PQ.insert([0,0,0])
        d = {}
        pred = {}
        d[(0,0)] = 0

        
        while(PQ.minheap != []):
            v = PQ.extract_min()
            x = v[0]
            y = v[1]
            
            
            
            
            if((x, y) == (mp.sx-1, mp.sy-1)):
                break
            
            
            u = (x, y-1)
            if(not(u[0] < 0 or u[1] < 0) and not(u[0] >= mp.sx or u[1] >= mp.sy)):
                
                
                
                if((u[0], u[1]) not in d):
                    PQ.insert([u[0],u[1], float("inf")])
                    d[(u[0], u[1])] = float("inf")
                    
                    
                    
                
                    
                    
                if d[(x, y)] + weight(mp, (x, y), u) < d[u]:
                    item = [u[0], u[1]] + [d[u]]
                    index = PQ.minheap.index(item)
                    PQ.decrease_priority(index, d[(x, y)] + weight(mp, (x, y), u))
                    d[u] = d[(x, y)] + weight(mp, (x, y), u)
    
                    pred[u] = (x, y)

                    
                    
                
                
            u = (x+1, y)
            if(not(u[0] < 0 or u[1] < 0) and not(u[0] >= mp.sx or u[1] >= mp.sy)):
                
                if((u[0], u[1]) not in d):
                    PQ.insert([u[0],u[1], float("inf")])
                    d[(u[0], u[1])] = float("inf")
                

                
                if d[(x, y)] + weight(mp, (x, y), u) < d[u]:
                    item = [u[0], u[1]] + [d[u]]
                    index = PQ.minheap.index(item)
                    PQ.decrease_priority(index, d[(x, y)] + weight(mp, (x, y), u))
                    d[u] = d[(x, y)] + weight(mp, (x, y), u)
    
                    pred[u] = (x, y)
                    

                  
                    
                    
                
                
            u = (x, y+1)
            if(not(u[0] < 0 or u[1] < 0) and not(u[0] >= mp.sx or u[1] >= mp.sy)):
                
                
                if((u[0], u[1]) not in d):
                    PQ.insert([u[0],u[1], float("inf")])
                    d[(u[0], u[1])] = float("inf")
                
            
                    
                    

                    
                    
                
                if d[(x, y)] + weight(mp, (x, y), u) < d[u]:
                    item = [u[0], u[1]] + [d[u]]
                    index = PQ.minheap.index(item)
                    PQ.decrease_priority(index, d[(x, y)] + weight(mp, (x, y), u))
                    d[u] = d[(x, y)] + weight(mp, (x, y), u)
    
                    pred[u] = (x, y)
                    
               

                
            u = (x-1, y)
            if(not(u[0] < 0 or u[1] < 0) and not(u[0] >= mp.sx or u[1] >= mp.sy)):
            
                if((u[0], u[1]) not in d):
                    PQ.insert([u[0],u[1], float("inf")])
                    d[(u[0], u[1])] = float("inf")
                    
                    
                
                
                if d[(x, y)] + weight(mp, (x, y), u) < d[u]:
                    item = [u[0], u[1]] + [d[u]]
                    index = PQ.minheap.index(item)
                    PQ.decrease_priority(index, d[(x, y)] + weight(mp, (x, y), u))
                    d[u] = d[(x, y)] + weight(mp, (x, y), u)
    
                    pred[u] = (x, y)
                        
 
                    

                    
                    
        u = (mp.sx-1, mp.sy-1)
        
        while(pred[u] != (0,0)):
            mp.path.append(u)
            u = pred[u]
        mp.path.append(u)
        mp.path.append((0,0))
        mp.path.reverse()

        
        
        
        

        cost = d[mp.sx-1, mp.sy-1]
        return round(cost,5)  


        
        






