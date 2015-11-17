from twisted.internet import reactor, defer

def multiplyByThree(x):
    
    d = defer.Deferred()
    reactor.callLater(2, d.callback, x * 3)
    return d

def printData(d):
    print(d)

d = multiplyByThree(3)
d.addCallback(printData)

# manually set up the end of the process by asking the reactor to
# stop itself in 4 seconds time
reactor.callLater(4, reactor.stop)
# start up the Twisted reactor (event loop handler) manually
reactor.run()