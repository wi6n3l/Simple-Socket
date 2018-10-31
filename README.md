# Simple Socket

Simple Socket is a module for python with the objective of simplify the socket connections for beginers.

Example of Server:

```
import SSocket

SSocket.Server_wait(connections, port)

SSocket.Server_accept()

print(SSocket.Read(1024, "ascii"))

SSocket.Write("'Handshake' Hi! I'm Server!", "ascii")

SSocket.Close()
```

Example of Client:

```
import SSocket

SSocket.Connect(ip, port)

SSocket.Write("'Handshake' Hi! I'm Client!", "ascii")

print(SSocket.Read(1024, "ascii"))

SSocket.Close()
```
Output of Server:

```
'Handshake' Hi! I'm Client!
```

Output of Client:

```
'Handshake' Hi! I'm Server!
```

To get connected client IP and Port use:

```
SSocket.connected
```

Dependencies:
  - socket module
  - time module