# Paper
Refactor Project : https://github.com/kullawattana/refactor_thesis_v1_2022
Chula Thesis : http://cuir.car.chula.ac.th/simple-search?query=BPMN
Conference : https://acisinternational.org/conferences/csii-2022/

# Install
Git Authentication : https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to

## Install python 3.9.1
Ref : https://www.python.org/downloads/release/python-391/
Install for M1 and active : macOS 64-bit universal2 installer
Ref : https://www.python.org/downloads/release/python-370/
Recommend for NeuralCoref

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
- $ pip install spacy==2.1.0 (Recommend for NeuralCoref)
- $ python -m spacy download en_core_web_sm
- $ python -m spacy download en_core_web_sm-2.2.0
- python -m spacy download en
- $ pip install spacytextblob

# Check Info package
- $ python -m spacy info

# Install NeuralCoref package (support spacy 2.1.0, python 3.7)
- $ pip install neuralcoref
Ref : https://morioh.com/p/19b916530cb8

# Install NeuralCoref from Source (support spacy 2.1.0, python 3.7)
- $ python3 -m venv env
- $ source env/bin/activate
- $ git clone https://github.com/huggingface/neuralcoref.git
- $ cd neuralcoref
- $ pip install -r requirements.txt
- $ pip install -e .
Ref : https://stackoverflow.com/questions/61269954/attribute-error-using-neuralcoref-in-colab

# Uninstall NeuralCoref
- $ pip uninstall neuralcoref
- $ pip install neuralcoref --no-binary neuralcoref

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
- $ heroku git:remote -a chula-nlp-bpmn-v1 
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