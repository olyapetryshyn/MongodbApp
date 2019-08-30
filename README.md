# Sign up / Sign in application with mongo db

## Description
This is the source code of the app, that allows you to create an account and then sign in with that data. 
Was created with no purpose at all, just to play around with pymongo.

## Install

### MongoDB
To run the app you need to install Mongodb Community edition. 
######
To do so, follow this link: https://docs.mongodb.com/manual/administration/install-community/

### MongoDB Compass
If you like GUI you can install MongoDB Compass, by following this link: https://docs.mongodb.com/compass/master/install/

### DB settings
In MongoDB Compass create connection with just two fields:
######
Hostname: localhost
######
Port: 27017
######
Create database, called users_db and collection, called users.

### Github repository
You have to have installed git on your computer.
Clone this github repository, by writing this command in terminal.
```
git clone https://github.com/olyapetryshyn/MongodbApp.git
```

### Install requirements
Install all needed packages, by writing this command in terminal.
```
pip install -r requirements.txt
```

## Run the server
Run Flask server by writing this command in terminal and then open your browser to see the website.
```
python login.py
```
