from flask import Flask, render_template,redirect, session, request

from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()


app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

# need to add register in login.html and check all the stuff

@app.route("/")
def home():
    if not (session):
        return redirect("/login")
    else:
        username=session["username"]+"Task"
        cursor.execute(f"SELECT * FROM {username}")
        items=cursor.fetchall()
        print(items)
        return render_template("home.html",items=items)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        print(username,password)
        try:
            cursor.execute("SELECT password FROM users WHERE name=?", (username,))
            check_pass = cursor.fetchall()[0][0]
        except:
            return render_template("login.html",msg="Invalid user name")
        # i need to check the username in the database here and than check the password
        print("\n",check_pass)
        
        if  check_password_hash(check_pass,password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html",msg="Invalid Password")
        

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
   # print(request.form.get("username"))
   # print(request.form.get("password"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users=cursor.execute("SELECT name FROM users")

        # Ensure username was submitted
        if not username:
            return render_template("register.html",msg="Provide a Username")            
        # Ensure password was submitted
        elif not password:
             return render_template("register.html",msg="Provide a Password")
        # Ensure passwords match
        elif not password == request.form.get("confirmation"):
             return render_template("register.html",msg="Passwords did not match")

        else:
            for user in users:
                if user==username:
                     return render_template("register.html",msg="User Name Already Taken")

            # Insert new user into database
            cursor.execute("INSERT INTO users (name, password) VALUES(?, ?)", (username, generate_password_hash(password)))
            
            username=username+"Task"
            cursor.execute(f"CREATE TABLE {username}(task varchar(255), done boolean)")
            connection.commit()
            # Redirect user to home page
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")
@app.route("/logout", methods=["POST"]) 
def logout():
    """Log user out"""
    if not (session):
        return redirect("login.html")
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

@app.route("/add", methods=["POST"])
def add():
    #add task
    if not (session):
        return redirect("/login")
    username=session["username"]+"Task"
    newTask= request.form.get("newTask")
    print(newTask)
    cursor.execute(f"INSERT INTO {username} (task,done) VALUES(?,?)",(newTask,0))
    connection.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])   
def delete():
    if not (session):
        return redirect("/login")
    username=session["username"]+"Task"
    task=request.form.get("task")
    print(task)
    cursor.execute(f"DELETE FROM {username} WHERE task=?",(task,))
    connection.commit()
    return redirect("/")

@app.route("/markAsDone", methods=["POST"])
def markAsDone():
    if not (session):
        return redirect("/login")
    username=session["username"]+"Task"
    task=request.form.get("task")
    cursor.execute(f"UPDATE {username} SET done=? WHERE task=?",(1,task))
    connection.commit()
    return redirect("/")







if __name__ == "__main__":
    app.run(debug=True)
