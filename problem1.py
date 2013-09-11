import time

def calculate(index):
    t1 = time.clock()
    x = sum([x for x in range(0, index) if x % 3 == 0 or x % 5 ==0])
    t2 = time.clock()
    print(x)
    print('time: %0.6f' % (t2-t1))
    
calculate(1000)
