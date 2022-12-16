import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

mongo = PyMongo(app)

fs = gridfs.GridFS(mongo.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()


@app.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)
    if err:
        return err
    return token


@app.route("/upload", methods=["POST"])
def upload():
    access, err = validate.token(request)
