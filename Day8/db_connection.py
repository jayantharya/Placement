import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Employee',
            user='root',
            password='JKD@1816arya' 
        )
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None



my_db = connect_db()


if my_db and my_db.is_connected():
    print("Success! Connected to the Student database.")
    
    
    my_db.close()
    print("Database connection closed.")