# FastAPI Ledger API

## Project Description
This project is an accounting (ledger) system built using FastAPI. Users can create accounts, view their balances, and perform transactions.

## Getting Started

### Requirements
- Python 3.10+
- PostgreSQL
- FastAPI
- SQLAlchemy
- Uvicorn

   
1. *Create a Virtual Environment and Install Dependencies:*
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use 'venv\Scripts\activate'
   pip install -r requirements.txt
   ```
   
2. *Configure the Database:*
   Set up your PostgreSQL database by defining the `DATABASE_KEY` value in `constants/constants.py`.
   > **⚠️ <span style="color:red">Warning:</span>** Make sure to configure your database before running the application in <span style="color:red">"constants.py"</span> and <span style="color:red">"alembic.ini"</span> files.

3. *Start the Application:*
   ```bash
   uvicorn main:app --reload
   ```
   
## API Usage

### User Management
| Method | Endpoint | Description |
|--------|-------------|------------|
| GET | /users/ | Retrieves all users |
| GET | /users/{user_id} | Retrieves a specific user |
| POST | /users/ | Creates a new user |

### Ledger Management
| Method | Endpoint | Description |
|--------|-------------|------------|
| GET | /ledger/{owner_id} | Retrieves the user's current balance |
| POST | /ledger/ | Adds a new transaction |

#### Postman Collection can be found in Postman folder.