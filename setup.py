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


        print('Adding files from uploads to db')
        files_array = []
        for root, subdirs, files in os.walk('uploads'):
            for filename in fnmatch.filter(files, '*'):
                files_array.append(os.path.join(root, filename))

        for file in files_array:
            filename, file_extension = os.path.splitext(file)
            conn.execute('INSERT INTO FILE (NAME, TYPE) VALUES ("'+filename+'","'+file_extension+'");')

else:
    print('Database %s already exists' % config.DATABASE_NAME)

# TODO: Populate PARAMETER table with default values
# TODO: Install virtualenv and flask
# TODO: Install node and react

# TODO: Make all files. Look in all directories for Makefile. Make if there is one.
try:

    os.system('npm install')
    os.system('bower install')

    os.chdir(dirpath + '/rpi-rgb-led-matrix/include')
    os.system('wget http://www.sqlite.org/2017/sqlite-autoconf-3170000.tar.gz')
    os.system('tar xzf sqlite-autoconf-3170000.tar.gz')  # Unpack the source tree into "sqlite"
    os.system('mkdir bld')  # Build will occur in a sibling directory
    os.chdir(dirpath + '/rpi-rgb-led-matrix/include/bld')  # Change to the build directory
    os.system('pwd')
    os.system('../sqlite-autoconf-3170000/configure')  # Run the configure script
    os.system('make')  # Run the makefile.
    os.system('make sqlite3.c')
    os.system('rm -r ../sqlite-autoconf-*')


except Exception as e:
    print ('Failed to install required dependencies')
    print(e)
