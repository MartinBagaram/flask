from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return 'Hello, World and friends! I did some changes'

@app.route('/about')
def about():
    return 'This is about me not anayone else'


if __name__=='__main__':
    app.run(debug=True)
