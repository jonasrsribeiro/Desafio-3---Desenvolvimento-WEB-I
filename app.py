from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

app.secret_key = b'42'

from dbconnection import *

from routes import *

app.run(debug=True)