<h1 align="center">Employee Management Application</h1>

<p align="center">
A simple Django-based web application to efficiently manage employee records with automatic, non-reusable employee ID generation.
</p>

---

## Features

### Employee Management
- Add new employees with details:
  - Name  
  - Designation  
  - Salary  
  - Skills  
- Each employee is assigned a **unique Employee ID (empId)** in the format `E001`, `E002`, `E003`, etc.  

---

### ID Generation Logic
- A dedicated model `EmployeeCounter` tracks the last used employee number.
- On creating a new employee:
  - The system fetches the next available ID.
  - The counter increments and stores the latest number permanently.
- Ensures deleted employee IDs are **never reassigned**.

---

### Employee Form
- Employee ID field is **auto-filled** and **read-only**.
- Fields available:
  - Employee Name
  - Designation
  - Salary
  - Skills

---

### Database Models
- **Employee** – stores employee details.  
- **EmployeeCounter** – maintains the last used ID for unique ID generation.

---

### Tech Stack
| Component | Technology |
|------------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS (Bootstrap) |
| **Database** | SQLite (default Django DB) |

### Author
<p align="center"> <b>Dharshini R</b> <br> Employee Management Application | Django | Python | 2025 </p> ```
