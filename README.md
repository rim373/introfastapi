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

ID: A unique identifier for each question.
Content: The text of the question.
Responses dictionnary :{ID: A unique identifier for each response,
                        Response : The text of the response,
                        Is Correct: A boolean indicating if the response is correct}
PROBLEM: SQLite does not support storing dictionaries directly within a table
SOLUTION :Migration to PostgrSQL
PROBLEM:PostgrSQL also does not support storing dictionaries directly within a table
SOLUTION:Creation of two tables

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```



