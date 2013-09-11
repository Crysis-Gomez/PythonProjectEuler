import time
import math

class longestCollatzSequence:

    def __init__(self):
        self.chainCount = 0
        self.currentCount = 1
        self.chainNumber = 1
        self.start()
                
    def start(self):
        t1 = time.clock()
        self.calculate()
        t2 = time.clock()
        print(self.chainNumber)
        print('Time: %0.6f' % (t2-t1))

    def calculate(self):
        for l in range(1,1000000):
            num = self.evenOrOddsCalculator(l)
            self.currentCount = 1
            while num != 1:
                num = self.evenOrOddsCalculator(num)
            else:
                if  self.currentCount > self.chainCount:
                    self.chainCount = self.currentCount 
                    self.chainNumber = l  
    
    def evenOrOddsCalculator(self,x):
        self.currentCount +=1;
        if x % 2 == 0:
            num = x/2
        else:
            num = 3*x+1
        return num
   
a = longestCollatzSequence()
