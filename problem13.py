import time
import math
from urllib.request import urlopen
import urllib.request

localFile = open('file.html', 'w')

class largeSum:

    def __init__(self):
        self.number_string = ""
        self.start()
    
    def start(self):
        t1 = time.clock()
        self.calculate()
        t2 = time.clock()
        print(self.number_string)
        print('Time: %0.6f' % (t2-t1))

    def calculate(self):
        u = urlopen('https://raw.github.com/Crysis-Gomez/PythonProjectEuler/master/euler.txt')        
        lines = u.readlines()
        arrayList = []
        
        for l in range(0,len(lines)):
            arrayList.append(int(lines[l]))
                
        totalSum = sum(arrayList)
        u.close()
        for x in range(0,10):
            self.number_string += str(totalSum)[x]
   
a = largeSum()
