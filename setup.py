#!flask/bin/python
import config
import sqlite3
import os
import fnmatch
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
        conn.execute('CREATE TABLE FILE (ID INT PRIMARY KEY,NAME TEXT NOT NULL, TYPE TEXT NOT NULL);')

        print('Populating database')
        conn.execute('INSERT INTO PARAMETER (NAME, VALUE) VALUES ("--led-brightness", "30");')
        conn.execute('INSERT INTO PARAMETER (NAME, VALUE) VALUES ("--led-gpio-mapping", "adafruit-hat");')
        conn.execute('INSERT INTO PARAMETER (NAME, VALUE) VALUES ("-t", "10");')
        conn.execute('INSERT INTO PARAMETER (NAME, VALUE) VALUES ("-m", "100");')
        conn.execute('INSERT INTO PARAMETER (NAME, VALUE) VALUES ("-R", "0");')

        #Get list of files in uploads
        files = []
        for root, subdirs, files in os.walk('uploads'):
            for filename in fnmatch.filter(files, '*'):
                files.append(os.path.join(root, filename))
        for file in files:
            filename, file_extension = os.path.splitext(file)
            print(filename)
            print(file_extension)
            conn.execute('INSERT INTO FILE (NAME, TYPE) VALUES ("'+filename+'","'+file_extension+'");')

else:
    print('Database %s already exists' % config.DATABASE_NAME)

# TODO: Populate PARAMETER table with default values
# TODO: Install virtualenv and flask
# TODO: Install node and react

# TODO: Make all files. Look in all directories for Makefile. Make if there is one.
try:
    print('Making files for rpi-rgb-led-matrix library')
    os.system('sudo apt-get install python-virtualenv')
    os.system('virtualenv flask')
    os.system('. flask/bin/activate')
    os.system('sudo pip install Flask')
    os.system('sudo pip install Pillow')
    os.system('sudo npm install -g bower')
    os.system('bower init')
    os.system('npm init')
    os.system('npm install --save-dev bower')
    os.system('bower install')
    os.chdir('rpi-rgb-led-matrix')
    os.system('make')
    os.chdir('python')
    os.system('sudo apt-get update && sudo apt-get install python2.7-dev python-pillow -y')
    os.system('make build-python')
    os.system('sudo make install-python')
    os.chdir('../examples-api-use')
    os.system('make')
    os.chdir('../utils')
    os.system('sudo apt-get install libgraphicsmagick++-dev libwebp-dev -y')
    os.system('make led-image-viewer')



except Exception as e:
    print ('Failed to make files')
    print(e)
