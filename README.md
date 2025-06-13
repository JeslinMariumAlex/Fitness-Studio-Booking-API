# Fitness Booking App

This is a Django app to book fitness classes like yoga, zumba, HIIT, etc.

## How to set it up

1. Install requirements:
   pip install -r requirements.txt

2. Run migrations:
   python manage.py migrate

3. Load sample data:
   python manage.py loaddata studio/fixtures.json

4. Run the project:
   python manage.py runserver

## API Endpoints

- GET /api/classes/ – Get all classes
- POST /api/book/ – Book a class
- GET /api/bookings/?email=your@email.com – See your bookings
