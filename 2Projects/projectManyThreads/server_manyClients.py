import socket
import threading
import SocketServer
import logging
import json
import sys
import os
import logfile
dir_path = os.path.dirname(os.path.realpath(__file__))+'/'

import stack
itemList=stack.Stack()  # SAFE FOR ATOMIC FUNCTIONS IN THREAD  NOT NEED TO ADD LOCK MECHANIZIM

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

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def MYErrorMessage(self,Opt,message):
        global DebugFlag
        global globalLogging
        global dir_path
        if (DebugFlag & 3) > 0 :  # 1 or 2
            if (DebugFlag & 1) == 1:  # global logginh
				if (Opt==0):
					globalLogging.error(message)# "error: " + VErr.message)
            else:  # ==2
                # private logging
                if (Opt ==2):
					logfile.Local_logger(self.client_address[0], dir_path + self.client_address[0]+".log", logging.INFO,message)
                else:
					logfile.Local_logger(self.client_address[0], dir_path + self.client_address[0]+".log", logging.ERROR,message)

    def handle(self):
        global StopServer
        global itemList
        global DebugFlag
        global globalLogging
        try:
            data = self.request.recv(1024)
            self.MYErrorMessage(2,"data="+data)
            JsonP = json.loads(data)
            command=JsonP["comm"]
            item=JsonP["item"]
            self.MYErrorMessage(0, "EQQQQQQQQQQQQQ error")

        except ValueError as VErr:
            if (DebugFlag&3) > 0 : # 1 or 2

                if (DebugFlag&1)==1: # global logginh
                    self.MYErrorMessage(0, "error: " + VErr.message)
                if (DebugFlag & 2) == 2: # may be that want write in global and local
                    self.MYErrorMessage(0,"error: " + VErr.message+" data:"+ data)
                self.request.sendall("error: " + VErr.message)
            return
        except:
            self.MYErrorMessage(0, "ERROR: Unexpected error")
            return
        msgback="OK"
        try:
            if (command == 'INC'):
                itemList.append(item)  # assume safe threads
                pass
                # add to stack
            elif   (command == 'DEC'):
                if(itemList.size() <= 0):
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
        self.request.sendall(msgback)



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "port:", port

    while (StopServer==0):
        pass


    server.shutdown()
    server.server_close()

