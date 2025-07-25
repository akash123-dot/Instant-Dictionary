# 📚 Instant Dictionary

Instant Dictionary is a **Flask-based web application** that allows users to search for word definitions instantly without relying on external APIs.  
It also provides a **REST API** so developers can integrate this dictionary service into their own applications.

---

## ✅ Features
- 🌐 **Web Interface** for searching English word definitions
- 🔐 **User Authentication** with JWT tokens
- 📦 **SQLite Database** for user storage
- 📂 **CSV-based Dictionary** using **Pandas**
- ⚡ **API Endpoints** for developers
- 🔒 **Password Hashing** using `werkzeug.security`

---

## ✅ Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite (via SQLAlchemy ORM)
- **Authentication:** JWT (PyJWT)
- **Data Handling:** Pandas
- **Frontend:** HTML + CSS (Jinja2 templates)

---

## ✅ Project Structure

Instant_dictionary/
│
├── app/
│   ├── api_logic/
│   │   └── api_logic.py
│   ├── auth/
│   │   └── auth.py
│   ├── dictionary/
│   │   └── dictionary_logic.py
│   ├── main/
│   │   ├── templates/
│   │   └── app.py
│   ├── utils/
│   │   └── jwt_helper.py
│   ├── models.py
│   ├── __init__.py
│   |── data.csv
|
├── instance/
├── requirements.txt
├── run.py
└── README.md
