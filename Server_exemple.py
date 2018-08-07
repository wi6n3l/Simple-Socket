import SSocket

SSocket.Server_wait(5, 2020)

SSocket.Server_accept()

print(SSocket.Read())

SSocket.Write("'Handshake' Hi! I'm Server!")

print(str(SSocket.connected) + " connected!")

SSocket.Close()