import mysql
import mysql.connector


class Besant:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="BESANT")
        self.mycursor = self.mydb.cursor()
        self.login_page()

    def login_page(self):
        user_input = input("please chose?  1.Enter a to register  2.Enter b to login  :::    ")

        if user_input == "a":
            self.register()
        elif user_input == "b":
            self.login()
        else:
            print("bye")

    #    u_name,u_email,u_password,u_dob, u_address, u_phone, u_qualification

    def register(self):
        u_name = input("Enter name  : ")
        u_email = input("Enter email  : ")
        u_password = input("Enter password  : ")
        u_dob = input("Enter DOb  : ")
        u_address = input("Enter address  : ")
        u_phone = input("Enter phone  : ")
        u_qualification = input("Enter Qualification  : ")

        self.mycursor.execute(
            "INSERT INTO users(user_id,u_name,u_email,u_password,u_dob, u_address, u_phone, u_qualification) VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}')".format
            (u_name, u_email, u_password, u_dob, u_address, u_phone, u_qualification))
        self.mydb.commit()
        print("REGISTER SUCCESS")

    def login(self):
        u_email = input("Enter email  : ")
        u_password = input("Enter password  : ")

        self.mycursor.execute("SELECT * FROM users WHERE u_email LIKE '{}' AND u_password LIKE '{}'".format
                              (u_email, u_password))

        if len(self.mycursor.fetchall()) == 0:
            print("INCORRECT PASSWORD")
        else:
            print("WELLCOME")


obj = Besant()
