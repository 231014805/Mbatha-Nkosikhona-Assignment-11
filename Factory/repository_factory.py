from repositories.inmemory.in_memory_student_repository import InMemoryStudentRepository
# Future import: from repositories.filesystem.file_system_student_repository import FileSystemStudentRepository

class RepositoryFactory:
    @staticmethod
    def get_student_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryStudentRepository()
        # elif storage_type == "FILE":
        #     return FileSystemStudentRepository("/path/to/storage.json")
        else:
            raise ValueError(f"Invalid storage type: {storage_type}")

