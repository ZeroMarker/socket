import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234))
    s.send(b"Hello, World!")
    data = s.recv(1024)
    print("Received", repr(data))