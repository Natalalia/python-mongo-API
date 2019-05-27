## Set up

Create virtual environment:

```
python3 -m venv userAPI
```

Activate virtual environment:

```
source userAPI/bin/activate
```

## Install dependencies

```
pip install Flask
```

```
pip install Flask-RESTful
```

```
pip install mongoengine
```

If requirements.txt already created just need to run `pip install -r requirements.txt` and all dependencies indicated in the file will be installed.

## Run the server

```
python3 user.py
```

## Run mongoDB

```
sudo service mongod start
```
