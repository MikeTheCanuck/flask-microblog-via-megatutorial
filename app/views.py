from app import my_app # Miguel named the variable "app" instead of my_app

@my_app.route('/')
@my_app.route('/index')
def index():
    return "Hello Mr. Stark"
