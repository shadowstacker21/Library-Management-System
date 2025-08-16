# 📚 Library Management System – Django REST API

A robust **Library Management System** built with **Django REST Framework**, designed to manage books, authors, borrowing, and returning functionality. It uses **JWT authentication** with **Djoser**, and includes interactive API documentation using **Swagger (drf_yasg)**.

---

## 🚀 Features

- 📖 **Book Management** – Add, update, delete, and list books.
- ✍️ **Author Management** – Manage book authors.
- 🧾 **Borrow & Return System**
  - Only one user can borrow a book at a time
  - A user can only borrow a specific book once
  - Prevents multiple returns
- 📂 **Image Uploads** – Upload and view book images
- 🔐 **Permissions**
  - Authenticated users can borrow/return books
  - Admin users can manage all resources
- 🧑‍💼 **JWT Authentication** using **Djoser**
- 📘 **API Docs** with **Swagger** and **ReDoc**
- 📊 **Search, Filter, Pagination** for books

---

## 🧱 Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** Djoser + JWT (SimpleJWT)
- **Documentation:** drf_yasg (Swagger / ReDoc)
- **Database:** SQLite (easy to swap with PostgreSQL/MySQL)
- **Python Version:** 3.10+

---

## 📁 Project Structure

library-management/
├── books/ # Book & author models, views, serializers
├── borrow/ # Borrowing logic
├── returns/ # Return logic
├── users/ # User management (Djoser)
├── media/ # Uploaded images
├── philm/ # Project settings
├── manage.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🔑 API Endpoints

### 📌 Authentication (Djoser + JWT)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/auth/jwt/create/`    | Login (obtain JWT) |
| POST   | `/auth/jwt/refresh/`   | Refresh JWT token |
| POST   | `/auth/users/`         | Register new user |
| GET    | `/auth/users/me/`      | Get current user |

---

### 📚 Books & Authors
| Method | Endpoint              | Description       |
|--------|-----------------------|-------------------|
| GET    | `/api/books/`         | List books        |
| POST   | `/api/books/`         | Add new book      |
| GET    | `/api/books/{id}/`    | Book detail       |
| PATCH  | `/api/books/{id}/`    | Update book       |
| DELETE | `/api/books/{id}/`    | Delete book       |
| GET    | `/api/authors/`       | List authors      |
| POST   | `/api/authors/`       | Add author        |

---

### 📥 Borrowing & 📤 Returning
| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| POST   | `/api/borrow/`         | Borrow a book            |
| GET    | `/api/borrow/`         | List borrows (admin)     |
| POST   | `/api/return/`         | Return a borrowed book   |
| GET    | `/api/return/`         | List returns (admin)     |

---

## 📸 Media

- Book images are uploaded via Django's `ImageField`.
- Accessible via `/media/` URL when in development.

---

## 📜 API Documentation

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/library-management.git
cd library-management
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run Migrations
bash
Copy code
python manage.py migrate
5️⃣ Create Superuser
bash
Copy code
python manage.py createsuperuser
6️⃣ Run Development Server
bash
Copy code
python manage.py runserver
🔐 Environment Variables
Create a .env file and add:

ini
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
You can use django-environ to load environment variables in settings.py.

📌 Requirements
See requirements.txt for the full dependency list, including:

Django

djangorestframework

djoser

drf_yasg

Pillow

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Your Name
📧 your.email@example.com
🔗 GitHub


