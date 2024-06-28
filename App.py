from flask import Flask, request, redirect, render_template_string, abort
import mysql.connector

app=Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'Sneha',
    'password': 'root',
    'host': 'localhost',
    'database': 'python'
}


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)
        
        # Insert new user into database
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Redirect to /users page
        return redirect('/users')
    
    # HTML template for new user form
    html_template = """
    <!doctype html>
    <html>
        <head>
            <title>New User</title>
        </head>
        <body>
            <h1>Add New User</h1>
            <form method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    
    # Render the HTML template for the form
    return render_template_string(html_template)

@app.route('/users')
def users():
    # Connect to MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Execute query to retrieve users
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # HTML template to display users in a table
    html_template = """
    <!doctype html>
    <html>
        <head>
            <title>Users List</title>
        </head>
        <body>
            <h1>Users List</h1>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
                {% for user in users %}
                <tr>
                    <td>{{ user[0] }}</td>
                    <td>{{ user[1] }}</td>
                    <td>{{ user[2] }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """
    
    # Render the HTML template with users data
    return render_template_string(html_template, users=users)

@app.route('/users/<int:id>')
def user_detail(id):
    # Connect to MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Execute query to retrieve the specific user
    cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    if user is None:
        abort(404)  # If user not found, return 404 error

    # HTML template to display user details
    html_template = """
    <!doctype html>
    <html>
        <head>
            <title>User Details</title>
        </head>
        <body>
            <h1>User Details</h1>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
                <tr>
                    <td>{{ user[0] }}</td>
                    <td>{{ user[1] }}</td>
                    <td>{{ user[2] }}</td>
                </tr>
            </table>
            <a href="/users">Back to Users List</a>
        </body>
    </html>
    """
    
    # Render the HTML template with user data
    return render_template_string(html_template, user=user)

@app.errorhandler(404)
def page_not_found(e):
    # HTML template for 404 error page
    html_template = """
    <!doctype html>
    <html>
        <head>
            <title>Page Not Found</title>
        </head>
        <body>
            <h1>404 - Page Not Found</h1>
            <p>The page you are looking for does not exist.</p>
            <a href="/users">Back to Users List</a>
        </body>
    </html>
    """
    
    # Render the HTML template for 404 error page
    return render_template_string(html_template), 404

if __name__ == '__main__':
    app.run(debug=True)