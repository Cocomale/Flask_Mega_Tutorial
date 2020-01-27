from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Laura'}
    posts = [
        {
            'author': {'username': 'Coco'},
            'body': 'Te amo carino!'
        },
        {
            'author': {'username': 'Kathe'},
            'body': 'Te amo tambien carino mio!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


