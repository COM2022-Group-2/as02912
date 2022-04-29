import socket

UDP_IP="192.168.0.3"
UDP_PORT = 1001

sock = socket.socket(socket.AF_INET, #internet
                    socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
    data.bytes.decode(data)
    print("recieved message: %s" % data)