# pprint library is used to make the output look more pretty
from pprint import pprint
from Backend.python_server import DB_Connection
import logging
from flask import Flask

class DB_Connector:


    # def main(self):
    #     conn = DB_Connection().client
    #
    #
    #     # Issue the serverStatus command and print the results
    #     serverStatusResult = conn.admin.command("serverStatus")
    #     pprint(serverStatusResult)
    #
    #
    #     self.add_new_student(1, 'John', 'Smith', 'jsmith@umd.edu', 'jsmith01', 'disco1', conn)



    # NEW ACCOUNTS
    # Inserts new student into db
    def add_new_student(self, studentID, fname, lname, email, username, password, conn):
        # client[organization][table]
        conn['eduspace']['students'].insert_one({
            "studentID": studentID,
            "fname": fname,
            "lname": lname,
            "email": email,
            "username": username,
            "password": password
        })


    def add_new_teacher(empID, fname, lname, email, username, password, client):
        # client[organization][table]
        client['eduspace']['teachers'].insert_one({
            "empID": empID,
            "fname": fname,
            "lname": lname,
            "email": email,
            "username": username,
            "password": password
        })

    # Dashboard creation functionality



    # def add_new_dev(empID, fname, lname, email, username, password):
    #
    # # New organization will manually be added as a new DB: initialized with approriate tables



if __name__ == "__main__":
    DB_Connector().main()
