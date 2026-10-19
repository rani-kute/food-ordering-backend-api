# Food Ordering Backend API

A RESTful backend application built using Python, Django, and Django REST Framework to manage restaurants, food items, carts, and customer orders.

## Overview

This project provides APIs for restaurant information, food categories, menu items, carts, and orders. It also includes user registration and JWT-based authentication.

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- SQLite
- JWT Authentication
- Postman
- Git and GitHub

## Features

- User registration
- JWT token generation and refresh
- Restaurant APIs
- Food category APIs
- Food item APIs
- Cart and cart item APIs
- Order and order item APIs
- Order status updates
- Order status validation
- Django Admin integration

> **Project status:** This project is still under development. The CartItem database schema issue and FoodItem POST request validation issue are pending investigation. Cart/checkout flows and security checks also need further verification.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/restaurants/` | List restaurants |
| GET | `/api/categories/` | List food categories |
| GET | `/api/food-items/` | List food items |
| GET | `/api/food-items/<id>/` | Retrieve a food item |
| GET | `/api/carts/` | List carts |
| GET | `/api/cart-items/` | List cart items (database issue pending) |
| GET, POST | `/api/orders/` | List or create orders |
| GET, POST | `/api/order-items/` | List or create order items |
| POST | `/api/register/` | Register a user |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh an access token |
| PATCH | `/api/orders/<id>/` | Update order status |

Endpoint availability does not mean every operation is fully verified. Check the current code and test each endpoint before relying on it.

## Setup

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username:

```bash
git clone https://github.com/YOUR_USERNAME/food-ordering-backend-api.git
cd food-ordering-backend-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the packages used by the project:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Authentication

1. Register a user using `/api/register/`.
2. Send the username and password to `/api/token/` to obtain JWT tokens.
3. For protected endpoints, send the access token in the request header:

```text
Authorization: Bearer <access_token>
```

Never publish real passwords, JWT tokens, or Django secret keys.

## Testing

Postman has been used to test several GET and POST endpoints, JWT token generation, order creation, order item creation, and order status updates. Further testing is still required for cart operations, FoodItem creation, authorization, and the complete checkout flow.

## Planned Improvements

- Fix the CartItem database schema issue
- Fix FoodItem POST request data validation
- Verify cart quantity and checkout workflows
- Add automated API tests
- Verify user-level order permissions
- Add a `requirements.txt` file
- Deploy the application

## Author

Rani Kute  
Computer Science and Engineering, 2026  
Interested in Python Backend Development
