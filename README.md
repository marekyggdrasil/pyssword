# About

A simple program allowing you to practice password memory. It is not a password manager, passwords are securely stored as hashed strings hashed using `bcrypt` algorithm. If you like to rely on your memory and like to remember very long, random passwords full of strange characters, this program is for you. This script helps to build a good habit to practice your memory once every few days.

# Usage

All the data is stored locally in the file `db.p` placed in root directory of this project.

## Adding password

`python run.py --add myname@gmail.com`

You are going to be prompted for the password.

## Removing password

`python run.py --remove myname@gmail.com`

Will remove hashed password labeled with `myname@gmail.com`

## Practive

`python run.py --test`

Will begin a test session where you will be displayed with label and you will need to provide correct password. Example output:

```
1/2
myname@gmail.com
Password:
2/2
myname@yahoo.com
Password:
congratulations!
```

Passwords are not displayed in terminal and are not stored, only resulting hash strings are stored in the `db.py` file.
