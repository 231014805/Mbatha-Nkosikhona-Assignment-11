# Mbatha-Nkosikhona-Assignment-11
.
├── models                          # Entity classes (Student, Counselor, Appointment)
│   └── student.py
├── repositories                    # Repository interfaces and implementations
│   ├── repository.py               # Generic Repository Interface
│   ├── student_repository.py       # Entity-specific Repository Interface
│   ├── inmemory
│   │   └── in_memory_student_repository.py  # In-memory implementation
│   └── filesystem
│       └── file_system_student_repository.py  # (Optional) File-based implementation
├── factories                       # Repository Factory for dynamic selection
│   └── repository_factory.py
├── tests                           # Unit tests for repositories
│   └── test_in_memory_student_repository.py
└── README.md                       # Project documentation
