# python web

## Browser & Server 架构

使用 http 协议 - 基于 tcp/udp 协议。

客户端服务段之间使用socket 约定协议版本 tcp udp制定地址和端口

server 发送 html

browser 渲染 html

客户端发起请求（url），服务端准备好数据（动态/静态），封装成html。发送给客户端，客户端解析呈现。

在 tcp server 之上 application 层的一个开发模式。

在 80 端口发起 tcp 请求，使用http application。

## HTTP协议

http 协议是无状态协议

同一个客户端两次请求之间没有任何关系，服务器端角度看，不知道两个请求来自同一个客户端

设计时的网络环境太差了，目的是网络上分享科研数据或者文献，没有必要记录客户端信息。处理完请求之后，立即关闭连接，节约资源。没想到需要记录状态和实现动态。

cookie

- 解决无状态
- 键值对
- 每次发起请求，客户端都会传送一次cookie
- 服务端通过cookie判断请求和之前请求的关联
- cookie客户端可以自己指定，所以不可信，不安全
- 第一次发送请求不带cookie，服务器发给客户端一个出世cookie，之后每次客户端发送cookie
- 短时间保持

url

- uniform resource locator
- `schema://host[:port#]/path/.../[;url-params][?query-string][#anchor]`
- 理解为访问静态资源，某路径下的某个html文件
- `?key=value1&key=value2`浏览器发的数据
- 以前路径代表资源，参数代表数据，现在路径就是数据
- restful 用url代表静态资源不用`?key=value`

HTTP 消息

request and response

请求头 request head

```
GET / HTTP/1.1      请求方法，请求路径，请求协议版本
Host: www.sadofjoa.com
UserAgent: Mozilla/5.0 (adlkfjalkefj)
Accept: text/html.application/sdfawe
awefj
asefjaeo
Cookie: skdfalkjfeawef
```

- GET 获取url对应的资源
  - 用一个 url 里的 query string 获取资源
  - `GET path/to/resource?sdfajweif=aefawef&aoiewjfoai=awefa`
  - BODY里没参数
- POST 提交数据到服务器
  - `POST /xxe/yyy?id=4&name=sada HTTP/1.1`
  - 之后在BODY里面也有参数
- HEAD 和GET类似，但是不返回消息正文

不用POST，用url包含信息`http://www.sadf.com/student/001`，restful

RESTful Api
- 使用 http 规定的 动词 (GET POST PUT PATCH DELETE)
- 用url定位资源，一个url对应一个资源，url里不包含动词
- 透明化资源
- query string 里包含信息，或者header里包含信息

响应
- `HTTP/1.1 200 OK`
- `charset=utf-8`
- `301 or 302` 重定向 不返回响应体
- `404` 数据找不到

## WSGI

解决 server 和 app 之间的通讯接口

WSGI server
- 接收 http 请求
- 接收浏览器的HTTP请求，并解析封装成 environ 环境数据
- 把返回方法名发给 WSGI App
- 调用应用程序，将environ和start_response方法传入
- 将应用程序响应的正文封装成HTTP响应豹纹返回浏览器

WSGI APP
- 业务逻辑
- 把正文给server封装
- 调用返回方法

```python
def demo_app(environ,start_response):
    #environ 是 request head 封装的 dict
    from io import StringIO
    stdout = StringIO() #开启一个缓存区，存放print的内容
    print_std = lambda x: print(x,file=stdout)
    print_std("hello_world\n")
    h = sorted(environ.items())
    for k,v in h:
      print_std(k,"=",repr(v))
    start_response("200 OK",[("Content-Type","text/plain;charset=utf-8")])
    #先把报头返回，发给客户端
    return [stdout.getvalue().encode("utf-8")]
    #把缓存区的内容读取出来，发送给SWGIapp，SWGI转化成html再发送给客户端
```

```python
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def simple_app(environ,start_response):
    print(environ) #展示一下请求是啥样的

    status = "200 OK"
    headers = [("Content-type","text/plain;charset=utf-8")]

    start_response(status,headers)

    ret = [f"{key}:{value}".encode("utf-8")for key,value in envrion.items()]
    return ret #返回可迭代对象，包含很多字符串的 list

httpd = make_server("0.0.0.0",9000,simple_app) 

try:
    httpd.serve_forever()
except Exception as e:
    print(e) #如果出错了，服务器不能停
except KeyboardInterrupt:
    print("stop")
    http.server_close()

#最好在app里处理error，这样就不会把服务器搞坏
```

## environ

|          名称           |     含义      |
| :---------------------: | :-----------: |
|     REQUEST_METHOD      |               |
|        PATH_INFO        | url的路径部分 |
|      QUERY_STRING       |               |
| SERVER_NAME,SERVER_PORT |               |
|        HTTP_HOST        | 地址和端口好  |
|     SERVER_PROTOCOL     |               |
|     HTTP_USER_AGENT     |               |

make_server 也可以传入类

需要这么写

```python
class A:
    def __init__(self,*args,**kwargs):
      pass
    def __call__(self,environ,start_response):
      pass

class B:
  def __init__(self,environ,start_response):
    pass

  """因为init返回的是实例，所以不能用return，server需要接收一个可迭代对象，所以需要定义迭代方法"""
  def __iter__(self):
    yield from self.ret

httpd = make_server("0.0.0.0",9000,A()) #A的实例
httpd = make_server("0.0.0.0",9000,B) #直接传可迭代类
```

start_response(status,response_headers)
status 状态数
response_headers 二元组的列表[("Content-Type","text/plain;charset=utf-8"),]
exc_info 错误处理使用的

服务器端

curl
```
curl -I http://0.0.0.0:9999/xxx?id=5
curl -X POST http://0.0.0.0:9999/xxxx?id=5 -d '{"x":2}'
```

WEB 服务器

本质是TCP服务器，舰艇在特定端口
支持HTTP协议，能够将http请求报文进行解析
python提供了 wsgi 协议

自己写一个web框架

类flask框架实现

```python
from urllib.parse import parse_qs
def simple_app(environ,start_response):
    query_string = environ.get("QUERY_STRING")
    # d = []
    # for item in query_string.split("&"):
    #     k,_,v = item.partition("=")
    #     d[k] = v
    #d = {k:v for k,_,v in map(lambda x:partition("="),query_string.split("&"))}
    qs = parse_qs(query_string) #返回 key：[value1,value2,value3...]
    method = environ.get("METHOD")
    #environ解析，webob库 


    status = "200 OK"
```

```python
from wsgiref.simple_server import make_server
from webob import Request, Response

def simple_app(environ,start_response):
    request = Request(environ)
    query_string = request.query_string
    method = request.method
    path = request.path
    params = request.params

```

webob

```python 
from webob.multidict import MultiDict

md = MultiDict()
md.add("a",1)
md.add("b",2)
md.add("b",3)
```

```python
res = Response()
res.body = "<h1>sadfaM</h1>"
return res(environ,start_response)
```

```python
from webob.dec import wsgify

@wsgify
def app(request:Request) -> Response:
    return Response()
```
装饰器帮我们简化业务逻辑处理，装饰器里面定义了environ -> request的映射和start_response的调用。
如果我们return string 或者 bytes 那么response也帮我们封装成response了