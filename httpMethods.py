from flask import request
from flask import Flask,url_for
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.methods == 'POST':
       return 'do_the_login'
    else:
        return 'show_the_login_form()'