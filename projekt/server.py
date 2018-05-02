from flask import Flask
from flask import request

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'

@app.route('/login',methods=['GET'])
def signin_from():
    return ''' <form action = "/signin" method = "post">
              <p> <input name = "username" > </p>
              <p> <input name = "password" type = "password"> </p>
              <p> <button type = "submit"> Sign In </button> </p>
              </form >'''
    pass
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h2>Gratulieren</h2>'
    return '<h2>bad boy</h2>'

if __name__=='__main__':
    app.run()#这里是执行Flask的run method，跟文件命名无关。