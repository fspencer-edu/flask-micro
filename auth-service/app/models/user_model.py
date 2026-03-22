from app.db import mysql

class UserModel():
    @staticmethod
    def create_user(name, email, password_hash):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password_hash)
        )
        mysql.connect.commit()
        user_id = cur.lastrowid
        cur.close()
        return user_id
    
    @staticmethod
    def find_by_email(email):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT id, name, email, password FROM users WHERE email =%s",
            (email,)
        )
        row = cur.fetchone()
        cur.close()
        return row
    
    @staticmethod
    def find_by_id(user_id):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT id, name, email FROM users WHERE id = %s",
            (user_id,)
        )
        row = cur.fetchone()
        cur.close()
        return row