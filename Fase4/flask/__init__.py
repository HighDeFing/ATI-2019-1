from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from flask import Flask, current_app
from pymongo import MongoClient
import os
import json

app = Flask(__name__)

#variables globales 

punkty = 0
a = 0
cor =2
pre=0
todos=[]
todos_l=[]

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017) #host
client.drop_database('Trivias')

db = client['Trivias'] #database created
db = client.Trivias
db.Categorias.delete_many({}) #restart from zero
db.Trivia11.delete_many({})

todosC = db["Categorias"] #create the name of categorias
with open('Fase4/flask/categoria.json') as json_file:
    data = json.load(json_file)
todosC = db.Categorias
db.todosC.insert_many(data)

todos = db["Trivia11"] #collection of trivias
with open('Fase4/flask/trivias11.json') as json_file:
    data = json.load(json_file)
todos = db.Trivia11 #Select the collection name
db.todos.insert_many(data)


@app.route('/')
@app.route('/home.html')
def home(name=None):
    if not session.get('logged_in'):
        global a
        a=0
        global punkty
        punkty=0
        return render_template('home.html', name='home.html')
    elif session.get('logged_in'):
        return render_template('homelogin.html', name='home.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    if request.form['password'] == '1234' and request.form['username'] == 'heider':
        session['logged_in'] = True
    else:
        session['logged_in'] = True
    return home()


@app.route('/login', methods=['POST'])
def do_user_login():
    if request.form['password'] == '1234' and request.form['username'] == 'heider':
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/Home.html', methods=['GET', 'POST'])
def home1():
    return redirect("/home.html")

@app.route('/trivias1.html', methods=['GET', 'POST'])
def trivias1():
    global todos
    client = MongoClient(
        os.environ['DB_PORT_27017_TCP_ADDR'], 27017)  # host
    db = client.Trivias  # Select the database
    todos = db.Trivia11  # Select the collection name
    global a
    a=0
    global punkty
    punkty=0
    return render_template('trivias1.html')


@app.route('/jugar.html', methods=['GET', 'POST'])
def index():
    global punkty
    global todos_l
    
    global cor
    client = MongoClient(
        os.environ['DB_PORT_27017_TCP_ADDR'], 27017)  # host
    db = client.Trivias  # Select the database
    todos = db.Trivia11  # Select the collection name
    todos_l = db.todos.find()
    global a
    global pre

    if request.method == 'GET':

        print("a es ete ",a)
        return render_template('jugar.html', todos=todos_l,a3=a,men=1,core=cor,pun=punkty)
    
    if request.method == 'POST':
        odpowiedzi = request.form['valo']
        
        if(a<todos_l.count()-1):
            print ("valor obtenido", odpowiedzi)
            print ("valor de la bd", todos_l[a]['correct '])
            if odpowiedzi == todos_l[a]['correct ']:
                    punkty += 100
                    flash(u'rspuesta correcta: {0}'.format(punkty))
                    cor =1
            else:
                flash(u'rspuesta incorrecta :( ): {0}'.format(punkty))
                cor =0
            
            a=a+1 
             
        else:
            if odpowiedzi == todos_l[a]['correct ']:
                punkty += 100
                cor =1
                flash(u'respuesta correcta: {0}'.format(punkty))
                    
            else:
                cor =0
                flash(u'rspuesta incorrecta :( ): {0}'.format(punkty))
                   
            #flash(u'esto en el else del final de arreglo {0}'.format(punkty))
            return redirect(url_for('menu'))
         
    return render_template('jugar.html', todos=todos_l,a3=a,men=1,core=cor,pun=punkty)
        
@app.route("/nuevo")
def menu ():
	#cuando llego a la ultima pregunto muestro que finalizo y gano x puntos
    flash(u'estoy en nuevo {0}'.format(punkty))
    cor=2
    #el valor anterior lo mando a la BD
    return render_template('jugar.html', todos=todos_l,a3=a,men=0,core=cor,pun=punkty)

@app.route("/help.html")
def Phelp ():
	#voy nuevamente a la pagina principal para seleccionar otra trivia
    flash(u'estoy en nuevo del gert {0}'.format(punkty))
    #el valor anterior lo mando a la BD
    return render_template('help.html')

#navegacion modo usuario
@app.route("/user.html")
def userU ():
    #el valor anterior lo mando a la BD
    return render_template('user.html')

@app.route("/rankig_usuario(BuscadorUsuario).html")
def rankingU ():
    #el valor anterior lo mando a la BD
    return render_template('rankig_usuario(BuscadorUsuario).html')

#navegacion admin
@app.route("/admin")
def admin ():    
    return render_template('admin/homeadmin.html')

@app.route("/useradmin.html")
def useradmin ():    
    return render_template('admin/useradmin.html')

@app.route("/administrar_roles.html")
def rolesdmin ():    
    return render_template('admin/administrar_roles.html')

@app.route("/helpAdmin.html")
def helpadmin ():    
    return render_template('admin/helpAdmin.html')

@app.route("/homeadmin.html")
def homeadmin ():    
    return render_template('admin/homeadmin.html')

@app.route("/visualizar_status_premios.html")
def premiosadmin ():    
    return render_template('admin/visualizar_status_premios.html')

@app.route("/visualizarGanadores.html")
def ganadores ():    
    return render_template('admin/visualizarGanadores.html')


#operaciones crud del admin
title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

#para crear categorias
client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.Trivias    #Select the database
todosC = db.Categorias #Select the collection name

@app.route("/CrearCategoria.html")
def lists ():
	#Display the all Tasks
	
	todos_l = todosC.find()
	a1="active"
	return render_template('admin/CrearCategoria.html',a1=a1,todos=todos_l,t=title,h=heading)


@app.route("/action", methods=['POST'])
def action ():
	#Adding a Task
	name=request.values.get("name")
	desc=request.values.get("desc")
	todosC.insert({ "Categoria":name, "desc":desc})
	return redirect("/list")

@app.route("/remove")
def remove ():
	#Deleting a Task with various references
	key=request.values.get("_id")
	todosC.remove({"_id":ObjectId(key)})
	return redirect("/")

@app.route("/update")
def update ():
	id=request.values.get("_id")
	task=todosC.find({"_id":ObjectId(id)})
	return render_template('admin/modificarCategoria.html',tasks=task,h=heading,t=title)

@app.route("/action3", methods=['POST'])
def action3 ():
	#Updating a Task with various references
	name=request.values.get("name")
	desc=request.values.get("desc")
	id=request.values.get("_id")
	todosC.update({"_id":ObjectId(id)}, {'$set':{ "Categoria":name, "desc":desc}})
	return redirect("/")

#para crear preguntas de trivias
  
todosT = db.Trivia11 #Select the collection name

@app.route("/CrearTrivia.html")
def CTrivia ():
	todos_lT = todosT.find()
	return render_template("admin/CrearTrivia.html",todos=todos_lT,t=title,h=heading)

@app.route("/ModificarTrivia.html")
def MTrivia ():
	todos_lT = todosT.find()
	id=request.values.get("_id")
	task=todosT.find({"_id":ObjectId(id)})
	return render_template('admin/ModificarTrivia.html',tasks=task,h=heading,t=title)



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
    client = MongoClient(
        os.environ['DB_PORT_27017_TCP_ADDR'],
        27017)  # host
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
    return redirect("Administrador.html")


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
	return redirect("Administrador.html")




if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000, debug=True)


