# Python TCP Client B
import socket 


"""
I add code for dinamic IP and port - also can use function gethostbyname to get from name IP
the port take from consol in server - not true work (  ?????

explain for options more then INC , DEC as in the mail see at the server code
"""
ip = raw_input("Give HostIp: ")
# can use  ip = socket.gethostbyname('www.google.com')  if want to use name and not ip
# is_number(x) ??????
port = int(raw_input("Give Port: ")) #asumeto mistakes for begging
# asumeportis numeber not check it
print "%s,%s"%(ip,port)





def client(ip, port):
    BUFFER_SIZE = 30
    # explain for options more then INC , DEC as in the mail see at the server code
    comm = raw_input(
        "Give option: 1 to INC 2 -DEBUG_LOCAL 3 -DEBUG_ALL 4 stop server and exit 5- exit  6-NODEBUG else DEC ")  # DEBUG option see in the server explain
    action = "DEC"
    val = " "
    if (comm == '1'):
        val = raw_input("Give string as item: ")
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
    tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcpClientB.connect((ip, port))
        tcpClientB.send(MESSAGE)
        data = tcpClientB.recv(BUFFER_SIZE)
        print " Client received data:", data
    finally:
        tcpClientB.close()
    if (comm == '4'):
        return -1
    return 1

host=ip


while client(ip, port) >=0:
    pass



