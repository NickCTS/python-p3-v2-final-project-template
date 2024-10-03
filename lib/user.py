import sqlite3

class User:
    @staticmethod
    def create(username):
        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()  # Commit the changes to save them
            return cursor.lastrowid  # Return the new user's ID
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
            return None  # Return None if the user already exists
        finally:
            conn.close()

    @staticmethod
    def delete(username):
        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def find_by_username(username):
        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        return user  # This will return the user's data or None if not found
