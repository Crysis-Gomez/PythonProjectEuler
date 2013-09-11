import time

class searchPrime:

    def __init__(self):
        self.start()

    def primeChecker(self,num):
        isPrime = True
        n = int(num *0.5)
        for x in range(2,n+1):
            if num % x == 0:
               isPrime = False
               break    
        return isPrime

    def start(self):
        t1 = time.clock()
        self.search(10001)
        t2 = time.clock()
        print('Time: %0.6f' % (t2-t1))
        
    def search(self,num):
        count = 0
        number = 1
        while count != num:
            number +=1
            if number == 2 or number == 3:
                count += 1
            else:    
                if self.primeChecker(number) == True:
                    count += 1

        print(number)  


a = searchPrime()
