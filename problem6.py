import time

class squareDifference:

    def __init__(self):
        self.start()
   
    def start(self):
        t1 = time.clock()
        self.calculate(0,100)
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))
        
    def calculate(self,num,num2):
        count = 0
        count2 = 0
        num2 = num2+1
        for x in range(num,num2):
            count2 += x
            count  += x*x

        count2 = count2 * count2
        count = count2 - count
        print(count)


a = squareDifference()
