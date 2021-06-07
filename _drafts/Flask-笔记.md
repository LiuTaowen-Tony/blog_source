---
title: Flask 笔记 22nd May 2021
tags:
---

这里记录一下目前我都学了啥

还没学 blue print 啥的

视图函数

```python
@app.route("\url\<int : number>", methods = ["GET", "POST"])
def view(number):
	pass
```

wtf 表单

```python
class Login(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    password_confirm = PasswordField("password_confirm")
    submit = SubmitField("submit")
    

@app.route("/form", methods=["GET", "POST"])
def login():
    login_form = Login()
    return render_template("index.html", login_form = login_form
```

```html
    <form method="post">
      {{ login_form.username.label }}{{ login_form.username }}
      {{ login_form.password.label }}{{ login_form.password }}
      {{ login_form.password_confirm.label }}{{ login_form.password_confirm }}
      {{ login_form.submit.label }}{{ login_form.submit }}
    </form>
```

flash 传输 message

```python
      if not all([username, pswd, pswd2]):
            flash("not full")
        elif pswd != pswd2:
            flash("not consistent")
```

```html
      {% for message in get_flashed_messages() %}
        {{ message }}
      {% endfor %}
```

需要配置secrete key

```python
   SECRET_KEY = os.urandom(16),
```

