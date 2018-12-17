#!/usr/bin/python
# -*- conding:utf-8 -*-
import time
import struct
from socket import *
 
SENDERIP = '192.168.0.101'
SENDERPORT = 1501
MYPORT = 1234
MYGROUP = '224.1.1.1'
MYTTL = 255
 
def sender():
    s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
    s.bind((SENDERIP,SENDERPORT))
    # Set Time-to-live (optional)
    ttl_bin = struct.pack('@i', MYTTL)
    s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
    status = s.setsockopt(IPPROTO_IP,
        IP_ADD_MEMBERSHIP,
        inet_aton(MYGROUP) + inet_aton(SENDERIP))
    while True:
        data = 'cisco'
        s.sendto(data + '\0', (MYGROUP, MYPORT))
        print "send data ok !"
        time.sleep(10)
 
if __name__ == "__main__":
    sender()
