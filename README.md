# Mongo-Python
## Installation
### On Windows
python -m venv env-pymongo-fastapi-crud
. env-pymongo-fastapi-crud\Scripts\Activate.ps1

### Install Dependencies
python -m pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv

## Start programm
python -m uvicorn main:app --reload
### Check entries on Database
python DBTerminal.py
