# 🧘‍♀️ Fitness Booking App

A Django REST API project to browse and book fitness classes like Yoga, Zumba, and HIIT.

---


## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JeslinMariumAlex/Fitness-Studio-Booking-API.git
cd fitness-booking
```

### 2. Create and activate a virtual environment

python3 -m venv env
source env/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run database migrations

python manage.py migrate

### 5. Load sample data

python manage.py loaddata studio/fixtures.json

### 6. Run the development server

<pre> ```bash 
python manage.py migrate python manage.py runserver ``` </pre>



## 📬 API Endpoints

### Get all fitness classes

GET /api/classes/


### Book a fitness class

POST /api/book/

Body (JSON):
{
  "client_name": "Jeslin",
  "client_email": "jeslin@example.com",
  "fitness_class": 1
}


### View your bookings by email

GET /api/bookings/?email=jeslin@example.com


## 🧪 Sample cURL Request

curl -X POST http://127.0.0.1:8000/api/book/ \
  -H "Content-Type: application/json" \
  -d '{"client_name": "Jeslin", "client_email": "jeslin@example.com", "fitness_class": 1}'


## 📝 Sample Data

Seed data is located in:
studio/fixtures.json


## 📹 Loom Walkthrough 
🎥 Watch the video demo here: Loom Video


## 🛠 Tech Stack

- Python

- Django

- Django REST Framework

- SQLite (Default)


## ✅ Author

Jeslin Marium Alex








