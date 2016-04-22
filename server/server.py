#Server program
#by Christopher Kossatz
#0.2 21.04.16


import socket
import sys
from thread import *
import sqlite3

HOST = '192.168.1.191'
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

allData = []

def clientthread(conn):
    #Sending message to connected client
    #conn.send('1')

    #infinite loop so that function do not terminate and thread do not end.
    for i in range(17):

        #Receiving from client
        data = conn.recv(1024)
        #reply = '1'
        if not data:
            break
        allData.append(filter(None, data.split('\n')))
        print data
        #conn.send(reply)

    try:
        sqconn = sqlite3.connect('WeatherProject.db')
        sqc = sqconn.cursor()
        sqc.execute("CREATE TABLE IF NOT EXISTS pi(time UNIX)")
    except:
        print "Couldn't connect to/ create DB, please try again"
        sys.exit()

    #fetch all Column Names
    head = allData[0][0].split('-')
    del allData[0]
    print head[-1]    # could be used to select table in database
    del head[-1]

    #fetch witch columns are already present
    try:
        sqc.execute('PRAGMA table_info(pi)')
        d = sqc.fetchall()
    except:
        print "Couldn't fetch Data from db"
    present_columns = []

    for i in d:
        present_columns.append(i[1])

    #insert all columns that aren't present yet
    try:
        for h in head:
            if h not in present_columns:
                sqc.execute('ALTER TABLE pi ADD COLUMN {} REAL'.format(h))
                sqconn.commit()
    except:
        print "Couldn't insert additional columns!"

    #formating Data
    r = []
    allData_new = []
    i = 0

    for row in allData:

        for cell in row:
            cell = cell.split(':')
            if ((cell[0] == 'time') & (len(r) == 0)) | ((i <= len(head)) & (cell[0] != 'time')):
                r.append(cell)
            elif (cell[0] == 'time'):
                allData_new.append(r)
                r = []
                r.append(cell)

    #insert Data into table
    try:
        for data in allData_new:
            sqc.execute("INSERT INTO pi (time) VALUES ({})".format(data[0][1]))
            t = data[0][1]
            del data[0]
            for cell in data:
                sqc.execute("UPDATE pi set {} = {} WHERE time = {}".format(cell[0],cell[1],t))
                sqconn.commit()
    except:
        print 'Database is probably locked. PLease close all other programms that might interfere with the db!'

    sqconn.close()
    conn.close()

#now keep talking with the client
for i in range(2):
    #wait to accept a connection
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread
    try:
        start_new_thread(clientthread ,(conn,))
    except:
        print "Couldn't start Thread"

s.close()
