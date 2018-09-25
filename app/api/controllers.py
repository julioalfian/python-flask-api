from flask import Blueprint, render_template, request, Response
from app.pegawai.db import db as db_pegawai
from app.divisi.db import db as db_divisi
from app.task.db import db as db_task
from app.task_pegawai.db import db as db_task_pegawai
import json

api = Blueprint('api',__name__, url_prefix='/api')

# pegawai-------------
@api.route('/pegawai',methods=['GET','POST'])
def get_all_pegawai():
    if request.method == "GET":
        return Response(json.dumps(db_pegawai.get_all_pegawai()), mimetype='text/json')
    elif request.method == "POST":
        content = request.get_json(silent=True)
        return Response(json.dumps(db_pegawai.add_pegawai(content)), mimetype='text/json')
    
@api.route('/pegawai/delete/<id>',methods=['GET','POST'])
def delete_pegawai(id):
    return Response(json.dumps(db_pegawai.delete_pegawai(id)), mimetype='text/json')

@api.route('/pegawai/update',methods=['GET','POST'])
def update_pegawai():
    content = request.get_json(silent=True)
    return Response(json.dumps(db_pegawai.update_pegawai(content)), mimetype='text/json')

# divisi-----------------
@api.route('/divisi',methods=['GET','POST'])
def get_all_divisi():
    if request.method == "GET":
        return Response(json.dumps(db_divisi.get_all_divisi()), mimetype='text/json')
    elif request.method == "POST":
        content = request.get_json(silent=True)
        return Response(json.dumps(db_divisi.add_divisi(content)), mimetype='text/json')

@api.route('/divisi/delete/<id>',methods=['GET','POST'])
def delete_divisi(id):
    return Response(json.dumps(db_divisi.delete_divisi(id)), mimetype='text/json')

@api.route('/divisi/update',methods=['GET','POST'])
def update_divisi():
    content = request.get_json(silent=True)
    return Response(json.dumps(db_divisi.update_divisi(content)), mimetype='text/json')

# task-----------------
@api.route('/task',methods=['GET','POST'])
def get_all_task():
    if request.method == "GET":
        return Response(json.dumps(db_task.get_all_task()), mimetype='text/json')
    elif request.method == "POST":
        content = request.get_json(silent=True)
        return Response(json.dumps(db_task.add_task(content)), mimetype='text/json')

@api.route('/task/delete/<id>',methods=['GET','POST'])
def delete_task(id):
    return Response(json.dumps(db_task.delete_task(id)), mimetype='text/json')

@api.route('/task/update',methods=['GET','POST'])
def update_task():
    content = request.get_json(silent=True)
    return Response(json.dumps(db_task.update_task(content)), mimetype='text/json')

# task_pegawai-----------------
@api.route('/task_pegawai',methods=['GET','POST'])
def get_all_task_pegawai():
    if request.method == "GET":
        return Response(json.dumps(db_task_pegawai.get_all_task_pegawai()), mimetype='text/json')
    elif request.method == "POST":
        content = request.get_json(silent=True)
        return Response(json.dumps(db_task_pegawai.add_task_pegawai(content)), mimetype='text/json')

@api.route('/task_pegawai/delete/<id>',methods=['GET','POST'])
def delete_task_pegawai(id):
    return Response(json.dumps(db_task_pegawai.delete_task_pegawai(id)), mimetype='text/json')

@api.route('/task_pegawai/update',methods=['GET','POST'])
def update_task_pegawai():
    content = request.get_json(silent=True)
    return Response(json.dumps(db_task_pegawai.update_task_pegawai(content)), mimetype='text/json')
