import unittest
import json
from flask_app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Task Manager App!", response.data)

    def test_get_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    def test_create_task(self):
        response = self.app.post(
            '/tasks',
            json={"title": "Test Task"}
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["title"], "Test Task")

    def test_update_task(self):
        response = self.app.put(
            '/tasks/1',
            json={"title": "Updated Task", "completed": True}
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["title"], "Updated Task")
        self.assertTrue(data["completed"])

    def test_delete_task(self):
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["result"], "Task deleted")

if __name__ == "__main__":
    unittest.main()
