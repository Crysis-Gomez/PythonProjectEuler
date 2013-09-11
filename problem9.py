import time
import math

class specialTriplet:

    def __init__(self):
        self.found = False
        self.start()
        
    def start(self):
        t1 = time.clock()
        self.calculate()
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))

    def calculate(self):
        for x in range(0,500):
            for y in range(0,500):
                if self.found is True:
                    break
                count = x*x
                count2 = y*y
                count3 = count + count2
                countsqrt = math.sqrt(count3)
                count4 = countsqrt + x + y
                if count4 == 1000 and self.found is False:
                    self.found = True
                    print(countsqrt*x*y)
                    break;
   
a = specialTriplet()
