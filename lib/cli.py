import click
from lib.helpers import initialize_db
from lib.user import User
from lib.workout import Workout

@click.group()
def cli():
    """Fitness Tracker CLI"""
    pass

@cli.command()
@click.argument('username')
def add_user(username):
    """Add a new user"""
    if not username.strip():
        click.echo("Username cannot be empty.")
        return
    user_id = User.create(username)
    if user_id:
        click.echo(f"User '{username}' added with ID {user_id}.")
    else:
        click.echo(f"Failed to add user '{username}'.")

@cli.command()
@click.argument('username')
def delete_user(username):
    """Delete a user"""
    if not username.strip():
        click.echo("Username cannot be empty.")
        return
    User.delete(username)
    click.echo(f"User '{username}' deleted.")

@cli.command()
def list_users():
    """List all users"""
    users = User.get_all()
    for user in users:
        click.echo(user)

@cli.command()
@click.argument('username')
@click.argument('workout_type')
@click.argument('duration', type=int)
@click.argument('date')
def add_workout(username, workout_type, duration, date):
    """Add a workout for a user"""
    if duration <= 0:
        click.echo("Duration must be a positive number.")
        return

    workout_id = Workout.create(username, workout_type, duration, date)
    if workout_id:
        click.echo(f"Workout added for user '{username}' with ID {workout_id}.")
    else:
        click.echo(f"Failed to add workout for user '{username}'.")

@cli.command()
@click.argument('workout_id', type=int)
def delete_workout(workout_id):
    """Delete a workout"""
    Workout.delete(workout_id)
    click.echo(f"Workout with ID '{workout_id}' deleted.")

@cli.command()
def list_workouts():
    """List all workouts"""
    workouts = Workout.get_all()
    for workout in workouts:
        click.echo(workout)

@cli.command()
@click.argument('username')
def list_workouts_by_user(username):
    """List all workouts for a specific user"""
    if not username.strip():
        click.echo("Username cannot be empty.")
        return
    
    user = User.find_by_username(username)
    if user is None:
        click.echo(f"User '{username}' not found.")
        return
    
    workouts = Workout.get_all()  # You can implement a more specific method to get workouts by user ID.
    user_workouts = [w for w in workouts if w[1] == user[0]]  # Assuming user[0] is user_id.
    
    if not user_workouts:
        click.echo(f"No workouts found for user '{username}'.")
    else:
        click.echo(f"Workouts for user '{username}':")
        for workout in user_workouts:
            click.echo(workout)

if __name__ == '__main__':
    initialize_db()  # Ensure the database is initialized when the CLI starts
    cli()
