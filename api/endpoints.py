from app import app
from flask import request, send_from_directory
from helpers.mongoConnection import *
from bson import json_util
import os
from random import choice


@app.route("/")
def hello_world():
    return {"hello": "World!"}






'''

MANDAR INFO A LA API:

1)

@app.route("/hello")
def salute():
    name = request.args.get("name")
    lastname = request.args.get("lastname")
    return f"Hello, {name} {lastname}"

2)
@app.route("/hello/<name>")
def salute(name):
    name = request.args.get("name")
    return f"Hello, {name}"





@app.route("/help")
def help():
    return {"welcome":"Welcome to my API"}


@app.route("/salute")
def salute():
    name = request.args.get("name")
    return f"Hello, {name}!!!"


##Llamada a get_company de mongo
@app.route("/company")
def comp():
    name = request.args.get("name")
    return json_util.dumps(get_company(name))

@app.route("/insert/<collection>")
def insert(collection):
    return json_util.dumps(insert_data(collection, dict(request.args)))


@app.route("/sql/<name>")
def sql(name):
    return json_util.dumps(list(get_table(name)))


@app.route("/flash")
def flash():
    return open("w6d4-api/templates/meme.html","r").read()

@app.route("/memes")
def meme():
    directory = os.path.join(os.getcwd(), "w6d4-api/memes")
    print(directory)
    files = choice(os.listdir("w6d4-api/memes"))
    return send_from_directory(directory=directory, filename=files, as_attachment=True)


'''