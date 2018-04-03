from flask import Flask, request, render_template, redirect 
import os
#import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ["GET"])
def sign_up():
    

    username = request.args["username"]
    space = " "
    username_error = ""

    
    password_one = request.args['password']
    password_two = request.args['password2']
    password_error = ""
    
    email = request.args['email']
    email_error = ""


    if not username:
        username_error = " username field may not be left blank."
    elif len(username) > 20 or len(username) < 3:
        username_error = " username must be between 3 and 20 characters."
        return error
    elif space in username:
        username_error = "username may not contain any spaces."
        return error
    else:
        username_error = error
    
    
    if len(password_one) > 26 or len(password_one) < 3:
        password_error = " password must be between 3 and 20 characters. "
    elif space in password_one:
        password_error= " password may not contain any spaces."
    elif password_one != password_two:
        error = " passwords do not match."
    else:
        password_error = password_error
    
    #if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
       # email_error = "please enter a valid email address."
    # else:
        #email_error = email_error

    
    
    

    return  render_template("base.html")

app.run()