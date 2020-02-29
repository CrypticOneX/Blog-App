from flask import Flask, render_template, url_for, flash, get_flashed_messages, redirect
from forms import SignupUser, SigninUser

app = Flask(__name__)

app.config['SECRET_KEY'] = '24f0f4380e3b73eadaaf0fcaa4a139c5'

posts = [
    {
        "title": "Hello World",
        "author": "Ashutosh Singh",
        "posted_on": "Feb, 27 2020",
        "content": '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut iure repellat explicabo esse possimus laborum, soluta ex qui deleniti.
                        Ipsa blanditiis sit repudiandae aperiam nisi consequuntur rem, officiis soluta? Temporibus.'''
    },
    {
        "title": "Hello Dex",
        "author": "Dexter Root",
        "posted_on": "Feb, 28 2020",
        "content": '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut iure repellat explicabo esse possimus laborum, soluta ex qui deleniti.
                        Ipsa blanditiis sit repudiandae aperiam nisi consequuntur rem, officiis soluta? Temporibus.'''
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignupUser()
    if form.validate_on_submit():
        flash(f"User successfully signedup with {form.username}!", 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', form = form)

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = SigninUser()
    if form.email.data == "ashutosh@darkshell.com" and form.password.data == "password":
        flash("User signed in successfuuly", 'success')
        return redirect(url_for('home'))
    else:
        flash("Invalid username and password", 'danger')
    return render_template('signin.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)