from flask import Flask, render_template, request
from datetime import datetime
import requests
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/dogs', methods=['GET'])
def dogs():
    images = requests.get('http://shibe.online/api/shibes?count=5&urls=true').json()
    return render_template('dogs.html', links=images)

@app.route('/cats', methods=['GET'])
def cats():
    fact = requests.get('https://cat-fact.herokuapp.com/facts/random?count=1&facts=true').json()
    return render_template('cats.html', links=fact)

@app.route('/', methods=['GET'])
def main():
    hostname = request.host_url
    message = 'cool feature'
    return render_template('main.html', host=hostname, msg=message)

@app.route('/about', methods=['GET'])
def mission():
    current_time = datetime.now()
    return render_template('about.html', time=current_time)

@app.route('/artist', methods=['GET'])
def artist():
    return 'Juice WRLD'