from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.Trivias    #Select the database
todos = db.Categorias #Select the collection name

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('CrearCategoria')

@app.route("/")
@app.route("/list")
def lists ():
	#Display the all Tasks
	
	todos_l = todos.find()
	a1="active"
	return render_template('CrearCategoria.html',a1=a1,todos=todos_l,t=title,h=heading)

@app.route("/action", methods=['POST'])
def action ():
	#Adding a Task
	name=request.values.get("name")
	desc=request.values.get("desc")
	todos.insert({ "Categoria":name, "desc":desc})
	return redirect("/list")

@app.route("/remove")
def remove ():
	#Deleting a Task with various references
	key=request.values.get("_id")
	todos.remove({"_id":ObjectId(key)})
	return redirect("/")

@app.route("/update")
def update ():
	id=request.values.get("_id")
	task=todos.find({"_id":ObjectId(id)})
	return render_template('modificarCategoria.html',tasks=task,h=heading,t=title)

@app.route("/action3", methods=['POST'])
def action3 ():
	#Updating a Task with various references
	name=request.values.get("name")
	desc=request.values.get("desc")
	id=request.values.get("_id")
	todos.update({"_id":ObjectId(id)}, {'$set':{ "Categoria":name, "desc":desc}})
	return redirect("/")

todosT = db.Trivia11 #Select the collection name

@app.route("/CrearTrivia.html")
def CTrivia ():
	todos_lT = todosT.find()
	return render_template("/CrearTrivia.html",todos=todos_lT,t=title,h=heading)

@app.route("/ModificarTrivia.html")
def MTrivia ():
	todos_lT = todosT.find()
	id=request.values.get("_id")
	task=todosT.find({"_id":ObjectId(id)})
	return render_template('ModificarTrivia.html',tasks=task,h=heading,t=title)



@app.route("/removeTrivia")
def removeT ():
	todos_lT = todosT.find()
	#Deleting a Task with various references
	key=request.values.get("_id")
	todosT.remove({"_id":ObjectId(key)})
	return redirect("/CrearTrivia.html")

@app.route("/Administrador.html")
def AdminTri ():
	#Deleting a Task with various references

	return redirect("/CrearTrivia.html")


@app.route("/actionCT", methods=['POST'])
def actionCT ():

	client = MongoClient("mongodb://127.0.0.1:27017") #host uri
	db = client.Trivias    #Select the database
	todos = db.Trivia11 #Select the collection name
	#Adding a trivia
	question=request.values.get("preguntaTrivia")
	choiceA=request.values.get("pregunta1")
	choiceB=request.values.get("pregunta2")
	choiceC=request.values.get("pregunta3")
	choiceD=request.values.get("pregunta4")
	correct=request.values.get("Respuesta")
	Categoria=request.values.get("select")
	todos.insert({ "question":question, "choiceA":choiceA,"choiceB":choiceB ,"choiceC":choiceC,"choiceD":choiceD,"correct ":correct,"Categoria":Categoria })
	return redirect("/Administrador.html")

@app.route("/actionMT", methods=['POST'])
def actionMT ():
	
	Categoria=request.values.get("select")

	question=request.values.get("preguntaTrivia")
	choiceA=request.values.get("pregunta1")
	choiceB=request.values.get("pregunta2")
	choiceC=request.values.get("pregunta3")
	choiceD=request.values.get("pregunta4")
	correct=request.values.get("Respuesta")
	Categoria=request.values.get("select")
	id=request.values.get("_id")
	todosT.update({"_id":ObjectId(id)}, {'$set':{ "question":question, "choiceA":choiceA,"choiceB":choiceB ,"choiceC":choiceC,"choiceD":choiceD,"correct ":correct,"Categoria":Categoria }})
	
	
	
	return redirect("/Administrador.html")


if __name__ == "__main__":

    app.run()
