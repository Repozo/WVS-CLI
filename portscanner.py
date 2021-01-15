!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2:
        target=socket.gethostbyname(sys.argv[1])
else:
        print("invalid no of args.")
        sys.exit()

portList = [20,21,22,23,25,53,80,110,123,143,161,194,443]

try:
        for port in portList:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1) #is a float
                result = s.connect_ex((target,port)) #returns error indictor
                print("check port {}".format(port))
                if result == 0:
                        print("port {}  is open".format(port))
                s.close()

except KeyboardInterrupt:
        print("\n exiting program yayay.")
        sys.exit()

except socket.gaierror:
        print("hostname could not be resolver.")
        sys.exit()

except socket.error:
        print("cound't connect to server")
        sys.exit()
