from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):

    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self._send("What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        name = name.decode("utf-8")
        if name in self.users:
            self._send("Name taken, please choose another.")
            return
        self._send(str.format("Welcome, {}!" ,name))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = str.format("<{}> {}", self.name, message.decode("utf-8"))
        # protocol is not a good name here!
        for name, protocol in self.users.items():
            if protocol != self:
                protocol._send(message)

    def _send(self, message):
         self.sendLine(str.encode(message))

class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()