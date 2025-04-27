import json
from models import Student

class FileSystemStudentRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, student: Student) -> None:
        students = self._load_all()
        students[student.student_id] = student
        with open(self.file_path, 'w') as f:
            json.dump(students, f)

    def _load_all(self) -> dict:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
