# FastAPI User Management REST API

A RESTful **User Management API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

The application provides user registration, login, authentication, pagination, and CRUD operations while following a modular FastAPI project structure.

## Features

- User registration
- User login
- JWT-based authentication
- Secure password hashing with bcrypt
- PostgreSQL database integration
- SQLAlchemy ORM
- User CRUD operations
- Protected API endpoints
- Pagination using `skip` and `limit`
- Pydantic request and response validation
- Automatic Swagger/OpenAPI documentation
- Environment-based configuration

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database interaction |
| Pydantic | Request and response validation |
| JWT | Authentication tokens |
| Passlib + bcrypt | Password hashing |
| python-jose | JWT encoding and decoding |
| python-dotenv | Environment variable management |

## Project Structure

```text
fastapi-user-api/
│
├── app/
│   ├── routes/
│   │   └── users.py
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── auth.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

### Main Components

- `main.py` — FastAPI application entry point and router registration
- `database.py` — PostgreSQL connection and SQLAlchemy session configuration
- `models.py` — SQLAlchemy database models
- `schemas.py` — Pydantic request and response models
- `crud.py` — Database CRUD operations
- `auth.py` — Password hashing, JWT creation, validation, and authentication
- `routes/users.py` — User registration, login, and CRUD API endpoints

## API Endpoints

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| `GET` | `/` | API health/root endpoint | No |
| `POST` | `/users/register` | Register a new user | No |
| `POST` | `/users/login` | Login and generate JWT access token | No |
| `GET` | `/users/` | Get users with pagination | Yes |
| `GET` | `/users/{user_id}` | Get a user by ID | Yes |
| `PUT` | `/users/{user_id}` | Update a user | Yes |
| `DELETE` | `/users/{user_id}` | Delete a user | Yes |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/siri-chandanak/fastapi-user-api.git
cd fastapi-user-api
```

### 2. Create a Virtual Environment

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/fastapi_users

SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace the PostgreSQL username, password, database name, and JWT secret with values appropriate for your environment.

> Do not commit the `.env` file or real credentials to GitHub.

## PostgreSQL Setup

Create a PostgreSQL database for the application.

Example:

```sql
CREATE DATABASE fastapi_users;
```

Then configure your `.env`:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/fastapi_users
```

The application uses SQLAlchemy to create the required database tables when the API starts.

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

Test the root endpoint:

```text
http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "FastAPI User API is running"
}
```

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can also be used to register users, log in, authorize requests with a JWT token, and test protected endpoints.

## Authentication Flow

The application uses JWT bearer authentication.

### Step 1 — Register

Send a request to:

```http
POST /users/register
```

Example request:

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "securepassword"
}
```

The password is hashed before being stored in the database.

### Step 2 — Login

Send credentials to:

```http
POST /users/login
```

The login endpoint uses OAuth2 form data.

Example:

```text
username=john
password=securepassword
```

A successful login returns:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Step 3 — Access Protected Endpoints

Include the generated JWT token:

```http
Authorization: Bearer <access_token>
```

For example:

```http
GET /users/
Authorization: Bearer <access_token>
```

## User Model

A user contains the following fields:

| Field | Description |
|---|---|
| `id` | Unique user ID |
| `username` | Unique username |
| `email` | Unique email address |
| `hashed_password` | Securely hashed password |
| `is_active` | Indicates whether the account is active |

Passwords are never returned through the API response model.

## Pagination

The user listing endpoint supports pagination.

Example:

```http
GET /users/?skip=0&limit=10
```

Parameters:

- `skip` — Number of records to skip
- `limit` — Maximum number of records to return

Example:

```http
GET /users/?skip=10&limit=5
```

This skips the first 10 users and returns up to 5 users.

## Update User

Authenticated users can send:

```http
PUT /users/{user_id}
```

Example request:

```json
{
  "username": "john_updated",
  "email": "john.updated@example.com",
  "is_active": true
}
```

All update fields are optional, allowing partial updates.

## Delete User

To delete a user:

```http
DELETE /users/{user_id}
```

A successful deletion returns:

```json
{
  "message": "User deleted successfully"
}
```

## Security

The project includes several basic API security practices:

- Passwords are hashed using bcrypt
- Plain-text passwords are not stored
- JWT tokens are used for authentication
- Protected endpoints require bearer authentication
- Secrets and database credentials are loaded through environment variables
- Password hashes are excluded from API responses

## Current Limitations

This project is currently a lightweight user-management API intended for learning and backend development practice.

Possible production improvements include:

- Role-based access control (RBAC)
- Restricting users from modifying other users
- Refresh tokens
- Token revocation/logout
- Password reset functionality
- Email verification
- Stronger password policies
- Database migrations with Alembic
- Automated testing with pytest
- Docker support
- CI/CD pipeline
- Rate limiting
- Structured logging
- Production deployment configuration

## Example Development Workflow

```bash
# Clone repository
git clone https://github.com/siri-chandanak/fastapi-user-api.git

cd fastapi-user-api

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure .env
# Start API
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Learning Objectives

This project demonstrates several important backend development concepts:

- REST API development with FastAPI
- HTTP methods and status handling
- Request and response validation
- PostgreSQL database connectivity
- ORM-based database operations
- CRUD architecture
- Dependency injection
- Authentication and authorization
- JWT lifecycle
