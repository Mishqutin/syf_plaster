import socket


class Client:
    def connect(ip, data):
        s = socket.socket()

        s.connect(ip)
        s.send(str(data).encode())
        data = (s.recv(65536)).decode("UTF-8")
        s.close()
        return data



if __name__=="__main__":
    IP = ("localhost", 12345)
    KEY = "123456"
    NAME = "anon"

    while True:
        command = input("Cmd: ")
        data = {"key": KEY, "name": NAME, "string": command}

        recvData = Client.connect(IP, data)
        if recvData: print(recvData)
