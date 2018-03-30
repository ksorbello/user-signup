from flask import Flask, request, render_template, redirect 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def sign_up():
    return render_template("base.html")























app.run()