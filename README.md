# Secure-ML-API-JWT-Auth
This repo contains the demo on How to create a secure Machine Learning API with FastAPI and Docker enabled with JWT authentication.


Upcomming work 
- Add Dockerfile and docker-compose.yml
- Add Unit tests
- Need to add logging feature
1. https://machinelearningmastery.com/logging-in-python/
2. https://docs.python.org/3/library/logging.html



### Still building 
Build and Run the Docker Container
Use the following commands to run your API:

# Build the Docker image and run it

```
docker build -t secure-ml-api .
docker run -p 8000:8000 secure-ml-api
```
Now your machine leanring API will be available at http://localhost:8000.

Step: Test your API with Curl
For that, first, get the JWT by running the following command:

```curl -X POST http://localhost:8000/token```
Copy the access token and run the following command:

```curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer PASTE-TOKEN-HERE" \
  -d '{"data": [1.5, 2.3, 3.1, 0.7]}'
```
You should receive a prediction like:

```{"prediction": 0}```
You can try different inputs to test the API.