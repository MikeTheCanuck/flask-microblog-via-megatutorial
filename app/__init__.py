from flask import Flask

my_app = Flask(__name__) # Miguel named the variable "app"
from app import views
