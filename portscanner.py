#!/bin/python3

import sys
import socket
from datetime import datetime
from threading import Thread
from commonPortsDict import commonPortsDict

#Storing list
portList = list(commonPortsDict.keys())

#Checking for argument
if len(sys.argv)==2:
        target=socket.gethostbyname(sys.argv[1])
else:
        print("invalid no of args.")
        sys.exit()

#scan function
def scanPort(port):
        try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                #print("check port {}".format(port))
                if result == 0:
                        print("port {}  is open".format(port))
                s.close()

        except KeyboardInterrupt:
                print("\n exiting program.")
                sys.exit()

        except socket.gaierror:
                print("hostname could not be resolved.")
                sys.exit()

        except socket.error:
                print("couldn't connect to server")
                sys.exit()

#threading
for port in commonPortsDict:
        t = Thread(target=scanPort, kwargs={'port':port})
        t.start()
t.join()
