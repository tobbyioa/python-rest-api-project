# CONTRIBUTING

## How to run the Dockerfile locally

## replace "/c/Users/path/Work/python_rest_api" with $(pwd) in mac

```
docker run -p  5000:5000 -w /app -v  "/c/Users/path/Work/python_rest_api:/app" flask-smorest-api  sh -c "flask run"   
```