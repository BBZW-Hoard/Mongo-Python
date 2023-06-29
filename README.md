# Mongo-Python
## Start programm
docker compose up --build

The website runs on http://localhost:9661/ if not configured different
## Start without Docker
### On Windows
python -m venv env-pymongo-fastapi-crud

. env-pymongo-fastapi-crud\Scripts\Activate.ps1

### Install Dependencies
pip install -r requirements.txt

python -m uvicorn main:app --reload
