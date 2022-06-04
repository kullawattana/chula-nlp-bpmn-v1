# Install

## Install python 3.9.1
Ref : https://www.python.org/downloads/release/python-391/
Install for M1 and active : macOS 64-bit universal2 installer

## install environtment for setup library
$ python3 -m venv env
$ source env/bin/activate

## install flask to env
$ pip install Flask
$ pip install Flask-SQLAlchemy
$ pip install flask-restful
$ pip install python-dotenv
$ pip install gunicorn
$ pip install Flask-WTF
$ pip install WTForms
pip freeze > requirements.txt

# Remove requirement
- $ pip uninstall -r requirements.txt -y
- deactivate

# Validation WTForms
- $ pip install email_validator

## install spacy to env
- $ pip install -U pip setuptools wheel
- $ pip install -U spacy
- $ python -m spacy download en_core_web_sm
- python -m spacy download en
- $ pip install spacytextblob

# Create Procfile on VS Code and add to file
web: gunicorn app:app

# Format Code python
$ pip install autopep8
$ pip install pylint

# Check python version
- $ brew list | grep python

## Install Homebrew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

## Export Path
$ export PATH=/opt/homebrew/bin:$PATH

## Test Homebrew
- $ brew

## Install 
- $ brew tap heroku/brew && brew install heroku 

## login 
- $ heroku login

## Commit to git
- $ git init
- $ git add .
- $ heroku git:remote -a chula-nlp-bpmn 
### set git remote heroku to https://git.heroku.com/chula-nlp-bpmn.git
### URL : https://chula-nlp-bpmn.herokuapp.com/
- $ git commit -am "make it better"
- $ git push heroku master

## Every commit
- $ git add .
- $ git commit -am "make it better"
- $ git push heroku master

## View Log after deployment
- $ heroku logs --tail

## Change python 2 -> python 3
- $ alias python=python3

# DEPLOYING REST-API BASED FLASK APP ON HEROKU PART 1
Ref : https://medium.com/@ashiqgiga07/deploying-rest-api-based-flask-app-on-heroku-part-1-cb43a14c50c

# DEPLOYING REST-API BASED FLASK APP ON HEROKU PART 2
Ref : https://medium.com/@ashiqgiga07/deploying-rest-api-based-flask-app-on-heroku-part-2-54698cf7c96d

# DATABASE Example
Ref : https://github.com/ashiqks/Flask-Python/tree/master/flask-restful