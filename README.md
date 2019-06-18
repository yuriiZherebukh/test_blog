# test_blog

To start work with 'Test Blog' project:
- Clone repository from git:
```
git clone https://github.com/yuriiZherebukh/test_blog
```

- Install Python 3.6.8 and higher on your OS

- Install PostgreSQL and other required packages for Python 3 intergration:

```
sudo apt-get install install python-pip python-dev libpq-dev postgresql postgresql-contrib
```
- Create Database and Database user:
```
sudo -su postres psql
\password postgres
```
Enter password for 'postgres' user. Then:
```
CREATE DATABASE testBlog;
GRANT ALL PRIVILEGES ON DATABASE testBlog TO postgres;
\q
exit
```
- Install Requirements for 'Test Blog' project

Install _virtualenv_
```
sudo pip3 install virtualenv 
```
Navigate to _test_blog_ directory and create virtualenv

```
cd test_blog
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```
- Create _local_settings.py_ module for configurations for PostgreSQL and also store SECRET_KEY for JWT:

```
cd /test_blog/test_blog/
touch local_settings.py
```

Alter this code:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testBlog',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
SECRET_KEY = "your_secret"
```
- Make migrations:
```python
python3 manage.py migrate
```

- Install and configure _nginx_ server:
```
sudo apt-get install nginx

sudo /etc/init.d/nginx start 

sudo ln -s ~/path/to/test_blog/test_blog/test_blog_nginx.conf /etc/nginx/sites-enabled/
```
- Change root paths to _test_blog_nginx.conf_ regarding _test_blog_ project path

Collect static files on the project nad restart _nginx_ server:
```python
python3 manage.py collectstatic
```
```
sudo /etc/init.d/nginx restart
```
- Add your local user to _www-data_ group to start the project successfully:
```
usermod -a -G www-data exampleusername
``` 

- Start nginx + uWSGI:
```python
uwsgi --ini test_blog_uwsgi.ini
```
Home page can be accessed with `http://127.0.0.1:8000` URL
