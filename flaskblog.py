from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Martin Bagaram',
        'title': 'First post',
        'content': 'My posts content',
        'date_posted': '11-12-2019'
    },
    {
        'author': 'Bella Bagaram',
        'title': 'First post',
        'content': 'Bella post content',
        'date_posted': '11-12-2019'
    }
]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__=='__main__':
    app.run(debug=True)
