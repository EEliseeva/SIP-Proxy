from cmath import log
import socketserver
import re
import socket
import sys
import time
import logging
import sys
sys.path.append(".")
import sipfullproxy

HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        filename='proxy.log',
                        level=logging.INFO, datefmt='%H:%M:%S')
    logging.info("SERVER STARTED " + time.strftime("%a, %d %b %Y %H:%M:%S ",
                                                   time.localtime()))
    ipaddr = socket.gethostbyname(socket.gethostname())
    if ipaddr == "127.0.0.1":
        ipaddr = sys.argv[1]
    logging.info("CURRENT IP: " + ipaddr)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddr, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddr, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()
