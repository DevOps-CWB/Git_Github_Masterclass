import unittest
from app.utils import add_task, list_tasks

class TestUtils(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        new_task = add_task(tasks, "Learn GitHub")
        self.assertEqual(new_task["task"], "Learn GitHub")
        self.assertEqual(len(tasks), 1)

    def test_list_tasks(self):
        tasks = [{"id": 1, "task": "Initial Task"}]
        result = list_tasks(tasks)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["task"], "Initial Task")

if __name__ == "__main__":
    unittest.main()
