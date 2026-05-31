# API Automation - FakeRESTApi.Web V1

In this project, I worked on API test automation using the endpoints available in the FakeRESTApi.Web V1 Swagger documentation:

https://fakerestapi.azurewebsites.net/index.html

#### For automation, I used:

- Python  
- Pytest  
- Requests library  

#### The endpoints are organized into separate modules:

- Activities  
- Authors  
- Books  
- Cover Photos  
- Users  

Each endpoint file contains requests based on the endpoints provided in the Swagger documentation:

- GET  
- POST  
- PUT  
- DELETE  

For each endpoint, I validated:

- status codes  
- response body structure  
- returned data  
- Content-Type headers  
- response time  

Also, I implemented 4 negative tests to check how the API behaves when invalid requests are sent.

### Manual Testing

Before implementing automation, all endpoints were manually tested in Postman.

Additionally, separate test cases were created for each endpoint to validate expected API behavior.


## Installation

### Clone the repository:

git clone <https://github.com/ilvanaburgic/fakeRESTApi-automation-atlantbh.git>
cd api-automation1-atlantbh

### Create a virtual environment:

python -m venv .venv

### Activate the virtual environment:

#### macOS / Linux
source .venv/bin/activate

#### Windows
.venv\Scripts\activate

### Install dependencies:

pip install -r requirements.txt

### Running Tests

#### Run all tests:

pytest

#### Generate HTML report:

pytest --html=report.html --self-contained-html

#### Run a specific test file:

pytest tests/test_books.py

#### Run a specific test:

pytest tests/test_books.py::test_get_all_books
