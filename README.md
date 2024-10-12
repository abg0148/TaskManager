
# Task Manager App

This is a simple command-line task manager application written in Python. The app allows users to authenticate, add, view, and delete tasks. All task information is stored in an in-memory SQLite database.

## Features

- **User Authentication**: Simple authentication system to ensure only authorized users can manage tasks.
- **Add Tasks**: Users can add new tasks with a description.
- **View Tasks**: Users can retrieve and view all tasks from the database.
- **Delete Tasks**: Users can delete tasks by their ID.
- **Persistent Task Storage**: Tasks are stored in a database and remain available during the runtime of the app.

## Project Structure

```
task_manager_app/
│
├── app.py          # Main application logic
├── auth.py         # User authentication module
└── db.py           # Database interaction module
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/task_manager_app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd task_manager_app
   ```

3. Ensure you have Python 3 installed. You can check this by running:

   ```bash
   python --version
   ```

4. No additional dependencies are needed as SQLite is included with Python by default.

## Usage

1. Run the app:

   ```bash
   python app.py
   ```

2. After running the app, you'll be prompted to log in with a username and password. Use the following credentials:

   - **Username**: `admin`
   - **Password**: `password123`

3. Once authenticated, you can choose from the following options:

   - Add a new task
   - View all tasks
   - Delete a task
   - Exit the application

### Example Flow

1. **Login**:
   - You will be prompted to enter the username and password.

2. **Adding a Task**:
   - Choose option `1` to add a task.
   - Enter the task description, and it will be added to the database.

3. **Viewing Tasks**:
   - Choose option `2` to view all tasks.
   - All tasks will be displayed with their IDs and descriptions.

4. **Deleting a Task**:
   - Choose option `3` to delete a task.
   - Enter the task ID to remove it from the database.

5. **Exiting**:
   - Choose option `4` to exit the application.

## Future Improvements

- **Persistent Storage**: Currently, tasks are stored in memory and will be lost when the application closes. This can be updated to use a persistent database like SQLite on disk or another database engine.
- **User Management**: Allow users to register and manage their own tasks with individual accounts.

## License

This project is licensed under the MIT License. Feel free to modify and use it for your own needs.

---

### Thank You for Using the Task Manager App!


P.S.  This is a repo for demo purposes only. Some bugs and vulnerabilities are introduced in this intentionally, for our scanning application to detect them and suggest resolutions 
