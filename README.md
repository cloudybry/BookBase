# BookBase

BookBase is a modular Django API project designed for expressive branding, clean backend architecture, and recruiter-ready polish. It showcases RESTful logic, template integration, and scalable app structure—perfect for portfolio presentation and real-world deployment.


## Features

- Modular Django app structure (`generator`)
- REST API with Django REST Framework
- SQLite database for local testing
- Swagger/OpenAPI schema branding
- Template rendering (`home.html`)
- Unit test scaffold for API and models


##  Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite
- Swagger (via `drf-yasg` or similar)


##  Setup Instructions

```bash
# Clone the repo
git clone https://github.com/cloudybry/bookbase.git
cd bookbase

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Author

Bryan John Berzabal

BSIT Fresh Graduate | Philippine Christian University

Philippines

Aspiring Software Engineer

