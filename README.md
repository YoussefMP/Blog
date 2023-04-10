<h1 align="center">
  <br>
    <img src="https://github.com/YoussefMP/Blog/blob/master/OrdinaryJoe/OJ_Blog/static/OJ_Blog/pictures/ReadMe_Banner.png" width="500"></a>
  <br>
</h1>

<p align="center">
<img src=https://img.shields.io/badge/Python-v3.7-blue>
<img src=https://img.shields.io/badge/Django-4.1.7-blue>
<img src=https://img.shields.io/badge/HTML-5-orange>
<img src=https://img.shields.io/badge/css-v2-blueviolet>
<img src=https://img.shields.io/badge/AWS-EC2-orange>
</p>

This is the code for my blog which you can find on Ordinaryjoe.org. If you want to take this code as a template to make you own blog, well... you can =).


## How to setup
1. First you will need to clone the project 
```bash
git clone https://github.com/YoussefMP/Blog.git
```

2. cd into the project's directory
```bash
cd Blog
```

3. Create a virtual environment (This step is optional, but it is good practice)
```bash
python -m venv /venv
```

4. Activate the virtual environment
```bash
venv\Scripts\activate.bat (on Windows)
```

5. cd into the Django project directory 
```bash
cd OrdinaryJoe
```

6. install all requirements in the requirement.txt file 
```bash
pip install -r requirements.txt
```

7. Now, you will need to run the following commands to setup the database and the static files
```bash
# packaging up your model changes into individual migration files
python manage.py makemigrations 

# propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema
python manage.py migrate 

# Collects the static files into STATIC_ROOT (Defined in settings.py)
python manage.py collectstatic
```
  7.1 If you run into the Server Error 500 error (it is most likely that your Database is missing some tables), run the following command
  ```bash
   python manage.py migrate --run-syncdb
  ```

8. At this point you should be able to start the server with the command
```bash
# This will run the server on the localhost 127.0.0.1 on the default port 8000 
python manage.py runserver
```
Open the browser type 127.0.0.1:8000 and you should be able to see the landing page. 

## Your first blog post
To add Posts you will have to first create and admin user then you will be prompted for credentials.
```bash
python3 manage.py createsuperuser
```
Then Visit 127.0.0.1:8000/admin, enter your credentials and from there it should be easy.

## Deployment
I am currently running this on an AWS EC2 instance. For a deployment tutorial you will have to wait a little bit =).
