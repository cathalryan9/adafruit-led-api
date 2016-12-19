#!flask/bin/python
from flask import Flask, render_template, jsonify, request, redirect, url_for, Response
import sqlite3
import json
import config
from werkzeug.utils import secure_filename
#add requests. Gets the request in json

import run_command as rc

import os
abspath = os.path.abspath('app.py')
dirpath = os.path.dirname(abspath)
os.chdir(dirpath)

app = Flask(__name__)
#curl -H "Content-type: application/json" -X POST -d {'file': 'runtext.ppm', 'duration': 10 }  http://127.0.0.1:5000/run

#curl -H "Content-type: application/json" -X POST -F "filename=test.jpg" http://127.0.0.1:5000/file
#curl -X POST -F 'file=@"test.jpg"' http://127.0.0.1:5000/file
@app.route('/')
def index():
    message="Welcome to the home page"
    return render_template('index.html', data=message)

@app.route('/parameter', methods=['GET'])
def get_parameter():
    

    conn = sqlite3.connect(config.DATABASE_NAME)
    with conn:
        cur = conn.cursor()

        cur.execute("SELECT * FROM PARAMETER")
        rows = cur.fetchall()
        parameters=[]
        for row in rows:
            value= {'id':row[0],'name':row[1],'value':row[2]}
            parameters.append(value)
                      
        conn.commit()
    print(parameters)

    #return jsonify({'parameter':parameters})
    return render_template('index.html', data=parameters, page='Parameter')
   

@app.route('/parameter', methods=['PUT'])
def set_parameter():
    
    conn = sqlite3.connect(config.DATABASE_NAME)
    
    value = request.json['value']
    name = request.json['name']
    
    cmd="UPDATE PARAMETER SET VALUE='" +str(value) + "' WHERE NAME='--" + name +"'"
    brightness = conn.execute(cmd)
    conn.commit()
    conn.close()
    
    return jsonify({'name':name,'value': value})


@app.route('/file', methods=['POST'])
def post_file():
    print(request.method)
    f = request.files['file']
    print(f)
    f.save(secure_filename(f.filename))
    #return 'file uploaded successfully'
    # if 'file' not in request.files:
    #     print("file not in request")
    #     return redirect(request.url)
    # file = request.files['file']
    # print(file.filename)
    #
    # if file.filename:
    #     filename = secure_filename(file.filename)
    #     print("Try to save")
    #     os.path.join('../../')
    #file.save(os.path.join(config.UPLOAD_FOLDER, 'bah'))
    #     print("saved")
    #     conn = sqlite3.connect(config.DATABASE_NAME)
    #
    #     name = request.json['name']
    #     # TODO don't add duplicates
    #     cmd = "INSERT INTO FILE (NAME) VALUES ('" + name + "')"
    #     conn.execute(cmd)
    #     conn.commit()
    #     conn.close()
    #     return redirect(request)
    # else:
    return 200

@app.route('/run', methods=['POST'])
def run_command():
    print(request.data)
    file = request.json['file']

    #Put in thread here to run command?
    print(file)
    if file.endswith('.ppm'):
        rc.run_command_ppm(request)
    elif file.endswith(('.gif','.jpg','.jpeg','.png')):
        rc.run_command_gif(request)

    return Response(json.dumps({'success':True}), 200, {'ContentType':'application/json'})

@app.route('/file', methods=['GET'])
def get_files():
    conn = sqlite3.connect(config.DATABASE_NAME)
    with conn:
        cur = conn.cursor()

        cur.execute("SELECT * FROM FILES")
        rows = cur.fetchall()
        files = []
        for row in rows:
            value = {'id': row[0], 'name': row[1]}
            files.append(value)
        conn.commit()

    if files == []:
        files="No Files"

    #return jsonify({'file': files})
    return render_template('index.html', data=files, page='File')


@app.route('/stop', methods=['POST'])
def stop_flask():

    #  TODO could be done better
    os.system('sudo reboot')

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1")