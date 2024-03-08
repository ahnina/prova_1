from flask import Flask, render_template, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('caminhos.json')
caminho = Query()

@app.route("/")
def index():
    return render_template("novo.html")

@app.route("/novo", methods=["POST"])
def novo(x, y,z,r):
    id = request.form.get("id")
    x = request.form.get("x")
    y = request.form.get("y")
    z = request.form.get("z")
    r = request.form.get("r")
    db.insert({'id': id, 'x': x, "y": y, "z": z, "r" : r})
    return render_template("index.html")



@app.route("/pegar_caminho", methods= ["GET"])
def pegar_caminho(id):
    id = request.form.get("id")
    db.search(caminho.id == id)

@app.route("/listas_caminhos", methods= ["GET"])
def listas_caminhos():
    db.all()

@app.route("atualizar", methods= ["GET"])
def atualizar(id):
    id = request.form.get("id")
    x = request.form.get("x")
    y = request.form.get("y")
    z = request.form.get("z")
    r = request.form.get("r")
    db.update({'x': x, "y": y, "z": z, "r" : r}, caminho.id == id)

@app.route("/deletar", methods= ["GET"])
def deletar(id):
    id = request.form.get("id")
    db.remove(caminho.id == id)