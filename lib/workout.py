import sqlite3
from lib.user import User  # Import the User class

class Workout:
    @staticmethod
    def create(username, workout_type, duration, date):
        user = User.find_by_username(username)

        if user is None:
            print(f"User '{username}' not found. Workout not added.")
            return None

        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO workouts (user_id, workout_type, duration, date)
            VALUES (?, ?, ?, ?)
        ''', (user[0], workout_type, duration, date))  # Use user[0] to get the user's ID
        conn.commit()
        workout_id = cursor.lastrowid  # Get the ID of the newly created workout
        conn.close()

        return workout_id

    @staticmethod
    def delete(workout_id):
        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('fitness_tracker.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM workouts")
        workouts = cursor.fetchall()
        conn.close()
        return workouts
