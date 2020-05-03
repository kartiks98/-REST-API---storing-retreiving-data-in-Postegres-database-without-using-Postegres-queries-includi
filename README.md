# REST API - Storing & Retreiving data from Postegres database (with Authentication)
An API of my unique style that is far easy to understand than other APIs that can be used to interact with the database quite easily and efficiently with the use of Authentication for Signup & Login.

## What is this API exactly do?
1. Can create stores with their name & an id.
2. Can create items inside a store by their name & price.
3. Can create a new user & store it in database by signing up.
4. Can be used for the authentication of a registered user by login.
5. Can retreive all or a particular item of a store.
6. Can retreive all or a particular store present in the database with their items inside them.
7. Can Sign Up new users in dabase.
8. Can Login the registered users through Authentication.

## Libraries Used for creating API without handling Postegres queries(Using SQLAlchemy)
1. flask
2. flask_restful
3. flask_jwt
4. flask_sqlalchemy
5. psycopg2
