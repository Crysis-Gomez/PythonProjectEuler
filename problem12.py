import time
import math

class divisibleTriangular:

    def __init__(self):
        self.number = 0
        self.i = 1;
        self.start()
  

    def divisors(self,x):
        num = int(x)
        sqrtNumber = int(math.sqrt(num))
        numberOfDivisors = 0
        for l in range(1,sqrtNumber):          
            if num % l == 0:
                    numberOfDivisors+= 1
        numberOfDivisors *=2
        return numberOfDivisors

        
    def start(self):
        t1 = time.clock()
        self.calculate()
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))

    def calculate(self):
        while self.divisors(self.number) < 500:
            self.number += self.i;
            self.i+=1
        else:
            print(self.number)
   
a = divisibleTriangular()
