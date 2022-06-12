# Papers
detail | reference
--- | ---
Refactor Project | https://github.com/kullawattana/refactor_thesis_v1_2022
Chula Thesis | http://cuir.car.chula.ac.th/simple-search?query=BPMN
Conference | https://acisinternational.org/conferences/csii-2022/

# Install Python
version | detail | reference
--- | --- | ---
3.9.1 | Install for M1 and active : macOS 64-bit universal2 installer | https://www.python.org/downloads/release/python-391/
3.7.0 | Recommend for NeuralCoref | https://www.python.org/downloads/release/python-370/

## Install environtment for setup library
detail | command 
--- | --- 
Create Environtment | $ python3 -m venv env
Activate Environtment | $ source env/bin/activate

# Install flask to env
detail | command 
--- | --- 
Flask | $ pip install Flask
SQL | $ pip install Flask-SQLAlchemy
RestFul | $ pip install flask-restful
Environtment | $ pip install python-dotenv
Heroku gunicorn | $ pip install gunicorn
Flask WTF | $ pip install Flask-WTF
WTForms | $ pip install WTForms
pip freeze | $ pip freeze > requirements.txt
Install Requirement | $ pip install -r requirements.txt 
Uninstall Requirement | $ pip uninstall -r requirements.txt -y
Deactive Environtment | $ deactivate

# Install spacy to env
detail | command 
--- | --- 
Setuptools Wheel | $ pip install -U pip setuptools wheel
Spacy | $ pip install -U spacy
Spacy 2.1.0 (Recommend for NeuralCoref) | $ pip install spacy==2.1.0
Spacy information package | $ python -m spacy info
Model | $ python -m spacy download en_core_web_sm
Download en | $ python -m spacy download en
Install NeuralCoref (support spacy 2.1.0, python 3.7) | $ pip install neuralcoref
Uninstall NeuralCoref | $ pip uninstall neuralcoref
Uninstall NeuralCoref without binary | $ pip install neuralcoref --no-binary neuralcoref

## Install NeuralCoref from Source (support spacy 2.1.0, python 3.7)
- $ python3 -m venv env
- $ source env/bin/activate
- $ git clone https://github.com/huggingface/neuralcoref.git
- $ cd neuralcoref
- $ pip install -r requirements.txt
- $ pip install -e .
- NeuralCoref Ref : https://morioh.com/p/19b916530cb8
- Colab Ref : https://stackoverflow.com/questions/61269954/attribute-error-using-neuralcoref-in-colab

# Create Procfile on VS Code and add to file
- web: gunicorn app:app

# Homebrew
detail | command
--- | ---
Install Homebrew | $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
Export Path | $ export PATH=/opt/homebrew/bin:$PATH
Test Homebrew | $ brew

# Heroku
## login and Commit to git
detail | command
--- | ---
Install | $ brew tap heroku/brew && brew install heroku 
Heroku Login | $ heroku login
Init | $ git init
Add | $ git add .
Remote | $ heroku git:remote -a chula-nlp-bpmn-v1 
Commit | $ git commit -am "make it better"
Push | $ git push heroku master
View Log | $ heroku logs --tail

topic | URL
--- | ---
Set Git remote heroku | https://git.heroku.com/chula-nlp-bpmn.git
Heroku URL | https://chula-nlp-bpmn.herokuapp.com/

# Git add
detail | command terminal
--- | ---
Add | $ git add .
Commit | $ git commit -am "make it better"
Push | $ git push heroku master

# Python
detail | command terminal
--- | ---
Change python 2 -> python 3 | $ alias python=python3
autopep8 | $ pip install autopep8
pylint | $ pip install pylint
Check python version | $ brew list | grep python

## Reference Deployment
topic | reference
--- | ---
DEPLOYING REST-API BASED FLASK APP ON HEROKU PART 1 | https://medium.com/@ashiqgiga07/deploying-rest-api-based-flask-app-on-heroku-part-1-cb43a14c50c
DEPLOYING REST-API BASED FLASK APP ON HEROKU PART 2 | https://medium.com/@ashiqgiga07/deploying-rest-api-based-flask-app-on-heroku-part-2-54698cf7c96d
DATABASE Example | https://github.com/ashiqks/Flask-Python/tree/master/flask-restful
Git Authentication | https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to