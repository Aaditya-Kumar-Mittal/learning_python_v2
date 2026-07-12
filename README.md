# 🐍 Python Learning Environment Setup Guide

This guide contains the commands I need whenever I create a new Python project.

---

## Step 1: Open Terminal

Open the project folder in VS Code.

Shortcut:

```keyboard
Ctrl + `
```

---

## Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

This creates a virtual environment named `.venv`.

---

## Step 3: Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

If activated successfully, the terminal becomes:

```text
(.venv) C:\Users\Aaditya\Python\MyProject>
```

---

## Step 4: Verify Python

```bash
python --version
```

Example output:

```text
Python 3.13.7
```

---

## Step 5: Verify pip

```bash
pip --version
```

---

## Step 6: Install Packages

Example:

```bash
pip install requests
```

Install multiple packages:

```bash
pip install numpy pandas matplotlib
```

---

## Step 7: Save Installed Packages

```bash
pip freeze > requirements.txt
```

This creates a file containing all installed packages.

---

## Step 8: Install Packages Again

If you clone the project later:

```bash
pip install -r requirements.txt
```

---

## Step 9: Check Installed Packages

```bash
pip list
```

---

## Step 10: Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## Step 11: Run Python File

```bash
python main.py
```

---

## Step 12: Open Python Interpreter

```bash
python
```

Example:

```python
>>> print("Hello World")
```

Exit:

```python
exit()
```

---

## Step 13: Deactivate Virtual Environment

```bash
deactivate
```

---

## Step 14: Delete Virtual Environment

Simply delete the `.venv` folder.

Then recreate it whenever needed:

```bash
python -m venv .venv
```

---

## Useful Commands

Current Python version:

```bash
python --version
```

Current Python executable:

```bash
python -c "import sys; print(sys.executable)"
```

Installed packages:

```bash
pip list
```

Package details:

```bash
pip show requests
```

Update a package:

```bash
pip install --upgrade requests
```

Remove a package:

```bash
pip uninstall requests
```

---

## Typical Workflow

1. Create project folder.
2. Open folder in VS Code.
3. Create virtual environment.
4. Activate it.
5. Install required packages.
6. Write code.
7. Run the program.
8. Save dependencies (`requirements.txt`) if needed.
9. Deactivate the environment when finished.
# learning_python_v2
