# Airline Booking System API

## Project Overview

This is a simplified Django REST Framework-based API for an airline booking system. The application allows management of flights and passengers with full CRUD (Create, Read, Update, Delete) functionality.

## Project Structure

```
airline_booking_project/
│
├── manage.py
├── requirements.txt
│
├── airline_booking/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── flights/
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

## Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd airline_booking_project
```

### 2. Create and Activate Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`

## Project Architecture

### Models

#### Flight Model
Represents an airline flight with the following attributes:
- `flight_number`: Unique identifier for the flight
- `departure`: Date and time of departure
- `arrival`: Date and time of arrival
- `origin`: Departure airport
- `destination`: Arrival airport
- `capacity`: Total number of seats

#### Passenger Model
Represents a passenger with the following attributes:
- `first_name`: Passenger's first name
- `last_name`: Passenger's last name
- `email`: Unique email address
- `phone_number`: Contact number
- `flight`: Foreign key to associated Flight

### Serializers

#### FlightSerializer
- Converts Flight model instances to JSON
- Includes all Flight model fields
- Adds a custom `available_seats` method to calculate remaining seats
- Nested representation of Passengers on each Flight

#### PassengerSerializer
- Converts Passenger model instances to JSON
- Includes all Passenger model fields
- Allows association with a Flight

### ViewSets

#### FlightViewSet
- Provides CRUD operations for Flights
- Supports filtering by origin and destination
- Enables searching by flight number
- Allows ordering by departure and arrival times

#### PassengerViewSet
- Provides CRUD operations for Passengers
- Supports filtering by associated Flight and last name
- Enables searching by first name, last name, and email
- Allows ordering by last name

## API Endpoints

### Flights
- `GET /api/flights/`: List all flights
- `POST /api/flights/`: Create a new flight
- `GET /api/flights/{id}/`: Retrieve a specific flight
- `PUT/PATCH /api/flights/{id}/`: Update a flight
- `DELETE /api/flights/{id}/`: Delete a flight

### Passengers
- `GET /api/passengers/`: List all passengers
- `POST /api/passengers/`: Create a new passenger
- `GET /api/passengers/{id}/`: Retrieve a specific passenger
- `PUT/PATCH /api/passengers/{id}/`: Update a passenger
- `DELETE /api/passengers/{id}/`: Delete a passenger

## Filtering and Search

### Flights Filtering
- Filter by origin: `/api/flights/?origin=New York`
- Search flights: `/api/flights/?search=AA123`
- Order flights: `/api/flights/?ordering=departure`

### Passengers Filtering
- Filter by flight: `/api/passengers/?flight=1`
- Search passengers: `/api/passengers/?search=Doe`
- Order passengers: `/api/passengers/?ordering=last_name`

## Design Decisions

1. **Pagination**: 
   - Default page size of 10 items
   - Implemented using Django Rest Framework's PageNumberPagination

2. **Filtering**:
   - Used Django Filter Backend for flexible querying
   - Supports filtering, searching, and ordering on most fields

3. **Relationships**:
   - One-to-Many relationship between Flight and Passengers
   - Cascading delete for Passengers when a Flight is deleted

4. **Validation**:
   - Added `MinLengthValidator` for flight numbers
   - Unique constraints on flight number and passenger email

## Testing

### Running Tests
```bash
python manage.py test
```

## Potential Improvements
- Add authentication
- Implement more complex booking logic
- Add more advanced validation
- Create comprehensive test suite

## Troubleshooting
- Ensure all dependencies are installed
- Check database migrations
- Verify Python and Django versions

