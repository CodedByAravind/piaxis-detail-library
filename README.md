## Tech Stack

    Backend: Python (Flask)

    Database: PostgreSQL

    ORM: SQLAlchemy

    Frontend: HTML + Bootstrap (server-rendered)

    Version Control: Git & GitHub

## How to Setup
    
### 1. Clone Reposetory or extract ZIP

```bash
git clone https://github.com/CodedByAravind/piaxis-detail-library.git
cd piaxis-detail-library
```
### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install flask flask-sqlalchemy psycopg2-binary
```
### 4.Setup PostgreSQL

```bash
CREATE DATABASE piaxis_local;
```
    Update database credentials in app.py if required. (password)

### 5.Run the application

```bash
python app.py
```

### 6.Open in browser:

```bash
http://127.0.0.1:5000/
```
