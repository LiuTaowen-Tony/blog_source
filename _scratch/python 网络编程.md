# 网络编程

## Socket 

socket 标准库

低级库，对 tcp/ip 的封装。

协议族

| 名称     | 含义               |
| -------- | ------------------ |
| AF_INET  | IPV4               |
| AF_INET6 | IPV6               |
| AF_UNIX  | Unix Domain Socket |

socket 类型

| 名称        | 含义    |
| ----------- | ------- |
| SOCK_STREAM | TCP协议 |
| SOCK_DGRAM  | UDP     |

进程间通讯，第三方消息队列，现在不用共享内存，用socket

用网络在本机进程间通讯

tcp 心跳

```python
import socket 

server = socket.socket()
server.bind(("127.0.0.1",9000))

server.listen()

s,raddr = server.accept()

while True:
    s.recv(1024)
    print(data)
    s.send(bf"ack. {data}")

s.close()

server.close()
```

```python
import socket
import threading
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

class ChatServer:
    def __init__(self,ip="127.0.0.1",port=9999):
        self.addr = (ip,port)
        self.sock = socket.socket()
        self.clients = {}
        self.event = treading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()

        threading.Tread(target=self.accept,name="accept").start()
        

    def accept(self):
        while not self.event.is_set():
            try:
                s,raddr = self.sock.accept() #阻塞
                self.clients[raddr] = s
                threading.Thread(target=self.recv,name="recv",args=s).start()
            except:
                pass


    def recv(self,s):
        while not self.event.is_set():
            try: #网络可能的异常不可知，而且可能比较频繁
                data = s.recv(1024) #阻塞
            except Exception as e:
                logging.error(e)
                data == b"quit"

            if data == b"quit":
                self.clients.pop(sock.getpeername())
                s.close()
                break

            logging.info(data)
            for s in self.clients.values(): #群聊
                s.send(f"ack {data.decode()}".encode("utf-8"))



    def stop(self):
        for s in self.clients.values:
            s.close()
        
        self.sock.close()
```