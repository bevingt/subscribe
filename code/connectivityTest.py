from threading import Thread
from queue import Queue
import socket

class ConnTest(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
    def run(self):
        try:
            socket.setdefaulttimeout(2)
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # sock.bind((self.ip, self.port))
            sock.connect((self.ip, self.port))
            # sock.shutdown(2)
            # OK_list.append([ip, port])
            print('通')
            return True
        except socket.timeout:
            # Timeout_list.append([ip, port])
            print('超时')
            return False
        except:
            # print '%s %d is DOWN' % (ip, port)
            # DOWN_list.append([ip, port])
            print('不通')
            return False

if __name__ == "__main__":
    slist=['213.105.29.14','3128','89.187.177.90','80']
    for i in range(0,len(slist),2):
        print(slist[i],slist[i+1])
        ConnTest(slist[i],slist[i+1]).run()
