# Briefing API

API developed with Django REST Framework to manage categories, vendors, retailers and briefings.

## Description

This project aims to provide a system for managing briefings, allowing the creation, listing, updating and deletion of categories, vendors, retailers and briefings.

## Technologies Used 🚀

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL (or SQLite for testing)
- Docker and Docker Compose

## How to Run the Project

### **Clone the Repository**
```bash
git clone https://github.com/GustavooRez/amicci-backend-test.git
```

## Running with Docker 🐳

To run the project in a Dockerized environment, follow these steps:

**Build and start the containers**
```bash
docker-compose up --build -d
```

**Access the container**
```bash
docker exec -it briefing bash
```

**Apply the migrations**
```bash
python manage.py migrate
```

**The API will be available em**
```bash
http://localhost:8000/
```

## 📀 API Endpoints

### **Categories (`/api/categories/`)**
- `GET /api/categories/` → Lists all categories
- `GET /api/categories/{id}/` → Gets details of a category
- `POST /api/categories/` → Creates a new category
- `PUT /api/categories/{id}/` → Updates a category
- `DELETE /api/categories/{id}/` → Deletes a category

### **Vendors (`/api/vendors/`)**
- `GET /api/vendors/` → Lists all vendors
- `GET /api/vendors/{id}/` → Get details of a vendor
- `POST /api/vendors/` → Create a new vendor
- `PUT /api/vendors/{id}/` → Update a vendor
- `DELETE /api/vendors/{id}/` → Delete a vendor

### **Retailers (`/api/retailers/`)**
- `GET /api/retailers/` → List all retailers
- `GET /api/retailers/{id}/` → Get details of a retailer
- `POST /api/retailers/` → Create a new retailer
- `PUT /api/retailers/{id}/` → Update a retailer
- `DELETE /api/retailers/{id}/` → Delete a retailer

### **Briefings (`/api/briefings/`)**
- `GET /api/briefings/` → Lists all briefings
- `GET /api/briefings/{id}/` → Gets details of a briefing
- `POST /api/briefings/` → Creates a new briefing
- `PUT /api/briefings/{id}/` → Updates a briefing
- `DELETE /api/briefings/{id}/` → Deletes a briefing

---

## Running Tests 🤖

To run automated tests, run:
```bash
python manage.py test
```
This will validate the functionality of the endpoints and models.

## 📲 Contact

If you have any questions or suggestions, please contact me:

- ✉️ Email: gurezende27.gr@gmail.com
- 👉 LinkedIn: (https://www.linkedin.com/in/gustavo-rezende-dev/)
- 🌐 GitHub: (https://github.com/GustavooRez)

💡 **Developed with Django and Django REST Framework** 🚀