Task 1: Flask Api Development

This is a simple Flask application to manage users. It provides routes to add new users, list all users, and retrieve user details from a MySQL database. It also includes basic error handling for cases when a user or resource is not found.

## Features

- /hello - Returns "Hello, World!"
- /new_user - Renders an HTML form to accept input from the user and stores the information in the database.
- /users - Retrieves a list of users from the MySQL database and displays them in an HTML table.
- /users/<id> - Retrieves a specific user's details from the database.
- Error handling for user or resource not found (404).

## Requirements

- Python 3.x
- Flask
- MySQL

## Installation

1. *Clone the repository:*
    bash
    git clone
    cd flask-user-management
    

2. *Set up a virtual environment:*
    bash
    python3 -m venv venv
    source venv/bin/activate
    

3. *Install the dependencies:*
    bash
    pip install Flask mysql-connector-python
    

4. *Set up the MySQL database:*
    - Create a database named pyproject.
    - Update the db_config dictionary in app.py with your MySQL user credentials.

    python
    db_config = {
        'user': 'your_mysql_username',
        'password': 'your_mysql_password',
        'host': 'localhost',
        'database': 'pyproject'
    }
    

5. *Run the application:*
    bash
    python app.py
    

## Usage

- *Access the "Hello, World!" page:*
    - Go to http://localhost:5000/hello
- *Add a new user:*
    - Go to http://localhost:5000/new_user
    - Fill in the form and submit.
- *View the list of users:*
    - Go to http://localhost:5000/users
- *View a specific user's details:*
    - Go to http://localhost:5000/users/<id>, replacing <id> with the user's ID.

## Error Handling

- If a user or resource is not found, a custom 404 error page is displayed.



Task 2 : Database Interaction

Prerequisites
MySQL server installed
MySQL client or any MySQL management tool (e.g., MySQL Workbench, phpMyAdmin)
Steps and SQL Queries
1. Create the Database
Create the database named "users":
2. Use the Database
Switch to the "users" database:
3. Create the "users" Table
Create a table named "users" with the following columns:

id (int, primary key)
name (varchar)
email (varchar)
role (varchar)
4. Insert Sample Data into the "users" Table
Insert sample data into the "users" table:
5. Retrieve All Users from the "users" Table
Retrieve all users from the "users" table:
6. Retrieve a Specific User by Their ID
Retrieve a specific user by their ID (replace 1 with the desired user ID):

