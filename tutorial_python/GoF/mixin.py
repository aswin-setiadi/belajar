import socket

# Our original example’s base class and subclasses.


class Logger(object):
    def __init__(self, file):
        print("file init called")
        self.file = file

    def log(self, message):
        print("file log called")
        self.file.write(message + "\n")
        self.file.flush()


class SocketLogger(Logger):
    def __init__(self, sock):
        print("socket init called")
        self.sock = sock

    def log(self, message):
        print("socket log called")
        self.sock.sendall((message + "\n").encode("ascii"))


# Don’t accept a “pattern” during initialization.


class FilteredLogger(Logger):
    pattern = ""

    def log(self, message):
        if self.pattern in message:
            # super call anything after FilteredLogger in mro
            # which in this case is SocketLogger log
            super().log(message)


# Multiple inheritance is now simpler.


class FilteredSocketLogger(FilteredLogger, SocketLogger):
    pass  # This subclass needs no extra code!


# Works just fine.
if __name__ == "__main__":
    sock1, sock2 = socket.socketpair()
    # The caller can just set “pattern” directly.

    logger = FilteredSocketLogger(sock1)
    logger.pattern = "Error"

    # Works just fine.

    logger.log("Warning: not that important")
    logger.log("Error: this is important")

    print("The socket received: %r" % sock2.recv(512))
    print(FilteredSocketLogger.__mro__)
