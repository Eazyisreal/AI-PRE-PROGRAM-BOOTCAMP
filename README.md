# FastAPI Full Name API

This FastAPI application takes the first and last name of a user as input and returns the user's full name.

## Prerequisites

- Python 3.7 or higher installed on your machine.
- `pip` package manager installed.

## Installation

1. Clone or download this repository to your local machine.

    ```bash
    git clone https://github.com/Eazyisreal/AI-PRE-PROGRAM-BOOTCAMP
    ```

2. Navigate to the project branch.

    ```bash
    git checkout task-2
    ```

3. Install the required Python dependencies.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application.

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API in your web browser or using an API client like Postman.

    - Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the interactive API documentation (Swagger UI). Here, you can test the API endpoints and see the documentation.
    - Alternatively, you can make HTTP requests to the API endpoints using tools like `curl` or Postman.

### Example:

- To get the full name of a user, make a GET request to the `/fullname/{first_name}/{last_name}` endpoint with the first name and last name as path parameters.

    ```bash
    curl -X GET "http://localhost:8000/fullname/John/Doe"
    ```

    Response:

    ```json
    {
      "full_name": "John Doe"
    }
    ```

