# Posts API Project

### Project Summary
This is a simple django project where users can register, create posts
and like each others posts.

Technologies used:
- Python
- Django
- Django REST framework
- Postgres
- Swagger and Redoc for Documentation

The project has observed python's PEP8 rules and standards. 
To check code formatting:
```sh
$ flake8
```

View documentation on the following endpoints:

- For Swagger UI: http://127.0.0.1:8000/api/docs/
- For Redoc: http://127.0.0.1:8000/api/redoc/

## Setup
- Clone the repository
- Create a `.env` file in the project root.
- Copy the contents of `.env.dist` into your `.env` file.
- Create a postgres database 
- Update the contents of your `.env` to match your database credentials.


Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv venv
$ venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd PostsAPI
(venv)$ python manage.py runserver
```

### Authorization and Authentication
The project uses django rest framework basic authentication and token authentication.

To use token authentication, you can attatch the token to the Authorization header
as:

``Authorization: Token <token_value>``

Authorization example in swagger:

![alt text](/static/img/img.png)

### Project Structure.
The project has the following structure with each app having their API configuration

```tree
PostsAPI/                   <- project directory
├── core/                   <- Django root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── __init__.py
├── static/                
│   └── img/
├── manage.py
├── README.md
├── .env
├── .env.dist
├── .gitignore
├── requirements.txt
```

### Automated Testing
- Individual app tests are in the `tests` module under each app.

- Run tests using coverage:
```shell
$ coverage run --source='.' manage.py test
```
- To check test coverage:
```shell
$ coverage html
```
