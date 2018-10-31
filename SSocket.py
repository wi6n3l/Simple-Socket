import socket
import time

rv = True

def Connect(hostip, Port):
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((hostip, Port))

def Server_wait(numofclientwait, port):
    global s2

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s2.bind(("", port))

    s2.listen(numofclientwait)

def Server_accept():

    global s, connected
    s = s2.accept()[0]
    connected = s.getpeername()

def Write(content, encode):
    a = content + "\r"
    s.send(a.encode(encode))
    return
    time.sleep(0.1)

def Read(bytes, encode):
    global rv
    b = ""

    while rv:
        a = s.recv(bytes)
        a = a.decode(encode)

        b = b + a
        return b
        rv = False
    rv = True

def Close():
    s.close()

    return