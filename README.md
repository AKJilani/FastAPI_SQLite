# Professional FastAPI CRUD API with JWT Authentication (SQLite)

This is a **production-ready REST API** project built with **FastAPI** and **SQLite**, following industry-standard structure. The API supports:
- JWT-based Authentication
- Password Hashing (bcrypt)
- CRUD Operations on Items
- SQLite as lightweight backend DB

---

## 🚀 Project Structure

api_project/
│
├── app/
│ ├── main.py # Entry Point
│ ├── models.py # SQLAlchemy Models
│ ├── schemas.py # Pydantic Schemas
│ ├── database.py # Database Connection
│ ├── crud.py # DB Operations
│ ├── auth.py # Authentication Helpers
│ ├── routers/
│ │ ├── user.py # User Routes (Register/Login)
│ │ └── item.py # Item CRUD Routes
│ └── core/
│ └── security.py # JWT + Password Hashing
│
├── requirements.txt
├── .env # Secret Config (Optional)
├── .gitignore
└── README.md



---

## ⚙️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/AKJilani/FastAPI_SQLite.git
cd FastAPI_SQLite

# 2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate    # For Linux/Mac
# venv\Scripts\activate     # For Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the server
uvicorn app.main:app --reload

🔐 Authentication Flow
POST /api/v1/users/register : Create User

POST /api/v1/users/login : Obtain JWT Token (Bearer)

Use the token in Authorization headers:

makefile
Copy
Edit
Authorization: Bearer your_token_here
📑 API Endpoints
Endpoint	Method	Description
/api/v1/users/register	POST	Register User
/api/v1/users/login	POST	Login & get JWT
/api/v1/items/	POST	Create Item
/api/v1/items/	GET	Get All Items
/api/v1/items/{id}	GET	Get Item by ID
/api/v1/items/{id}	PUT	Update Item by ID
/api/v1/items/{id}	DELETE	Delete Item by ID

Swagger Docs available at:
📄 http://127.0.0.1:8000/docs

📦 Production Deployment
Use uvicorn with gunicorn or hypercorn

Store sensitive config in .env file

Use a reverse proxy (Nginx, Caddy)

Serve React frontend separately or as static files

📜 License
This project is open source and free to use under the MIT License.