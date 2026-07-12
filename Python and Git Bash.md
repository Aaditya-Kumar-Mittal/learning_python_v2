# 🐍 Python Development Workflow (Git Bash + VS Code)

This guide contains the commands I use whenever I create a new Python learning folder or project.

---

## 📁 Recommended Folder Structure

```text
learning_python/
│
├── 01_basics/
│   ├── .venv/
│   ├── main.py
│   └── notes.md
│
├── 02_variables/
│   ├── .venv/
│   ├── main.py
│   └── notes.md
│
├── 03_strings/
│   ├── .venv/
│   ├── main.py
│   └── notes.md
│
└── ...
```

---

## 🚀 Step 1: Open the Folder

```bash
cd /d/learning_python/01_basics
```

Open it in VS Code:

```bash
code .
```

---

## 🚀 Step 2: Check Python Installation

```bash
python --version
```

Expected Output:

```text
Python 3.13.x
```

Check where Python is installed:

```bash
which python
```

---

## 🚀 Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

This creates a virtual environment named `.venv`.

---

## 🚀 Step 4: Activate the Virtual Environment (Git Bash)

```bash
source .venv/Scripts/activate
```

or

```bash
. .venv/Scripts/activate
```

If activated successfully:

```text
(.venv) Aaditya@MSI MINGW64 ...
```

---

## 🚀 Step 5: Verify Python

```bash
python --version
```

Check which Python is currently being used:

```bash
which python
```

It should point inside:

```text
.../.venv/Scripts/python
```

---

## 🚀 Step 6: Verify pip

```bash
pip --version
```

---

## 🚀 Step 7: Install Packages

Example:

```bash
pip install requests
```

Install multiple packages:

```bash
pip install numpy pandas matplotlib
```

---

## 🚀 Step 8: View Installed Packages

```bash
pip list
```

Package information:

```bash
pip show requests
```

---

## 🚀 Step 9: Save Dependencies

```bash
pip freeze > requirements.txt
```

---

## 🚀 Step 10: Install Dependencies Later

```bash
pip install -r requirements.txt
```

---

## 🚀 Step 11: Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 🚀 Step 12: Run a Python Program

```bash
python main.py
```

Example:

```bash
python hello.py
```

---

## 🚀 Step 13: Start the Python Interpreter

```bash
python
```

Example:

```python
>>> print("Hello, World!")
Hello, World!
```

Exit:

```python
exit()
```

or press:

```text
Ctrl + D
```

---

## 🚀 Step 14: Deactivate the Virtual Environment

```bash
deactivate
```

---

## 🚀 Step 15: Delete the Virtual Environment

```bash
rm -rf .venv
```

---

## 🚀 Step 16: Recreate the Virtual Environment

```bash
python -m venv .venv
```

Activate it again:

```bash
source .venv/Scripts/activate
```

---

## 🚀 Step 17: Common Git Bash Commands

Current folder:

```bash
pwd
```

List files:

```bash
ls
```

List all files (including hidden):

```bash
ls -la
```

Create a folder:

```bash
mkdir my_folder
```

Change folder:

```bash
cd my_folder
```

Go back one folder:

```bash
cd ..
```

Delete a file:

```bash
rm filename.py
```

Delete a folder:

```bash
rm -rf folder_name
```

Clear the terminal:

```bash
clear
```

---

## 🚀 Step 18: VS Code Commands

Open current folder:

```bash
code .
```

Open a specific file:

```bash
code main.py
```

---

## 📌 Typical Workflow

```text
1. Create a new folder.
2. cd into the folder.
3. Open it in VS Code.
4. Create a virtual environment.
5. Activate the virtual environment.
6. Verify Python.
7. Install packages (if needed).
8. Write your code.
9. Run your program.
10. Deactivate the virtual environment when finished.
```

---

## ⚡ Daily Commands

```bash
cd /d/learning_python/01_basics

code .

python -m venv .venv

source .venv/Scripts/activate

python --version

pip install requests

python main.py

deactivate
```

---

## 🧹 If Something Goes Wrong

Delete the old virtual environment:

```bash
rm -rf .venv
```

Create it again:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/Scripts/activate
```

---

## 💡 Best Practices

- Use one `.venv` per **real project**.
- Commit `requirements.txt` to Git.
- Do **not** commit `.venv/` to Git.
- Add `.venv/` to your `.gitignore`.
- Keep your code, notes, and exercises organized by topic.
