import time

class SmallestMultiple:

    def __init__(self):
        self.inc = 1
        self.num = 1
        self.start()
   

    def start(self):
        t1 = time.clock()
        self.multiple()
        t2 = time.clock()
        print(self.inc)
        print('Time: %0.6f' % (t2-t1))
        
    def multiple(self):
        for i in range(1,20):
           while self.num % i != 0:
              self.num += self.inc
           self.inc = self.num


a = SmallestMultiple()
