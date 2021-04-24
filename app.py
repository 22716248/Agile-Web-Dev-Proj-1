from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'testlogin' or request.form['password'] != 'testpassword':
            error = "login details not allowed"
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error = error)

if __name__=='__main__':
    app.run(debug=True)