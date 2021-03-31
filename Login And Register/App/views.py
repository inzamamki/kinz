import mysql.connector

from App import app
from flask import render_template, request

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="besant")
cursor = mydb.cursor()


@app.route("/")
def index():
    return render_template("start.html")


@app.route("/start")
def start():
    return render_template("start.html")
#


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/login_valid", methods=['POST'])
def login_valid():
    u_email = request.form.get('email')
    u_password = request.form.get('password')

    cursor.execute("SELECT * FROM users WHERE u_email LIKE '{}' AND u_password LIKE '{}'".format(u_email, u_password))
    users = cursor.fetchall()
    if len(users) > 0:
        return render_template("index.html")
    else:
        return render_template("login.html")
    # return users

        # ("login.html")


@app.route("/add_user", methods=['POST'])
def add_user():
    u_name = request.form.get('username')
    u_email = request.form.get('email')
    u_password = request.form.get('password')
    u_dob = request.form.get('dob')
    u_address = request.form.get('address')
    u_phone = request.form.get('phone')
    u_qualification = request.form.get('degree')
    cursor.execute("INSERT INTO users(user_id,u_name,u_email,u_password,u_dob, u_address, u_phone, u_qualification) VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}')".
                   format(u_name, u_email, u_password, u_dob, u_address, u_phone, u_qualification))
    mydb.commit()
    return render_template("index.html")
