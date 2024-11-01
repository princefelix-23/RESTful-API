# Flask REST API Demo

This project demonstrates a simple REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on student data, which can be tested locally and deployed to Azure App Service for cloud hosting.

## Features

- Retrieve all students
- Retrieve a specific student by ID
- Create a new student
- Update an existing student
- Delete a student

## Prerequisites

Before you can run or deploy this app, you need to have the following installed:

- Python 3.x
- pip (Python package manager)
- Flask (install with: pip install Flask)
- gunicorn (install with: pip install gunicorn)
- Azure CLI (optional, for deployment)

## Project Structure

- app.py: Main Flask application
- requirements.txt: List of Python dependencies
- test-api.http: Test the REST API using the REST Client extension in Visual Studio Code
- README.md: Documentation

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   `git clone https://github.com/princefelix-23/RESTful-API.git`

2. Navigate to the project directory:

   `cd RESTful-API`

3. Install the dependencies:

` pip install -r requirements.txt`

4. Run the application:

   `python app.py`

5. The API will be running at `http://127.0.0.1:8000`

6. Use test.http to test the REST API using the REST Client extension in Visual Studio Code.
