
class Fib(object):
    
    def __init__(self):
        self.a = 0
        self.b = 1
     
    def next(self):

        while True :
            yield self.a
            self.a, self.b = self.b, self.a + self.b

fib = Fib()

for x in fib.next():
    print ("Fib :: next : %s" %  x)