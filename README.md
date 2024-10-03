# Fitness Tracker CLI

## Overview
The Fitness Tracker CLI is a command-line application that allows users to manage their fitness activities. Users can create accounts, log workouts, and retrieve workout information. The application is built using Python and SQLite and follows object-oriented programming principles.

## Features
- Add and delete users
- Add and delete workouts associated with users
- List all users and workouts
- List workouts by specific users
- Simple command-line interface for easy interaction

## Requirements
- Python 3.x
- SQLite
- Click (for CLI)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fitness-tracker-cli.git
   cd fitness-tracker-cli

Install dependencies using Pipenv: 
        pipenv install

To start the application, run the following command: 
        pipenv run python -m lib.cli

Commands
Add User:pipenv run python -m lib.cli add-user <username>
Adds a new user with the specified username.

Delete User: pipenv run python -m lib.cli delete-user <username>
Deletes the specified user.

List Users: pipenv run python -m lib.cli list-users
Displays all users.

Add Workout: pipenv run python -m lib.cli add-workout <username> <workout_type> <duration> <date>
Adds a workout for the specified user. Requires username, workout type, duration (in minutes), and date (YYYY-MM-DD).

Delete Workout: pipenv run python -m lib.cli delete-workout <workout_id>
Deletes a workout by its ID.

List Workouts: pipenv run python -m lib.cli list-workouts
Displays all workouts.

List Workouts by User:pipenv run python -m lib.cli list-workouts-by-user <username>
Displays all workouts associated with a specified user.
