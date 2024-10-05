from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'


class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(255), nullable=False)
    post_test = db.Column(db.Text(), nullable=False)
    post_image = db.Column(db.String(255), nullable=False)
    continent = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.Date(), default=datetime.utcnow())


# створюємо базу даних, використовуємо один раз, після створення закоментувати
# with app.app_context():
#     db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles')
def articles():
    new_articles = ['How to avoid expensive travel mistakes', 'Top 5 places to experience supernatural forces',
                    'Three wonderfully bizarre Mexican festivals', 'The 20 greenest destinations on Earth',
                    'How to survive on a desert island']

    return render_template('articles.html', articles=new_articles)


@app.route('/add_article', methods=['POST'])
def add_article():
    post_name = request.form['title']
    post_test = request.form['text']
    post_image = request.form['URL']
    continent = request.form['continent']

    row = Poster(post_name=post_name,
                 post_test=post_test,
                 post_image=post_image,
                 continent=continent)
    db.session.add(row)
    db.session.commit()

    return render_template('add_article.html')


@app.route('/add_article', methods=['GET'])
def add_article_form():
    return render_template('add_article.html')

@app.route('/details')
def details():
    return render_template('details.html')


@app.route('/login')
def login():    
    return render_template('login.html', message=message)



@app.route('/about')
def about():
    return render_template('about.html', title='About')


# Only for local server (deleted)
if __name__ == '__main__':
    app.run(debug=True)
