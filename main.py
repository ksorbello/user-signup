from flask import Flask, request, render_template, redirect 
import os
import re
import sys


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home", methods = ["get"])
def sign_up():
    

    username = str(request.args.get("username"))
    space = " "
    username_error = ""
    #username = "  "

    
    password_one = str(request.args.get('password'))
    password_two = str(request.args.get('password2'))
    password_error = ""
    
    email = str(request.args.get('email'))
    email_error = ""
    email_error_flag = True
    username_error_flag = True
    password_error_flag = True
    

    if username == "None":
        username = ""
    elif not username:
        username_error = " username field may not be left blank."
        username = username
    elif len(username) > 20 or len(username) < 3:
        username_error = " username must be between 3 and 20 characters."
        username = username
    elif space in username:
        username_error = "username may not contain any spaces."
        username = username
    else:
        username_error_flag = False

    
    
    if len(password_one) > 26 or len(password_one) < 3:
        password_error = " password must be between 3 and 20 characters. "
    elif space in password_one:
        password_error= " password may not contain any spaces."
    elif password_one != password_two:
        password_error = " passwords do not match."
    else:
        password_error_flag = False
    
    
    #if email == "None":
        #email_error = email_error
    print("email"+ email, file=sys.stderr) 
    
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email_error_flag = False
    elif email == "":
        email_error = ""
        email_error_flag = False
    elif email == "None":
        email_error_flag = False
        email = ""
    else:
        email_error = "please enter a valid email."
    
    print("email"+ email, file=sys.stderr)   
    if not email_error_flag and not username_error_flag and not password_error_flag:
        return redirect("/welcome?username=" + username)

    return render_template("base.html", username_error=username_error, password_error=password_error,
    email_error=email_error,  email = email, username=username )

@app.route("/welcome")
def welcome_page():
    username =request.args.get("username")
    return render_template("welcome.html",username=username)


app.run()