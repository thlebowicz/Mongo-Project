from flask import Flask,render_template,request
import pymongo

app = Flask(__name__)


@app.route("/")
@app.route("/home",methods=['GET','POST'])
def home_html():
    if request.method=="POST":
        pass
    return render_template("home.html")


@app.route("/todo")
def todo_html():
    return render_template("todo.html")

@app.route("/login", methods=["GET","POST"])
def login_html():
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register_html():
    if(request.method=="POST"):
        newuser = request.form["username"]
        newpass = request.form["password"]
        newpass2 = request.form["pwdconfirm"]
        error = []
        success = True
        post = True
        
        if newpass!=newpass2:
            error.append("mismatchpass")
        if newuser=="jamal":
            error.append("jamal")
        if len(error)>0:
            success = False
        else:
            pass
            
        return render_template("register.html",
                               errorlist=error,
                               success=success,
                               post=post)
    else:
        return render_template("register.html")

@app.route("/settings")
def main_html():
    return render_template("main.html")

@app.route("/settings")
def settings_html():
    return render_template("settings.html")

###

if __name__ == "__main__":
    app.debug = True
    app.run()
