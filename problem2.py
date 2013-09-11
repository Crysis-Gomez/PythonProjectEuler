import time


class EvenFibonacci:

    def __init__(self):
        self.value = 0
        self.start()
        
    def start(self):
        t1 = time.clock()
        self.calculate(0,1,4000000)
        print(self.value)
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))

    def calculate(self,num,num2,n):
        num,num2 = num2,num+num2
        if num2 % 2 == 0:
           self.value += num2
        if num2 <= n :
            self.calculate(num,num2,n)
        
a = EvenFibonacci()
