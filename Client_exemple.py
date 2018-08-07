import SSocket

SSocket.Connect(ip, 2020)

SSocket.Write("'Handshake' Hi! I'm Client!")

print(SSocket.Read())

SSocket.Close()