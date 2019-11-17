from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '044c16e09c56ad89a1e136f98ebd0fcc'


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
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@bag.com' and form.password.data == 'password':
            flash('logged in successfully', 'success')
            return redirect(url_for('home'))
        flash('Failed try again', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)
