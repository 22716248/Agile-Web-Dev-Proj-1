from typing import NewType
from flask.globals import session
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, QuizForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Question, User, Score
from werkzeug.urls import url_parse
from sqlalchemy import and_
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    quizform = QuizForm()
    if quizform.validate_on_submit():
        user_id = current_user.get_id()
        scores = []
        attempts_list = Score.query.with_entities(Score.attempts).where(Score.user_id == user_id).all()
        if attempts_list:
            curr_attempt = max(attempts_list)[0] + 1
        else:
            curr_attempt = 1

        # All questions hardcoded

        #Question 1
        if quizform.question1.data == "Crux":
            newScore = Score(user_id=user_id, score=1, question_id=1, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=1, attempts=curr_attempt)
            scores.append(newScore)

        #Question 2
        if quizform.question2.data == "Australia, New Zealand, Brazil, Papua New Guinea, Samoa":
            newScore = Score(user_id=user_id, score=1, question_id=2, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=2, attempts=curr_attempt)
            scores.append(newScore)

        #Question 3
        if quizform.question3.data == "Aquarius":
            newScore = Score(user_id=user_id, score=1, question_id=3, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=3, attempts=curr_attempt)
            scores.append(newScore)

        #Question 4
        if quizform.question4.data == "Orion":
            newScore = Score(user_id=user_id, score=1, question_id=4, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=4, attempts=curr_attempt)
            scores.append(newScore)

        #Question 5
        if quizform.question5.data == "Centaurus":
            newScore = Score(user_id=user_id, score=1, question_id=5, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=5, attempts=curr_attempt)
            scores.append(newScore)

        #Question 6
        if quizform.question6.data == "Lupus":
            newScore = Score(user_id=user_id, score=1, question_id=6, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=6, attempts=curr_attempt)
            scores.append(newScore)

        #Question 7
        if quizform.question7.data == "Sagittarius":
            newScore = Score(user_id=user_id, score=1, question_id=7, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=7, attempts=curr_attempt)
            scores.append(newScore)

        #Question 8
        if quizform.question8.data == "Scorpius":
            newScore = Score(user_id=user_id, score=1, question_id=8, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=8, attempts=curr_attempt)
            scores.append(newScore)

        #Question 9
        if quizform.question9.data == "Canis Major":
            newScore = Score(user_id=user_id, score=1, question_id=9, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=9, attempts=curr_attempt)
            scores.append(newScore)

        #Question 10
        if quizform.question10.data == "Alpha Centauri":
            newScore = Score(user_id=user_id, score=1, question_id=10, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=10, attempts=curr_attempt)
            scores.append(newScore)

        db.session.add_all(scores)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('quiz.html', title='Quiz', quizform=quizform)

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
    user_id = current_user.get_id()
    attempts_list = Score.query.with_entities(Score.attempts).where(Score.user_id == user_id).all()
    score = Score.query.filter(and_(Score.user_id==user_id,Score.score==1)).count()
    scores = []
    if attempts_list:
            attempts = max(attempts_list)[0]
            for i in list(range(attempts)):
                score = Score.query.filter(and_(Score.user_id==user_id,Score.score==1,Score.attempts == i+1)).count()
                scores.append({'body':score})
    else:
        scores=[{'body':"Have not attempted the quiz"}]
    
    return render_template('profile.html', user=user, scores=scores)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')