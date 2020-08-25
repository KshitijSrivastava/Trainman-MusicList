# User Music List API

## Backend Python Assignment | Trainman



For a movie rating app, create a django rest api using django rest framework. 
The app needs to have the capability to 
- list movies, 
- logged in users can save movies to a watchlist or mark them watched.  
- logged in users can view list of movies in their watchlist or watched list.

Build the corresponding rest APIs.

To populate the movies in your database, create a scraper to scrape IMDb’s top list (https://www.imdb.com/chart/top/). The scrapper should follow each movie’s url and extract details from the movie’s page. The details you want to save are up to you. The more the better.
This scraper should ideally be triggered by an endpoint in your django api and accept any similar url e.g. https://www.imdb.com/india/top-rated-indian-movies.
Already existing movies should be only updated. Not replaced/duplicated.

Few points to keep in mind -
- use django-rest-framework
- use pipenv/virtualenv etc to make the project easy to setup for anyone, add a setup file
- use sqlite as database for portability
- users should be able to sign up and login, use token authentication
- take care of permissions - users cannot delete a movie, view other users’ watched list etc



# Documentation

# Setup

Make a python virtual environment
run `pip install -r requirements.txt`
run `python manage.py migrate`
run `python manage.py runserver`



# Creates a User

**URL** : `/user-signup`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data example** All fields must be sent.

```json
{
    "username": "kshitij",
    "password": "12345678",
    "email": "abcd@gmail.com"
}
```

## Success Response

**Code** : `201 Created`

**Content examples**

```json
{
    "id": 2,
    "username": "kshitij127",
    "email": "abcd@gmail.com",
    "password": "pbkdf2_sha256$216000$yxlX8cUr9SCj$DCxLEaXyifErayE3rMEIwsYKvNOIXet5Lm/CAcf3kuY="
}
```

# Get a token

**URL** : `/api-token-auth`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data example** All fields must be sent.

```json
{
    "username": "kshitij",
    "password": "12345678"
}
```

## Success Response

**Code** : `201 Created`

**Content examples**

```json
{
    "username": "kshitij127",
    "token": "pbkdf2_sha256$216000$yxlX8cUr9SCj$DCxLEaXyifErayE3rMEIwsYKvNOIXet5Lm/CAcf3kuY="
}
```

# Get all movies

**URL for getting info from slot** : `/movies`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**


```json
[
    {
        "name": "The Shawshank Redemption (1994) ",
        "imdb_rating": 9.3,
        "summary": "\n                    Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.\n            "
    },
    {
        "name": "The Godfather (1972) ",
        "imdb_rating": 9.2,
        "summary": "\n                    The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.\n            "
    },
    {
        "name": "The Godfather: Part II (1974) ",
        "imdb_rating": 9.0,
        "summary": "\n                    The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.\n            "
    }
]
```

# Get movie List of a user

**URL for getting info from slot** : `/user-movie-list`

**Method** : `GET`

**Auth required** : Token Token-key

**Permissions required** : Yes

## Success Response

**Code** : `200 OK`

**Content examples**


```json
[
    {
        "name": "The Shawshank Redemption (1994) ",
        "watched": "True"

    },
    {
        "name": "The Godfather (1972) ",
        "watched": "False"

    }
]
```

# Logged in users can save movies to a watchlist or mark them watched

**URL** : `/watchlist-add`

**Method** : `POST`

**Auth required** : Token Token-key

**Permissions required** : Yes


```json
{
    "data":[
        { "movie": "The Shawshank Redemption (1994) ", "watched": false },
        { "movie": "The Godfather (1972) ", "watched": true }
    ]
}
```

## Success Response

**Code** : `200`

**Content examples**

```json
{
    "Added/Updated the list"
}
```