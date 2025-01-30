# Flask MongoDB Docker CRUD API

A Flask REST API that performs CRUD operations with MongoDB, containerized using Docker.

## 🚀 Features
- REST API with Flask
- MongoDB integration
- Dockerized for easy deployment
- Structured and scalable code design

## 📂 Project Structure
```plaintext
├── controllers/          # Handles API request logic
│   ├── user_controller.py
│
├── db/                   # Database connection
│   ├── database.py
│
├── models/               # Database schema
│   ├── user_model.py
│
├── routes/               # API route definitions
│   ├── user_routes.py
│
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Multi-container setup with MongoDB
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## ⚙️ Installation & Setup

### **🔹 1. Clone the Repository**
```bash
git clone https://github.com/SathwikGit/flask-mongodb-docker-api.git
cd flask-mongodb-docker-api
```

### **🔹 2. Run with Docker**
Ensure **Docker & Docker Compose** are installed.
```bash
docker-compose up --build -d
```

### **🔹 3. Verify Running Containers**
```bash
docker ps
```
- Flask API → **http://127.0.0.1:9000**
- MongoDB → **localhost:27017**

### **🔹 4. API Endpoints**
#### **User CRUD Operations**
```plaintext
GET     /users          # Get all users
GET     /users/<id>     # Get user by ID
POST    /users          # Create a new user
PUT     /users/<id>     # Update user data
DELETE  /users/<id>     # Delete user
```

### **🔹 5. Test API using Postman**
- Open **Postman**
- Send requests to `http://127.0.0.1:9000`
- Use the API endpoints listed above

### **🔹 6. Stop Containers**
```bash
docker-compose down
```

### **🔹 7. Rebuild Containers**
```bash
docker-compose up --build -d
```

### **🔹 8. Check Logs**
```bash
docker logs flask_app
```


### **🔹 9. Remove All Docker Containers & Volumes**
```bash
docker-compose down -v
```

## 🛠️ Built With
- **Flask** - Python Web Framework
- **MongoDB** - NoSQL Database
- **Docker** - Containerization
- **Pymongo** - MongoDB Driver for Python

## 👤 Author
**SathwikGit**  
[GitHub Profile](https://github.com/SathwikGit)


