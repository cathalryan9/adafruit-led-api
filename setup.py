#!flask/bin/python
import config
import sqlite3
import os
abspath = os.path.abspath('setup.py')
dirpath = os.path.dirname(abspath)
os.chdir(dirpath)



# Create database and tables
print('Checking if database has been created')
if not os.path.isfile(config.DATABASE_NAME):
    print('Creating database')
    conn = sqlite3.connect(config.DATABASE_NAME)
    with conn:
        conn.execute('CREATE TABLE PARAMETER (ID INT PRIMARY KEY,NAME TEXT NOT NULL, VALUE TEXT);')
else:
    print('Database %s already exists' % config.DATABASE_NAME)
