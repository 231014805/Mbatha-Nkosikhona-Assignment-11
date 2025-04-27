from typing import Optional, List
from models import Student

class InMemoryStudentRepository:
    def __init__(self):
        self._storage = {}  # In-memory storage

    def save(self, student: Student) -> None:
        self._storage[student.student_id] = student

    def find_by_id(self, student_id: str) -> Optional[Student]:
        return self._storage.get(student_id)

    def find_all(self) -> List[Student]:
        return list(self._storage.values())

    def delete(self, student_id: str) -> None:
        if student_id in self._storage:
            del self._storage[student_id]
