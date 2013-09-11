import time
import math

class largeSum:

    def __init__(self):
        self.number_string = ""
        self.start()
                
    def start(self):
        t1 = time.clock()
        self.calculate()
        t2 = time.clock()
        print(self.number_string)
        print('Time: %0.6f' % (t2-t1))

    def calculate(self):
        f = open('euler.txt')
        lines = f.readlines()
        arrayList = []
        
        for l in range(0,len(lines)):
            arrayList.append(int(lines[l]))
                
        totalSum = sum(arrayList)
        f.close()
        for x in range(0,10):
            self.number_string += str(totalSum)[x]
   
a = largeSum()
