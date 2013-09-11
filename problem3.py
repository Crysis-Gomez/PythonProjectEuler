import time

class Largestprimefactor:

    def __init__(self):
        self.start()

    def start(self):
        t1 = time.clock()
        self.calculate(600851475143)
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))
        
    def calculate(self,n):
        y = 2
        while y * y <= n:
            if n % y == 0:
                n = n/y
            if(n != 1 and y* y >= n):
                print(int(n))    
            y+=1


a = Largestprimefactor()

