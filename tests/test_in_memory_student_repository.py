import unittest
from repositories.inmemory.in_memory_student_repository import InMemoryStudentRepository
from models import Student

class TestInMemoryStudentRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryStudentRepository()
        self.student = Student("S123", "John Doe", "john@example.com", "123-4567")

    def test_save_and_find_by_id(self):
        self.repo.save(self.student)
        result = self.repo.find_by_id("S123")
        self.assertEqual(result.name, "John Doe")

    def test_find_all(self):
        self.repo.save(self.student)
        all_students = self.repo.find_all()
        self.assertEqual(len(all_students), 1)

    def test_delete(self):
        self.repo.save(self.student)
        self.repo.delete("S123")
        self.assertIsNone(self.repo.find_by_id("S123"))

if __name__ == "__main__":
    unittest.main()
