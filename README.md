# 📝 Task Tracker CLI

A simple command-line task tracker built with Python using an object-oriented approach. Tasks are stored in a local JSON file and support full lifecycle management: creation, listing, updating, and deletion — all from your terminal.

---

## 🚀 Features

- ✅ Add new tasks  
- 📋 List tasks (all, or filtered by status: `todo`, `in-progress`, or `done`)  
- ✏️ Update task descriptions  
- 📌 Mark tasks as:
  - `todo`
  - `in-progress`
  - `done`
- ❌ Delete individual tasks with confirmation  
- 🧨 Clear all tasks with confirmation  
- 💾 Data is saved persistently to `tasks.json`  
- 🧱 Object-oriented design for clean, maintainable code  

---

## 📦 Requirements

- Python 3.6+
- No external libraries — uses only the Python Standard Library (`argparse`, `json`, `datetime`, `os`)

---

## 🔧 Setup

```bash
git clone https://github.com/diegomarinr99/task-tracker-cli
cd task-tracker-cli
python3 main.py --help
https://roadmap.sh/projects/task-tracker
```

---

## 📌 Usage

Each action is a subcommand of `main.py`. Here's how to use it:

### ➕ Add a new task
```bash
python3 main.py add "Buy groceries"
```

### 📋 List all tasks
```bash
python3 main.py list
```

### ✅ List only `done` tasks
```bash
python3 main.py list --done
```

### 🕒 List only `in-progress` tasks
```bash
python3 main.py list --progress
```

### 📌 List only `todo` tasks
```bash
python3 main.py list --todo
```

### ✔️ Mark a task as `done`
```bash
python3 main.py done 2
```

### 🔄 Mark a task as `in-progress`
```bash
python3 main.py progress 2
```

### 💤 Mark a task as `todo` again
```bash
python3 main.py todo 2
```

### 📝 Update a task’s description
```bash
python3 main.py update 2 "Buy groceries and cook dinner"
```

### 🗑️ Delete a task
```bash
python3 main.py del 2
```

### 💥 Clear all tasks (with confirmation)
```bash
python3 main.py clear
```

---

## 🗂 Data Storage

All tasks are saved in a `tasks.json` file. Each task has:

- `id`: Unique identifier (auto-incremented)
- `description`: Task description
- `status`: `"todo"`, `"progress"`, or `"done"`
- `createdAt`: Timestamp when created
- `updatedAt`: Timestamp when last updated

---

## 🧠 Code Structure

- `main.py` — CLI interface using `argparse`
- `task_manager.py` — Manages task logic and storage
- `task.py` — Defines the `Task` class

---

## 👨‍💻 Author

**Diego Marín**  
Built as a hands-on project to learn Python and object-oriented programming through real problem-solving.

---

## 📄 License

MIT License — feel free to use, modify, and share.
