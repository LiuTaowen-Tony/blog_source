"""
查看那些路由可以访问：
- 使用 app.url_map，返回的是 app 装饰的所有路由和路径之间的映射关系
app.run() 参数"
app.run(host = "127.0.0.1",port=5000,debug=False,)

如果 debug = True 运行过程中，改动代码，不需要重新启动
如果程序报错了，会友好提示

1. host 

"""



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world Flask"

if __name__ == '__main__':
    app.run()