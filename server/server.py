import socket
import sys
from thread import *

HOST = '192.168.2.111'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

def clientthread(conn):
    #Sending message to connected client
    #conn.send('1')

    #infinite loop so that function do not terminate and thread do not end.
    for i in range(10):

        #Receiving from client
        data = conn.recv(256)
        #reply = '1'
        print data + '\n'
        if not data:
            break

        #conn.send(reply)

    conn.close()

#now keep talking with the client
for i in range(2):
    #wait to accept a connection
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread
    start_new_thread(clientthread ,(conn,))

s.close()
