# 🧘‍♀️ Fitness Studio Booking API

A simple Django REST API for a fictional fitness studio where users can:
- View available fitness classes
- Book a class
- View their bookings

---


## 🔧 Setup Instructions

1. **Clone the project**

```bash
git clone https://github.com/JeslinMariumAlex/Fitness-Studio-Booking-API.git
cd Fitness-Studio-Booking-API
```

 2. **Create and activate a virtual environment**

```bash
python3 -m venv env
source env/bin/activate
```

3. **Install the required packages**

```bash
pip install -r requirements.txt
```

4. **Run database migrations**

```bash
python3 manage.py migrate
```

5. **Load sample data**

```bash
python3 manage.py loaddata studio/fixtures.json
```

6. **Run the development server**

```bash 
python3 manage.py runserver 
```


## 🔌 API Endpoints

1. **Get all fitness classes**

Endpoint:
```bash 
GET /api/classes/
```
Sample cURL:
```bash 
curl http://127.0.0.1:8000/api/classes/
```


2.**Book a fitness class**

Endpoint:
```bash 
POST /api/book/
```
Request Body (JSON):
```bash 
{
  "class_id": 1,
  "client_name": "Jeslin",
  "client_email": "jeslin@example.com"
}

```
Sample cURL:
```bash 
curl -X POST http://127.0.0.1:8000/api/book/ \
  -H "Content-Type: application/json" \
  -d '{"class_id": 1, "client_name": "Jeslin", "client_email": "jeslin@example.com"}'
```

3.**View your bookings by email**

Endpoint:
```bash 
GET /api/bookings/?email=jeslin@example.com
```
Sample cURL:
```bash 
curl http://127.0.0.1:8000/api/bookings/?email=jeslin@example.com
```

## 📝 Sample Data

Seed data is located in:
```bash 
studio/fixtures.json
```

## 🛠 Tech Stack

- Python

- Django

- Django REST Framework

- SQLite (Default)


## 👩‍💻 Author

**Jeslin Marium Alex**

## 📹 Loom Video Walkthrough

🎥 Watch the video demo here: https://www.loom.com/share/bca0259b919c42a7acde9b563cb54723?sid=c1bd58a3-40ac-4642-adca-82f9c974673f





