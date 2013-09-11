import time

class Palidrone:

    def __init__(self):
        self.value = 0
        self.palindrone()

    def palindrone(self):
        t1 = time.clock()
        calc =  [self.results(x * y) for x in range(1000,0,-1) for y in range(1000,0,-1)]
        print(self.value)
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))

    def results(self,count):
        results1 = str(count)
        results2 = results1[::-1]
        if count > self.value and results1 == results2:
            self.value  = count

a = Palidrone()

