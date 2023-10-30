import sqlite3
import datetime
from datetime import timedelta
import os

current_directory = os.getcwd()
database_path = os.path.join(current_directory, 'data', 'database.db')
connection = sqlite3.connect(database_path)

#Общая таблица "users"

class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                join_date DATETIME NOT NULL DEFAULT (DATETIME('now')),
                firstname TEXT,
                ages INTEGER,
                gender TEXT,
                why TEXT,
                is_paid INTEGER DEFAULT 0,
                onetimepromo INTEGER DEFAULT 0,
                expiry_date DATETIME,
                active INTEGER DEFAULT 0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS onemonth (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE NOT NULL,
                sub_date DATETIME DEFAULT (DATETIME('now')),
                paid_month INTEGER DEFAULT 0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sixmonth (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE NOT NULL,
                sub_date DATETIME DEFAULT (DATETIME('now')),
                paid_sixmonth INTEGER DEFAULT 0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS promo (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE NOT NULL
            )
        """)
        self.connection.commit()

#Таблица USERS
    def add_user(self, user_id, username):
         with self.connection:
            return self.cursor.execute("INSERT OR IGNORE INTO 'users' (user_id, username) VALUES (?, ?)", (user_id, username))
         
    def user_exists(self, user_id):
         with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))
   
    def set_firstname(self, user_id, firstname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `firstname` = ? WHERE `user_id` = ?", (firstname, user_id,))
        
    def set_ages(self, user_id, ages):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `ages` = ? WHERE `user_id` = ?", (ages, user_id,))
        
    def set_gender(self, user_id, gender):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `gender` = ? WHERE `user_id` = ?", (gender, user_id,))
        
    def set_why(self, user_id, why):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `why` = ? WHERE `user_id` = ?", (why, user_id,))
        
    def set_is_paid(self, user_id, is_paid):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `is_paid` = ? WHERE `user_id` = ?", (is_paid, user_id,))
        
    def set_onetimepromo(self, user_id, onetimepromo):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `onetimepromo` = ? WHERE `user_id` = ?", (onetimepromo, user_id,))
        
    def get_onetimepromo(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT `onetimepromo` FROM `users` WHERE `user_id` = ?", (user_id,))
            result = self.cursor.fetchone()
            if result is not None:
                return result[0]
            else:
                return None

    def get_is_paid(self, is_paid):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users WHERE is_paid = ?", (is_paid,))
            result = self.cursor.fetchall()
            return result
        
    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `user_id` = ?", (active, user_id,))
        
    def get_allusers(self):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users")
            result = self.cursor.fetchall()
            users = [row[0] for row in result]
            return users if users else []
        
    def get_expirycheck(self):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users")
            result = self.cursor.fetchall()
            users = [row[0] for row in result]
            return users if users else []
     
    def get_total_users(self):
            result = self.cursor.execute("SELECT COUNT(*) FROM 'users'").fetchone()
            if result:
                 return result[0]
            else:
                 return 0
            
    def get_expiry_date(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT expiry_date FROM users WHERE user_id = ?", (user_id,))
            result = self.cursor.fetchone()
            expiry_date_str = None  # Инициализация переменной
        if result is not None and result[0] is not None:
            expiry_date_str = result[0]
        if expiry_date_str:
            expiry_date = datetime.datetime.strptime(expiry_date_str, "%Y-%m-%d %H:%M:%S.%f")
            if expiry_date <= datetime.datetime.now():
                self.null_subscription(user_id)  # Обновить подписку пользователя
                return None
            else:
                return expiry_date
        return None
        
    def null_subscription(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE users SET expiry_date = NULL, is_paid = 0 WHERE user_id = ?", (user_id,))
            self.connection.commit()
        
#Таблица подписки "promo"
    def add_user_promo(self, user_id):
         expiry_date = datetime.datetime.now() + datetime.timedelta(days=2)
         with self.connection:
             return self.cursor.execute("INSERT OR IGNORE INTO 'promo' ('user_id') VALUES (?)", (user_id, expiry_date))
         
    def user_exists_promo(self, user_id):
         with self.connection:
            result = self.cursor.execute("SELECT * FROM 'promo' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))
         
    def set_promo(self, user_id):
         expiry_date = datetime.datetime.now() + datetime.timedelta(days=2)
         with self.connection:
            return self.cursor.execute("UPDATE `users` SET `expiry_date` = ? WHERE `user_id` = ?", (expiry_date, user_id))

#Таблица подписки "onemonth"
    def add_user_month(self, user_id):
         with self.connection:
             return self.cursor.execute("INSERT OR IGNORE INTO 'onemonth' (user_id) VALUES (?)", (user_id,))

    def user_exists_month(self, user_id):
         with self.connection:
            result = self.cursor.execute("SELECT * FROM 'onemonth' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_paid_month(self, user_id):
         expiry_date = datetime.datetime.now() + datetime.timedelta(days=31)
         with self.connection:
            return self.cursor.execute("UPDATE `users` SET `expiry_date` = ? WHERE `user_id` = ?", (expiry_date, user_id))
        
#Таблица подписки "sixmonth"
    def add_user_sixmonth(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT OR IGNORE INTO 'sixmonth' ('user_id') VALUES (?)", (user_id,))

    def user_exists_sixmonth(self, user_id):
         with self.connection:
            result = self.cursor.execute("SELECT * FROM 'sixmonth' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_paid_sixmonth(self, user_id):
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=31*6)
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `expiry_date` = ? WHERE `user_id` = ?", (expiry_date, user_id))

    def close(self):
         self.connection.close()