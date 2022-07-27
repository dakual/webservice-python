```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install Flask
python3 -m pip freeze > requirements.txt
```
```
export FLASK_ENV=development
export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
```
```
flask run
flask run -h localhost -p 8080
```

```
dockebuild -t kurtay/webservice-python .
docker run -p 8080:8080 kurtay/webservice-python
```