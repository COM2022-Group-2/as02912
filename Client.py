from email import message
from email.message import Message
import socket
from datetime import datetime
import time
from Reciever import UDP_PORT #Keeping UDP Ports Synchronised
from cryptography.fernet import Fernet #Encryption

Clients = {'Adrian': [str(datetime.date(2001, 9, 20).strftime('%d/%m')), b"192.168.0.4"],
            'Terry': [str(datetime.date(2000, 4, 25).strftime('%d/%m')), b"192.168.247.1"],
            'John': [str(datetime.date(1989, 10, 20).strftime('%d/%m')), b"192.168.0.1"],}
#Setting the Client names, DOB's and Addresses for sending the message
DateTime = datetime.today().strftime('%d/%m')
#Obtain current date
Time = time.time()
#Obtain current time

Message = "Happy Birthday "

key = "amVrNGpoaWQ4ZHNpZ2JqZTlidmo0bm1ka2tpbzllMw=="

Fernet = Fernet(key)
print(key)
encMessage = Fernet.encrypt(Message.encode())

while True:
    for key in Clients:
        if Clients[key][0] == DateTime:
            UDP_IP = "192.168.0.3" #Setting my fixed address
            UDP_PORT = 1001
            MESSAGE = encMessage + key
            MESSAGE = str.encode(MESSAGE) #Setting string to binary for UDP
            sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) #Send message to selected IP and Port
            print("UDP target IP: %s" % UDP_IP)
            print("UDP target port: %s" % UDP_PORT)
            MESSAGE = bytes.decode(MESSAGE)
            print("message: %s" % MESSAGE)
            time.sleep(86400) #24 Hour Timer
        else:
            time.sleep(86400) #24 Hour Timer