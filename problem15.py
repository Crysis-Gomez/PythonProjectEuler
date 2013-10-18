import time
import math


class LatticePath:

    def __init__(self):
        self.grid = 20
        self.path()
        
    def path(self):
       arr =[]
       count = 1
       for x in range(0,self.grid+1):
           arr.append([])
           arr[0].append(1)
           arr[x].append(1)

       self.calc(arr,count)
       print(arr[self.grid][self.grid])
    
    def calc(self,array,count):
         for x in range(0,self.grid):
            if x + 1 > self.grid:
                continue
            r = array[count][x] + array[count-1][x+1]
            array[count].append(r)
         
         if count < self.grid:
             self.calc(array,count+1)
        

a = LatticePath()
