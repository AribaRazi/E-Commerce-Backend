## E-Commerce Backend API

A RESTful backend service for a basic e-commerce platform built using **Flask** and **MySQL**.  
The project follows a clean layered architecture separating routing, business logic, and database access.

---

## Author

**Ariba Razi**  
Backend Developer (Python, Flask, MySQL)

---

## Tech Stack

- Python
- Flask
- MySQL
- mysql-connector-python

---

## Project Structure

```

ecom_backend/
├── models/        # Database queries
├── services/      # Business logic
├── routes/        # API routes (Blueprints)
├── app.py         # Application entry point
├── db.py          # Database connection
├── schema.sql     # Database schema
├── config.example.py
└── README.md

````

---

## Architecture

- **Models:** Handle raw SQL queries and database interaction  
- **Services:** Contain validations and business rules  
- **Routes:** Expose REST APIs using Flask Blueprints  
- **schema.sql:** Allows any user to recreate the same database structure  

---

## Database

MySQL is used as the relational database.  
The schema includes the following tables:

- `users`
- `products`
- `orders`
- `order_items`
- `payments`

All table definitions and relationships are available in `schema.sql`.

---

## API Endpoints

### Users
- `POST /users` – Register a user  
- `GET /users/<id>` – Get user by ID  
- `GET /users/email/<email>` – Get user by email  

### Orders
- `POST /orders` – Place an order  

### Payments
- `POST /payments` – Initiate payment  
- `GET /payments/order/<order_id>` – Get payment by order  
- `PATCH /payments/<payment_id>` – Update payment status  

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone <repository_url>
cd ecom_backend
````

### 2. Create Database

```sql
CREATE DATABASE ecommerce;
USE ecommerce;
SOURCE schema.sql;
```

### 3. Configure Database

Create `config.py` using `config.example.py`:

```python
DB_config = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password",
    "database": "ecommerce"
}
```

> `config.py` should not be committed to GitHub.

---

### 4. Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

### 5. Run Server

```bash
python app.py
```

---

## Sample API Testing (curl)

### Create User

```bash
curl -X POST http://127.0.0.1:5000/users ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"John\",\"email\":\"john@example.com\",\"password\":\"123456\"}"
```

### Place Order

```bash
curl -X POST http://127.0.0.1:5000/orders ^
-H "Content-Type: application/json" ^
-d "{\"user_id\":1,\"items\":[{\"product_id\":1,\"quantity\":2,\"price\":500}]}"
```

### Initiate Payment

```bash
curl -X POST http://127.0.0.1:5000/payments ^
-H "Content-Type: application/json" ^
-d "{\"order_id\":1,\"payment_method\":\"CARD\"}"
```

---

## Features

* RESTful API design
* Layered backend architecture
* MySQL relational schema
* Order and payment workflow
* Input validation and error handling
* Secure database configuration

---


```
```
