# introfastapi
⚡ FastAPI for the Python backend API.
💾 PostgreSQL as the SQL database.



This is a project to learn APIs
To execute this project :
```sh 
fastapi dev main.py
```




## The Database
Next let’s incorporate a sqlite database to store our question and response list items. The workhorse package we’ll use for database operations is sqlalchemy. sqlalchemy is powerful but complex.

First, let’s install sqlalchemy with 
```sh 
pip install sqlalchemy 
```
this is the database table that i wanted to create:

Questions Table:

- **id**: A unique identifier for each question. (Primary Key)
- **Content**: The text of the question.
- **Responses**: {
  - **id**: A unique identifier for each response. (Primary Key)
  - **response_text**: The text of the response.
  - **Is_correct**: A boolean indicating if the response is correct (`TRUE`) or incorrect (`FALSE`).}


## Problem and Solution

### Problem with SQLite

**Issue:** SQLite does not support storing dictionaries directly within a table.

**Solution:** Migration to PostgreSQL, which provides more advanced relational database features.

### Problem with PostgreSQL

**Issue:** PostgreSQL also does not support storing dictionaries directly within a table.

**Solution:** Creation of two related tables to represent the data structure effectively.




## Database Schema

### Tables

#### `Questions` Table

- **id**: A unique identifier for each question. (Primary Key)
- **Content**: The text of the question.




#### `Responses` Table

- **id**: A unique identifier for each response. (Primary Key)
- **question_id**: A foreign key linking each response to a question in the `Questions` table.
- **response_text**: The text of the response.
- **Is_correct**: A boolean indicating if the response is correct (`TRUE`) or incorrect (`FALSE`).

### SQL Code

To create the tables in PostgreSQL, use the following SQL commands:

```sql
-- Create the Questions table
CREATE TABLE Questions (
    id SERIAL PRIMARY KEY,
    content TEXT 
);

-- Create the Responses table
CREATE TABLE Responses (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES Questions(id) ON DELETE CASCADE,
    response TEXT ,
    is_correct BOOLEAN 
);
```

## CRUD (Create, Read, Update, Delete):
 operations for managing questions and their associated responses. It is built using FastAPI and interacts with a PostgreSQL database.
```sh 
# Initialize app
app = FastAPI() 
```
![CRUD](https://github.com/rim373/introfastapi/blob/main/pics/redoc.png)











