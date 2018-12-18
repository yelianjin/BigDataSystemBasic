#coding:utf-8
import time
import json
import sys
import threading
import re
import socket
###test_data
data0={'data':((1,2,3,4,5),(2,3,5,6,7))}##size,id,sell,bid,amount,time
jdata0=json.dumps(data0)
print jdata0
bdata0=jdata0.decode()
print bdata0
##listening
list=[]
def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('10.81.6.128', 6666))
        s.listen(10)
    except socket.error as msg:
        print msg
        sys.exit(1)
    print 'Waiting connection...'

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    print 'Accept new connection from {0}'.format(addr)

    while 1:
        datalens = conn.recv(1024)
        conn.send("next".encode())
        print datalens
        dataJson = ""
        print type(datalens)
        while 1:
            datatemp = conn.recv(1024)
            if not datatemp:
                break
            dataJson += datatemp
            buffer(dataJson,list)
        print len(dataJson)
        break
    print datalens.decode() == str(len(dataJson))
    conn.close()

##buffering if(time<=0.5s)&&size does not satisfy
def buffer(messageJson,list):
    time1=time.time()
    message=messageJson.decode()
    print type(message)
    message=json.loads(message)
    print type(message)
    result_list=[(i[0],i[1],i[2],i[3],i[4]+time1)for i in message['data']]
    list=list+result_list
    print sys.getsizeof(list)
if __name__ == '__main__':
    socket_service()
    print list
##sending
##sendingback


