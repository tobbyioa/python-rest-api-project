# CONTRIBUTING

## How to run the Dockerfile locally

## replace "/c/Users/path/Work/python_rest_api" with $(pwd) in mac

```
docker run -p  5000:5000 -w /app -v  "/c/Users/path/Work/python_rest_api:/app" flask-smorest-api  sh -c "flask run"   
```

## Run background worker

```
docker run -w /app rest-api-email sh -c "rq worker -u rediss://red-cj64jaacn0vc738c1ncg:rbFclyFTukgDVC7sH95jhz5kSwroWEuD@oregon-redis.render.com:6379  emails"
```

## Run the background worker master

```
docker run -p  5000:80  rest-api-email
```