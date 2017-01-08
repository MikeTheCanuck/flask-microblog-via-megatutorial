from flask import render_template
from app import my_app # Miguel named the variable "app" instead of my_app

@my_app.route('/')
@my_app.route('/index')
def index():
    user = {'nickname': 'Tony'} # mock user object while we populate other more critical code
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'Coulson'},
            'body': 'Beautiful day in Portland with my cellist!  Hope she doesn\'t run into any powered stalkers.'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The FF movie could have been better, but at least I wasn\'t wearing a thong!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
