

class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, event):
        print("[%10s]: %s" % (self.name, event))
