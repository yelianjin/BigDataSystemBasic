from Config import Config

class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, event):
        if Config.DEBUG:
            print("[%10s]: %s" % (self.name, event))
