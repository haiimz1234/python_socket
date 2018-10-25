# Python TCP Client B
import socket 

ip, port = "127.0.0.1", 0
port=2015
BUFFER_SIZE = 200



host=ip
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((ip, port))

def client(ip, port):
    global tcpClientB
    BUFFER_SIZE = 30
    # explain for options more then INC , DEC as in the mail see at the server code
    comm = raw_input(
        "Give option: 1 to INC 2 -DEBUG_LOCAL 3 -DEBUG_ALL 4 stop server and exit 5- exit  6-NODEBUG else DEC ")  # DEBUG option see in the server explain
    action = "DEC"
    val = " "
    if (comm == '1'):
        val = raw_input("Give string as item")
        if (len(val) > 20) :
            val=val[:19]
            print val
        action = 'INC'
    elif (comm == '2'):
        val = '2'
        action = "DEBUG"
    elif (comm == '3'):
        val = '1'
        action = "DEBUG"
    elif (comm == '4'):
        action = "STOP"
    elif (comm == '5'):
        return -1
    elif (comm == '6'):
        val = '1'
        action = "NODEBUG"
    MESSAGE = '{"comm":"' + action + '","item":"' + val + '"}'

    try:
        tcpClientB. send(MESSAGE)
        print "BEF RECIEVE"
        data = tcpClientB.recv(BUFFER_SIZE)
        print " Client received data:", data
    except:
        print " error recieve "
    if (comm == '4'):
        tcpClientB2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # be sure it will close server
        tcpClientB2.connect((ip, port))
        tcpClientB2.close()
        return -1
    return 1

host=ip


while client(ip, port) >=0:
    pass

tcpClientB.close()
