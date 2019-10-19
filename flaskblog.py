from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__) # setting app variable to an instance of Flask class
# __name__ variable in python - name of module
# __name__ is equal to __main__ if run the script with python directly
# but if we import this module somewhere else then the name will be the name of our module

app.config['SECRETE_KEY'] = '0198e4911acf2bf856c7a18f0b907b22'

posts = [
    {
        'author': 'Ankita Bhagat',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Vidhi Patel',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# Create route
@app.route('/') # decorator for home or root page
@app.route('/home')
def hello():
    #return "<h1>Home Page</h1>"
    return render_template('home.html', posts=posts)

@app.route('/about') # decorator for about page
def about():
    #return "<h1>About Page</h1>"
    return render_template('about.html', posts=posts, title='About')

@app.route('/register') # decorator for about page
def register():
    form = RegistrationForm()
    return render_template('register.html', posts=posts, title='Register', form=form)
    
@app.route('/login') # decorator for about page
def login():    
    form = LoginForm()
    return render_template('login.html', posts=posts, title='Login', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)