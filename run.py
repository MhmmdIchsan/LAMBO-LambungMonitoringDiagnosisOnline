from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return 'Welcome to my Flask project!'

@app.route('/about')
def about():
    return 'This is the about page.'
