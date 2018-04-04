from flask import Flask, request, render_template, redirect 
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home", methods = ["GET"])
def sign_up():
    

    username = str(request.args.get("username"))
    space = " "
    username_error = ""
    temp_username = "  "

    
    password_one = str(request.args.get('password'))
    password_two = str(request.args.get('password2'))
    password_error = ""
    
    email = str(request.args.get('email'))
    email_error = ""
    no_email = ''

    if not username:
        username_error = " username field may not be left blank."
        temp_username = temp_username
    elif len(username) > 20 or len(username) < 3:
        username_error = " username must be between 3 and 20 characters."
        temp_username = temp_username
    elif space in username:
        username_error = "username may not contain any spaces."
        temp_username = temp_username
    else:
        username_error = username_error
        temp_username = username
    
    
    if len(password_one) > 26 or len(password_one) < 3:
        password_error = " password must be between 3 and 20 characters. "
    elif space in password_one:
        password_error= " password may not contain any spaces."
    elif password_one != password_two:
        password_error = " passwords do not match."
    else:
        password_error = password_error
    
    
    if email:
        
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email_error = email_error
            email = email
        else:
            email_error = "please enter a valid email address."
            email = ""
    
    if not email:
        email_error = email_error
        
    if not email_error and not username_error and not password_error:
        return redirect("/welcome?username=" + username)

    return render_template("base.html", username_error=username_error, password_error=password_error,
    email_error=email_error,  email = email, temp_username=temp_username )

@app.route("/welcome")
def welcome_page():
    username =request.args.get("username")
    return render_template("welcome.html",username=username)


app.run()