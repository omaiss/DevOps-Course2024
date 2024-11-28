# 📝 Task Manager Flask App

Welcome to the **Task Manager Flask App**! This is a RESTful API built using Flask to manage tasks. It includes features like creating, reading, updating, and deleting tasks (CRUD operations). The app is integrated with **GitHub Actions** for Continuous Integration (CI) to ensure code quality through automated testing.

---

## 🚀 Features
- **View all tasks**: Fetch a list of tasks.
- **View a single task**: Get details about a specific task.
- **Add a new task**: Create a task with a title and status.
- **Update a task**: Modify the title or completion status of a task.
- **Delete a task**: Remove a task from the list.

---

## 🛠️ Endpoints

### Base URL
```
http://127.0.0.1:5000
```

### Routes

| Method | Endpoint         | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/`              | Welcome message                   |
| GET    | `/tasks`         | Get all tasks                     |
| GET    | `/tasks/<id>`    | Get a specific task by ID          |
| POST   | `/tasks`         | Create a new task                 |
| PUT    | `/tasks/<id>`    | Update a task by ID               |
| DELETE | `/tasks/<id>`    | Delete a task by ID               |

---

## 📦 Example JSON Payloads

### Create a Task
```json
{
  "title": "Learn Flask"
}
```

### Update a Task
```json
{
  "title": "Master Flask",
  "completed": true
}
```

---

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/omaiss/Home-Care-Pro.git
   cd Home-Care-Pro
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser or API testing tool (like Postman) and interact with the app.

---

## 🧪 Running Tests
The app includes unit tests to ensure functionality. Run the tests with the following command:
```bash
python -m unittest discover -s tests
```

---

## ⚙️ GitHub Actions Integration
This project uses **GitHub Actions** for Continuous Integration. Every push to the `main` branch or pull request triggers the following actions:
- Install dependencies.
- Run the unit tests in the `tests` folder.

You can find the workflow configuration in `.github/workflows/python-app.yml`.

---

## 📄 File Structure

```
📁 Home-Care-Pro/
├── 📁 .github/
│   └── 📁 workflows/
│       └── python-app.yml  # GitHub Actions workflow
├── 📁 tests/
│   └── test_app.py         # Unit tests for the Flask app
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

## 🎯 Future Improvements
- Add a database to persist tasks.
- Implement user authentication and authorization.
- Deploy the app to a cloud provider (e.g., AWS, Heroku).

---

## 🤝 Contributions
Feel free to fork the repository and open a pull request for any feature suggestions or bug fixes.

---

## 📫 Contact
For any questions or suggestions:
- **GitHub**: [omaiss](https://github.com/omaiss)
- **Email**: omaisafzal225@gmail.com
