# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template
from flask import request,redirect,url_for,flash # For flask implementation

from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
import random

app = Flask(__name__)

punkty = 0
a = 0
cor =2
pre=0


# konfiguracja aplikacji
app.config.update(dict(
 SECRET_KEY='bradzosekretnawartosc',
))


client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.Trivias   #Select the database
todos  = db.Trivia11 #Select the collection name

todos_l=[]



def rando(): 
    x=todos_l.count()-1
    y=random.randint(0,x)
    return redirect(url_for('index'))
    
@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('Home.html')

@app.route('/Home.html', methods=['GET', 'POST'])
def home():
    return render_template('Home.html')

@app.route('/trivias1.html', methods=['GET', 'POST'])
def trivias1():
    return render_template('trivias1.html')



@app.route('/jugar.html', methods=['GET', 'POST'])
def index():
    global punkty
    global todos_l
    global cor
    todos_l = todos.find()
    global a
    global pre

    if request.method == 'GET':

        print("a es ete ",a)
        return render_template('w.html', todos=todos_l,a3=a,men=1,core=cor,pun=punkty)
    
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
         
    return render_template('w.html', todos=todos_l,a3=a,men=1,core=cor,pun=punkty)
        

    #return 'Cześć, tu Python!'


@app.route("/nuevo")
def menu ():
	#cuando llego a la ultima pregunto muestro que finalizo y gano x puntos
    flash(u'estoy en nuevo {0}'.format(punkty))
    cor=2
    #el valor anterior lo mando a la BD
    return render_template('w.html', todos=todos_l,a3=a,men=0,core=cor,pun=punkty)


@app.route("/help.html")
def Phelp ():
	#voy nuevamente a la pagina principal para seleccionar otra trivia
    flash(u'estoy en nuevo del gert {0}'.format(punkty))
    #el valor anterior lo mando a la BD
    return render_template('help.html')




    #return 'Cześć, tu Python!'









if __name__ == '__main__':
    app.run(debug=True)