import socket 
from threading import Thread
# import threading
from SocketServer import ThreadingMixIn 
import logging
import json
import sys
import os
import logfile
dir_path = os.path.dirname(os.path.realpath(__file__))+'/'
itemList=[]  # SAFE FOR ATOMIC FUNCTIONS IN THREAD  NOT NEED TO ADD LOCK MECHANIZIM
TCP_IP = '0.0.0.0'
TCP_PORT = 2015
BUFFER_SIZE = 30  # Usually 1024, but we need quick response

"""

DebugFlag: 0 no debug
          1 debug for all users
          2- specify by IP

              more option not yet write
                can be bit optuon for bebug in other area of the code
                example:
                    can write that 8 is write every reqwest
                    16 write every response and etc' use bit flag;
    I add also action DEBUG item for change the use from client

StopServer - StopServer and exit

"""
DebugFlag=0
StopServer=0

globalLogging=logfile.Setup_MyGlobal_logger("GLOBAL",dir_path+"GlobalLog.log",logging.INFO)
class ClientThread(Thread): 
 
    def __init__(self,ip,port,conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn=conn
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
    def MYErrorMessage(self,Opt,message):
        global DebugFlag
        global globalLogging
        global dir_path
        if (DebugFlag & 3) > 0:  # 1 or 2
            if (DebugFlag & 1) == 1:  # global logginh
                globalLogging.error(message)# "error: " + VErr.message)
            else:  # ==2
                # private logging
                logfile.Local_logger(self.client_address[0], dir_path + self.client_address[0]+".log", logging.ERROR,message)


    def run(self):
        global StopServer
        global itemList
        global DebugFlag
        global globalLogging
        nmFree=0
        while True :
            try:
                data = self.conn.recv(2048)
                nmFree+=1
                if(nmFree >4):
                    return # must add time only if in small time know it closed

                JsonP = json.loads(data)
                command=JsonP["comm"]
                item=JsonP["item"]
                nmFree = 0
            except ValueError as VErr:
                if (DebugFlag&3) > 0 : # 1 or 2

                    if (DebugFlag&1)==1: # global logginh
                        self.MYErrorMessage(0, "error: " + VErr.message)
                    if (DebugFlag & 2) == 2: # may be that want write in global and local
                        self.MYErrorMessage(0,"error: " + VErr.message+" data:"+ data)
                    self.conn.sendall("error: " + VErr.message)
                return
            except:
                self.MYErrorMessage(0, "ERROR: Unexpected error")
                return
            msgback="OK"
            try:
                if (command == 'INC'):
                    itemList.append(item)  # assume safe threads

                    # add to stack
                elif   (command == 'DEC'):
                    if(len(itemList) <= 0):
                        msgback = "ERROR : no items"  #
                        self.MYErrorMessage(0, msgback)
                    else:
                        msgback="pop : "+ itemList.pop()  # assume safe threads
                    pass
                elif  (command == 'DEBUG'):
                    DebugFlag=(DebugFlag|int(item)) # is not thread safty - If wna need add lock unlock mechanizim
                elif (command == 'NODEBUG'):
                    DebugFlag =0  # is not thread safty - If wna need add lock unlock mechanizim
                    pass
                elif (command == 'STOP'):
                    StopServer=1
                else:
                    msgback = "ERROR:  command mistake"
            except:
                msgback ="ERROR: Unexpected error"
                self.MYErrorMessage(0,msgback)
            self.conn.sendall(msgback)


# Multithreaded Python server : TCP Server Socket Program Stub

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 

    (conn, (ip,port)) = tcpServer.accept()
    conn.connect
    newthread = ClientThread(ip,port,conn)
    newthread.start() 
    threads.append(newthread)
    if(StopServer==1):
        break
#    A=Thread.active_count

for t in threads: 
    t.join() 