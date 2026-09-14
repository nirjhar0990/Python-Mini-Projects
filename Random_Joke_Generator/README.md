# 😂 Random Joke Generator

A simple, lightweight Windows desktop application built with **Python** and **Tkinter** that fetches random setup/punchline jokes from the **Official Joke API** and displays them in a neat graphical user interface.

This repository demonstrates practical GUI development, REST API integration, exception handling, resource bundling for PyInstaller, and standalone executable packaging.

---

## 📸 Application Preview

<img width="756" height="546" alt="image" src="https://github.com/user-attachments/assets/fa392c15-c8cc-432c-afbd-ff7a20d57f5d" />


---

## 📌 Project Overview

The application provides an effortless one-click interface to pull jokes live from the web:

1. The user clicks **🎲 Get Random Joke**.
2. The app sends an HTTP `GET` request to the Official Joke API (`https://official-joke-api.appspot.com/random_joke`).
3. The JSON response is parsed into a **Setup** and a **Punchline**.
4. Both elements are updated dynamically on the screen.
5. If the user is offline or the server fails, clean error popups alert the user without crashing the app.

---

## ✨ Features

- 😂 Generate a random joke
- 🎲 Simple one-click interface
- 🖥️ Windows desktop GUI[cite: 3]
- 🌐 Uses an external REST API[cite: 3]
- 📡 Retrieves data using HTTP requests[cite: 3]
- 📋 Processes JSON API responses[cite: 3]
- ⚡ Five-second API timeout
- ❌ Handles API/server errors[cite: 3]
- 🌐 Handles internet connection errors[cite: 3]
- 🖼️ Custom application icon (`tongue.ico`)[cite: 3]
- 📦 Can be packaged into a standalone Windows `.exe`[cite: 3]
- 🔌 No database required
- 🔐 No user account required

---

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| **Python** | Core programming language[cite: 3] |
| **Tkinter** | Standard GUI toolkit[cite: 3] |
| **Requests** | HTTP client for consuming REST APIs[cite: 3] |
| **Official Joke API** | External public REST API endpoint[cite: 3] |
| **PyInstaller** | Executable compiler for Windows[cite: 3] |

---

## 📂 Repository Structure

```text
random-joke-generator/
│── app.py             # Main application script
│── tongue.ico         # Application icon asset
│── requirements.txt   # Python dependencies
│── screenshots/       # Application previews
│   └── application.png
└── README.md          # Project documentation

```

## 🚀 Getting Started
Prerequisites
OS: Windows 10 / 11

Python: 3.8 or higher

Network: Active internet connection

Installation & Execution
Clone the repository:

Bash
git clone [https://github.com/your-username/random-joke-generator.git](https://github.com/your-username/random-joke-generator.git)
cd random-joke-generator
Create and activate a virtual environment (optional but recommended):

Bash
python -m venv venv
venv\\Scripts\\activate
Install dependencies:

Bash
pip install requests
Run the application:

Bash
python app.py

## 📦 Building a Standalone Executable (.exe)
To bundle this script along with its custom icon into a single .exe file using PyInstaller:

Install PyInstaller:

Bash
pip install pyinstaller
Generate the executable:

Bash
pyinstaller --noconfirm --onedir --windowed --icon="tongue.ico" --add-data "tongue.ico;." app.py
Locate your compiled app in the dist/app/ directory!


##🔌 API Reference
Provider: Official Joke API

Endpoint: GET https://official-joke-api.appspot.com/random_joke

Response Format:

JSON
{
  "type": "general",
  "setup": "Why don't scientists trust atoms?",
  "punchline": "Because they make up everything!",
  "id": 59
}

## 📜 License
Distributed under the MIT License. See LICENSE for details.

## 👨‍💻 Author

**Nirjhar Dutta**

Senior SQL DBA | Python Enthusiast | Database Developer
