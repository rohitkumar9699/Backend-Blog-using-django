
# 📝 Blog API Project

This is a Django-based Blog API that supports user authentication with JWT tokens, CRUD operations on blog posts, and PostgreSQL as the backend database.

---

## 🚀 Features

- User registration and login
- JWT authentication (access + refresh tokens)
- Custom user model
- CRUD APIs for blogs
- Permissions using Django REST Framework
- PostgreSQL as the database
- Django admin for backend management

---

## 🛠 Tech Stack

- Python 3.11+
- Django 5.2
- Django REST Framework
- SimpleJWT (for authentication)
- PostgreSQL
- Docker (optional for deployment)

---

## 📁 Project Structure

```
blogs/
│
├── blogs/                 # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
│
├── users/                 # Custom user app
│   ├── models.py          # CustomUser model
│   ├── serializers.py     # User serializers
│   ├── views.py           # Register/Login API views
│   └── urls.py            # User-related routes
│
├── userblogs/             # Blog post logic
│   ├── models.py          # Blog model
│   ├── serializers.py     # Blog serializers
│   ├── views.py           # Blog API views
│   └── urls.py            # Blog routes
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL (or use SQLite for quick start)

Update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

---

## 🧪 API Endpoints

### 🔐 Authentication
- `POST /api/token/` – Get access and refresh tokens
- `POST /api/token/refresh/` – Refresh token
- `POST /register/` – Register new user

### 📝 Blog
- `GET /blogs/` – List blogs (requires auth)
- `POST /blogs/` – Create blog
- `GET /blogs/<id>/` – View a blog
- `PUT /blogs/<id>/` – Update blog
- `DELETE /blogs/<id>/` – Delete blog

---

## 🔐 Security Notes

- Ensure `DEBUG = False` in production.
- Keep `SECRET_KEY` secure and out of version control.
- Use HTTPS in production.

---

## ✍️ Author

**Rohit Kumar**  
Email: rk94523386@gmail.com  
GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is licensed under the MIT License.
