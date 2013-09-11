import time
import math

class primeUndertwoMillion:

    def __init__(self):
        self.start()

    def primeChecker3(self,num):
        if num%1 or num <2:
            return False
        if num%2==0:
            return(num==2)
        if num%3==0:
            return(num==3)

        m = math.sqrt(num)
        m = int(m)

        for x in range(5,m+1,6):
            if num%x == 0:
                return False
            if num%(x+2) == 0:
                return False
        
        return True

    def start(self):
        t1 = time.clock()
        self.calculate()
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))

    def calculate(self):
        primes = (x for x in range(2,2000000) if self.primeChecker3(x))
        print(sum(primes))
   
a = primeUndertwoMillion()
