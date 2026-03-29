from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, score FROM users ORDER BY score DESC")
    data = cursor.fetchall()

    conn.close()

    return render_template("leaderboard.html", data=data)


# Register user
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]

        conn = sqlite3.connect("project.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users(name) VALUES(?)",(name,))
        conn.commit()

        conn.close()

    return render_template("register.html")


# Submit work
@app.route("/submit", methods=["GET","POST"])
def submit():

    if request.method == "POST":

        user_id = request.form["user_id"]
        task = request.form["task"]
        points = int(request.form["points"])

        conn = sqlite3.connect("project.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks(user_id,task,points) VALUES(?,?,?)",
            (user_id,task,points)
        )

        cursor.execute(
            "UPDATE users SET score = score + ? WHERE id=?",
            (points,user_id)
        )

        conn.commit()
        conn.close()

    return render_template("submit.html")


app.run(debug=True)