# Insurance Policy Management API

This is a REST API developed with Django to manage insurance policies.

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Environment Configuration

1. Clone the repository
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

- Linux/Mac:

```bash
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Execute as migrações:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

## Running the Tests

To run the tests, use the command:

```bash
pytest
```

## API endpoints

- `POST /api/policies/` - Create a new policy
- `GET /api/policies/` - List all policies
- `GET /api/policies/{id}/` - Get details of a specific policy
- `PATCH/PUT /api/policies/{id}/` - Update an existing policy
- `DELETE /api/policies/{id}/` - Exclude a policy

## Project Structure

├── .gitignore  
├── LICENSE  
├── README.md  
├── insurance  
 ├── **init**.py  
 ├── asgi.py  
 ├── settings.py  
 ├── urls.py  
 └── wsgi.py  
├── manage.py  
├── policies  
 ├── **init**.py  
 ├── admin.py  
 ├── apps.py  
 ├── migrations  
 │ ├── 0001_initial.py  
 │ └── **init**.py  
 ├── models.py  
 ├── serializers.py  
 ├── tests.py  
 ├── urls.py  
 └── views.py  
├── pytest.ini  
└── requirements.txt
