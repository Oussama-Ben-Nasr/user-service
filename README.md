# Introduction
This project is a simple implemenation of user registration endpoints,
using fast-api and sqlalchemy as an ORM.

# routes
1. login
    An enpoint taking the login information

        + username
        + password

    returns

        -> valid registred user
        -> invalid creds

2. register
    An enpoint taking the login information

        + username
        + password

    returns

        -> registers a user with the given creds.

# commands to set up the dev environment.
pip install -r requirements.txt 
(not recomended as it can cause depandancies conflicts in future projects)

# commands to set up the dockerized dev environment.
docker build -t user-service .

docker run -d --name user-service-container -p 80:80 user-service
