import socket
import time

rv = True

def Connect(HostIp, Port):
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HostIp, Port))

def Server_wait(numofclientwait, port):
    global s2

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s2.bind(("", port))

    s2.listen(numofclientwait)

def Server_accept():

    global s

    s = s2.accept()[0]

def Write(D):
    a = D + "\r"
    s.send(a.encode("ascii"))
    return
    time.sleep(0.1)

def Read():
    global rv
    b = ""

    while rv:
        a = s.recv(1024)
        a = a.decode("ascii")

        b = b + a
        return b
        rv = False
    rv = True

def Close():
    s.close()

    return