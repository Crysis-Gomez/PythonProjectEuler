import time
import math


class LatticePath:

    def __init__(self):
        self.grid = 20
        t1 = time.clock()
        self.path()
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))
        
    def path(self):
       arr =[]
       for x in range(0,self.grid+1):
           arr.append([])
           arr[0].append(1)
           arr[x].append(1)
       self.calc(arr,1)
       print(arr[self.grid][self.grid])
    
    def calc(self,array,count):
         for x in range(0,self.grid):
            if x + 1 > self.grid:
                continue
            array[count].append(array[count][x] + array[count-1][x+1])
         if count < self.grid:
             self.calc(array,count+1)
        

a = LatticePath()
