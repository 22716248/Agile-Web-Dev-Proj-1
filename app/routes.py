from typing import NewType
from flask.globals import session
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, QuizForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Score
from werkzeug.urls import url_parse
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/quiz')
def quiz():
    form = QuizForm()
    if form.validate_on_submit:
        user_id = current_user.get_id()
        scores = []

        # All questions hardcoded

        #Question 1
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 2
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 3
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 4
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 5
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 6
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 7
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 8
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 9
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        #Question 10
        if form.question1.data == "answer":
            newScore = Score(user_id=user_id, score=1) # Make DB add a new attempt each time? !<<<<<<<<<<<
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0)
            scores.append(newScore)

        db.session.add_all(scores)
        db.session.commit()
        #return redirect(url_for('index'))
    return render_template('quiz.html', title='Take Quiz', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.checkpw(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.setpw(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    score = [
        {'User': user, 'Score': 'score'},
    ]
    return render_template('profile.html', user=user, score=score)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')