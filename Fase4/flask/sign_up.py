from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from flask import Flask, current_app
from pymongo import MongoClient
import os
import json
from .__init__ import app, home


@app.route('/sign_up', methods=['POST'])
def sign_up():
    render_template('sign_up.html', name='home.html')
    return home()
