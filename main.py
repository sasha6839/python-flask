from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>Моя сторінка на Flask №8456</h1><br><a href='http://127.0.0.1:5000/about'>seffdhdfag</a><br><a href='http://127.0.0.1:5000/sanya'>seffdhdfag</a>"
    return render_template('index.html')


@app.route('/Explore')
def about():
    return "<h1>Я Sanya228</h1><br><a href='http://127.0.0.1:5000/'>назад</a>"


@app.route('/login')
def login():
    return render_template('login.html')


#лише для локального сервера
if __name__ == '__main__':
    app.run(debug=True)