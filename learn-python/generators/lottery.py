import random

class MockRandom(object):
    
    def __init__(self, selected_array):
        self.selected = selected_array
     
    def next(self):
        for x in xrange(0, len(self.selected)):
            yield self.selected[x]

class RealRandom(object):
    
    def __init__(self, lowest, highest, count):
        self.selected = random.sample(range(lowest, highest), count)
     
    def next(self):
        for x in xrange(0, len(self.selected)):
            yield self.selected[x]

mock = MockRandom([1,2,3,4,5,6])
real = RealRandom(1,49,6)

for x in mock.next():
    print ("Mock :: next : %s" %  x)

print("\n")

for x in real.next():
    print ("Real :: next : %s" %  x)

