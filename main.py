from flask import Flask, request, render_template, redirect 
import os
import re



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home", methods = ["get","post"])
def sign_up():
    

    username = ""
    space = " "
    username_error = ""
    password_error = ""
    password_one = ""
    password_two = ""
    email_error = ""
    email= ""


    if request.method == "POST":
        password_one = str(request.form['password'])
        password_two = str(request.form['password2'])
        username = str(request.form["username"])
        
    
    
        email = str(request.form['email'])
        email_error = ""
        email_error_flag = True
        username_error_flag = True
        password_error_flag = True
        

        
        if not username:
            username_error = " username field may not be left blank."
            username = ""
        elif len(username) > 20 or len(username) < 3:
            username_error = " username must be between 3 and 20 characters."
            username = ""
        elif space in username:
            username_error = "username may not contain any spaces."
            username = ""
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
        
        

         
        
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email_error_flag = False
            
        elif email == "":
            email_error = ""
            email_error_flag = False

        else:
            email_error = "please enter a valid email."
            email = ""
        
           
        if not email_error_flag and not username_error_flag and not password_error_flag:
            return redirect("/welcome?username=" + username)

    return render_template("base.html", username_error=username_error, password_error=password_error,
    email_error=email_error,  email = email, username=username )

@app.route("/welcome")
def welcome_page():
    username =request.args.get("username")
    return render_template("welcome.html",username=username)


app.run()