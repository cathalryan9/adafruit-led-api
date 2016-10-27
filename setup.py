#!flask/bin/python
import config
import sqlite3
import os
abspath = os.path.abspath('setup.py')
dirpath = os.path.dirname(abspath)
os.chdir(dirpath)
print(os.system('pwd'))


# Create database and tables
print('Checking if database has been created')
if not os.path.isfile(config.DATABASE_NAME):
    print('Creating database')
    conn = sqlite3.connect(config.DATABASE_NAME)
    with conn:
        conn.execute('CREATE TABLE PARAMETER (ID INT PRIMARY KEY,NAME TEXT NOT NULL, VALUE TEXT);')
else:
    print('Database %s already exists' % config.DATABASE_NAME)

# TODO: Make all files. Look in all directories for Makefile. Make if there is one.
try:
    print('Making files for rpi-rgb-led-matrix library')
    os.chdir('matrix')
    os.system('make')
    os.chdir('examples-api-use')
    os.system('make')

except Exception as e:
    print ('Failed to make files')
    print(e)