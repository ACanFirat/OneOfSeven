*FastAPI-Based Ledger and User Management System Documentation*

## *Introduction*
This project is a Ledger (Accounting Book) and User Management system developed using FastAPI. It utilizes PostgreSQL as the database and SQLAlchemy ORM for managing data.

---
## *1. Project Structure*
The project consists of the following modules:

- *main.py*: The entry point of the application.
- *router/*: Contains API endpoints.
  - ledger.py: Manages ledger operations.
  - user.py: Manages user operations.
- *models/*: Contains database models.
  - user.py: Defines user and ledger entry tables.
- *controllers/*: Contains business logic and database operations.
  - User.py: CRUD operations for users.
  - Ledger.py: Ledger operations.
- *db/*: Manages database connection and session.
  - database.py: Handles SQLAlchemy-based database connections.
- *models/schematics/*: Contains Pydantic models.
  - schemas.py: Provides input/output validation for APIs.
- *enums/*: Contains enumeration classes.
  - base_enum.py: Defines constant enum values for ledger operations.
- *constants/*: Contains constant values.
  - constants.py: Configuration values for ledger operations.

---
## *2. Key Components*

### *2.1 main.py*
- Initializes the FastAPI application.
- Creates database tables.
- Includes users and ledger routers.

### *2.2 router/ledger.py*
- /ledger/{owner_id}: Returns the current balance of a specific user.
- /ledger/ (POST): Creates a new ledger entry.

### *2.3 router/user.py*
- /users/: Returns all users.
- /users/{user_id}: Retrieves a user by ID.
- /users/ (POST): Creates a new user.

### *2.4 models/user.py*
- User: Model storing user information.
- LedgerEntry: Model storing ledger entries.

### *2.5 models/schematics/schemas.py*
- UserCreate: Input model for creating a new user.
- UserResponse: Output model for returning user information.
- LedgerEntryCreate: Input model for adding a ledger entry.

### *2.6 enums/base_enum.py*
- BaseLedgerOperation: Enum class for basic ledger operations.
- LedgerOperation: Enum class for content creation and access operations.
- combined_enums: Function for merging enums.

### *2.7 db/database.py*
- DATABASE_URL: Stores the database connection URL.
- engine: Creates the SQLAlchemy database engine.
- get_db(): Manages database session lifecycle.

### *2.8 controllers/ledger.py*
- get_ledger_balance(user_id, db): Retrieves the current balance of a user.
- create_ledger_entry(entry, db): Adds a new ledger entry.

### *2.9 controllers/user.py*
- get_user_by_id(db, user_id): Retrieves a user by ID.
- get_user_by_email(db, email): Retrieves a user by email.
- get_all_users(db, skip, limit): Returns all users.
- create_user(db, name, email): Creates a new user.

### *2.10 constants/constants.py*
- LEDGER_OPERATION_CONFIG: Configuration for ledger operations.
- DATABASE_KEY: Database connection string.

---
## *3. Running the API*

Run the following command in the terminal to start the FastAPI application:
sh
uvicorn main:app --reload
