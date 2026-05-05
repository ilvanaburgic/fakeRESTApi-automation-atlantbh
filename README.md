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

Before starting automation, I tested the same endpoints manually in Postman and created separate test cases for each endpoint.
