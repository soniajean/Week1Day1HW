
from app import app

from flask import render_template


@app.route('/')
def homePage():
    artists = [
        {
        'name': 'Joyner Lucas',
        'age': 34,
        'spec' : 'American Rapper'
        },
        {
        'name': 'J. Cole',
        'age' : 38,
        'spec' : 'American rapper and record producer'
        },
        {
        'name' : 'Sofaygo',
        'age' : 21,
        'spec': 'American rapper from Georgia'
        },
        {
        'name': 'Kanye West',
        'age' : 45,
        'spec' : 'American rapper'
        },
        {
        'name' : 'Drake',
        'age' : 36,
        'spec': 'Canadian rapper, singer, songwriter and actor'
        }
    ]
    fav_musician = 'Top 5 Artists'
    return render_template('index.html', artists=artists, f = fav_musician)

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/landing')
def landingPage():
    return render_template('landing.html')
    
