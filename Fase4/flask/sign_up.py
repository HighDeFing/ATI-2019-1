from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
import json
from .__init__ import app, home


@app.route('/sign_up', methods=['POST'])
def sign_up():
    redirect('/homelogin.html', code=200)
    return home()
