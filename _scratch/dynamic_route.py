"""
在访问的时候用指定参数

@app.route("/类型:变量名")
常见的参数类型：
整数
小数
字符串，path

"""


from flask import Flask

app = Flask(__name__)

@app.route('/<int:age>')
def get_(age):
    return f"the age is {age}"


@app.route('/<float:age>')
def play_game(age):
    return f"the float is {age}"

if __name__ == "__main__":
    app.run()