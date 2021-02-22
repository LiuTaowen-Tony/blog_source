from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from io import StringIO

def simple_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type","test/plain;charset=utf-8")]
    print(environ)
    start_response(status, headers)
    ret = ["Hello world".encode("utf-8")]
    return ret

httpd = make_server("127.0.0.1",9000,simple_app)

try:
    httpd.serve_forever()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("stop")
    httpd.server_close()