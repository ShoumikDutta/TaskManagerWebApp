# Task Manager Web Application

This is a simple task manager web application built using Flask framework. It allows users to register, login, add tasks, mark tasks as done, and delete tasks.

## Prerequisites

- Python 3.x
- Flask
- SQLite

## Getting Started

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:
   ```
   pip install flask
   ```
3. Create an SQLite database file named `data.db` in the same directory as the code.
4. Run the `app.py` file to start the application.
   ```
   python app.py
   ```
5. Open a web browser and visit `http://localhost:5000` to access the application.

## Usage

- Home page ("/"): Displays the list of tasks for the logged-in user. If the user is not logged in, it redirects to the login page.
- Login page ("/login"): Allows users to log in with their username and password.
- Register page ("/register"): Allows new users to register by providing a username and password.
- Logout ("/logout"): Logs out the current user and redirects to the login page.
- Add task ("/add"): Adds a new task for the logged-in user.
- Delete task ("/delete"): Deletes a task for the logged-in user.
- Mark task as done ("/markAsDone"): Marks a task as done for the logged-in user.

## Database Structure

The application uses an SQLite database to store user information and tasks. The database file is named `data.db`. It contains two tables:

1. users:
   - Columns: name (username), password (hashed password)

2. {username}Task:
   - Columns: task (task name), done (boolean indicating task completion)

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality of the application, feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
