import mysql.connector

class Database:
    def __init__(self):
        
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Proma.com2003",
            database="bank_db"
        )
       
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(20) NOT NULL,
                email VARCHAR(50) NOT NULL,
                phone_number VARCHAR(15) NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                amount DECIMAL(10,2) NOT NULL,
                transaction_type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        
        self.connection.commit()

    def add_user(self, username, email, phone_number, password):
       
        query = "INSERT INTO users (username, email, phone_number, password) VALUES (%s, %s, %s, %s)"
        values = (username, email, phone_number, password)
        self.cursor.execute(query, values)
        self.connection.commit()

    def authenticate_user(self, phone_number, password):
        
        query = "SELECT * FROM users WHERE phone_number = %s AND password = %s"
        values = (phone_number, password)
        self.cursor.execute(query, values)
        user = self.cursor.fetchone()
        return True if user else False

    def get_user_id(self, phone_number):
        
        query = "SELECT user_id FROM users WHERE phone_number = %s"
        values = (phone_number,)
        self.cursor.execute(query, values)
        user_id = self.cursor.fetchone()
        return user_id[0] if user_id else None

    def get_balance(self, user_id):
       
        query = "SELECT SUM(amount) FROM transactions WHERE user_id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        balance = self.cursor.fetchone()[0]
        return balance if balance else 0.0

    def update_balance(self, user_id, new_balance):
       
        query = "INSERT INTO transactions (user_id, amount, transaction_type) VALUES (%s, %s, 'deposit')"
        values = (user_id, new_balance)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_transactions(self, user_id):
        
        query = "SELECT * FROM transactions WHERE user_id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        transactions = self.cursor.fetchall()
        return transactions

    def change_password(self, user_id, new_password):
       
        query = "UPDATE users SET password = %s WHERE user_id = %s"
        values = (new_password, user_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_email(self, user_id, new_email):
        
        query = "UPDATE users SET email = %s WHERE user_id = %s"
        values = (new_email, user_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_phone_number(self, user_id, new_phone_number):
        
        query = "UPDATE users SET phone_number = %s WHERE user_id = %s"
        values = (new_phone_number, user_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def user_exists(self, user_id):
        
        query = "SELECT * FROM users WHERE user_id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        user = self.cursor.fetchone()
        return True if user else False

    def close(self):
       
        self.cursor.close()
        self.connection.close()
