import socket
from datetime import datetime
import time

from zmq import Message

from Reciever import UDP_PORT

Clients = {'Adrian': [str(datetime.date(2001, 9, 20).strftime('%d/%m')), b"192.168.0.4"],
            'Terry': [str(datetime.date(2000, 4, 25).strftime('%d/%m')), b"192.168.247.1"],
            'John': [str(datetime.date(1989, 10, 20).strftime('%d/%m')), b"192.168.0.1"],}

DateTime = datetime.today().strftime('%d/%m')

Time = time.time()
while True:
    for key in Clients:
        if Clients[key][0] == DateTime:
            UDP_IP = "192.168.0.3"
            UDP_PORT = 1001
            MESSAGE = "Happy birthday " + key
            MESSAGE = str.encode(MESSAGE)
            sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            print("UDP target IP: %s" % UDP_IP)
            print("UDP target port: %s" % UDP_PORT)

            MESSAGE = bytes.decode(MESSAGE)

            print("message: %s" % MESSAGE)

            time.sleep(86400)
        else:
            time.sleep(86400)