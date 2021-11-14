# E-SHOP REST API
---
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
# Prerequisites
This is a project written using Python, Django and Django Rest Framework
1. Clone the repository
```
https://github.com/luianqi/E-shop.git
```
2. Create the virtual enviroment
 ```
python3 -m venv venv
source venv/bin/activate
```
3. Install the requirements
```
pip install -r requirements.txt
```
4. Create a new PostgreSQL database

In your terminal:
```
psql postgres
CREATE DATABASE databasename
\c databasename
```
8. Create a new superuser
```
python manage.py createsuperuser
```
9. Run the server
```
python manage.py runserver
```
# Built With

> ### `Django` - The framework used
> ### `Django Rest Framework` - The toolkit used to build API

# Postman Collections

### [Collections](https://documenter.getpostman.com/view/17623351/UVC8DSEC#intro)

# Deployed to Heroku

### [Heroku](https://neoshoplace.herokuapp.com/)
