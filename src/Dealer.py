from Logger import Logger
from Config import DealerConfig


class Dealer(object):
    def __init__(self):
        log = Logger("helloworld")
        log.log("hello")


if __name__ == "__main__":
    Dealer()
    print(DealerConfig.DEBUG)
