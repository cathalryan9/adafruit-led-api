#!flask/bin/python
from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlite3
import requests
import json
import config
from werkzeug.utils import secure_filename
#add requests. Gets the request in json

import run_command

import os
abspath = os.path.abspath('app.py')
dirpath = os.path.dirname(abspath)
os.chdir(dirpath)

app = Flask(__name__)
#curl -H "Content-type: application/json" -X POST -F "filename=test.jpg" http://127.0.0.1:5000/file
#curl -X POST -F 'file=@"test.jpg"' http://127.0.0.1:5000/file

@app.route('/parameter', methods=['GET'])
def get_parameter():
    

    conn = sqlite3.connect(config.DATABASE_NAME)
    with conn:
        cur = conn.cursor()
        #conn.execute("INSERT INTO PARAMETER (ID,NAME,VALUE) VALUES (6,'-led-slowdown-gpio','1')")
        #conn.execute('CREATE TABLE PARAMETER (ID INT PRIMARY KEY,NAME TEXT NOT NULL, VALUE TEXT);')   
        brightness = cur.execute("SELECT * FROM PARAMETER")
        rows = cur.fetchall()
        parameters=[]
        for row in rows:
            value= {'id':row[0],'name':row[1],'value':row[2]}
            parameters.append(value)
                      
        conn.commit()
    
    return jsonify({'parameter':parameters})
   

@app.route('/parameter', methods=['PUT'])
def set_parameter():
    
    conn = sqlite3.connect(config.DATABASE_NAME)
    #print(str(parameter))
    
    value = request.json['value']
    name = request.json['name']
    
    cmd="UPDATE PARAMETER SET VALUE='" +str(value) + "' WHERE NAME='--" + name +"'"
    brightness = conn.execute(cmd)
    conn.commit()
    conn.close()
    
    return jsonify({'name':name,'value': value})


@app.route('/file', methods=['POST'])
def post_file():
    print(request.files)
    if 'file' not in request.files:
        print("file not in requuest")
        return redirect(request.url)
    file = request.files['file']
    print(file.filename)

    if file.filename:
        filename = secure_filename(file.filename)
        print("Try to save")
        os.path.join('../../')
        #file.save(os.path.join("bah"))
        file.save(os.path.join(config.UPLOAD_FOLDER, filename))
        print("saved")
        return redirect(request)
    else:
        return redirect(request.url)
@app.route('/run', methods=['POST'])
def run_command():
    run_command.run_command(request)

if __name__ == '__main__':
    app.run(debug=True)
