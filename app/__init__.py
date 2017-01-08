from flask import Flask

my_app = Flask(__name__) # Miguel called the variable "app"
from app import views
