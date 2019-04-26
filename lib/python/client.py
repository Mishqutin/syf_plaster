
class Client:
    import socket
    
    def connect(ip, data):
        s = Client.socket.socket()
        
        s.connect(ip)
        s.send(str(data).encode())
        data = (s.recv(65536)).decode("UTF-8")
        s.close()
        return data