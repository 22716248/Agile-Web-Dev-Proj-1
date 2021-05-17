from typing import NewType
from flask.globals import session
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, QuizForm, RegistrationForm, ResetForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Question, User, Score
from werkzeug.urls import url_parse
from sqlalchemy import and_

# Routes the index main page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

# Routes the user to the quiz page
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
        if (quizform.question1.data).lower() == "crux":
            newScore = Score(user_id=user_id, score=1, question_id=1, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=1, attempts=curr_attempt)
            scores.append(newScore)

        #Question 2
        if( quizform.question2.data).lower() == "aquarius":
            newScore = Score(user_id=user_id, score=1, question_id=2, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=2, attempts=curr_attempt)
            scores.append(newScore)

        #Question 3
        if( quizform.question3.data).lower() == "centaurus":
            newScore = Score(user_id=user_id, score=1, question_id=3, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=3, attempts=curr_attempt)
            scores.append(newScore)

        #Question 4
        if( quizform.question4.data).lower() == "scorpius":
            newScore = Score(user_id=user_id, score=1, question_id=4, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=4, attempts=curr_attempt)
            scores.append(newScore)

        #Question 5
        if( quizform.question5.data).lower() == "sagittarius":
            newScore = Score(user_id=user_id, score=1, question_id=5, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=5, attempts=curr_attempt)
            scores.append(newScore)

        #Question 6
        if( quizform.question6.data).lower() == "lupus":
            newScore = Score(user_id=user_id, score=1, question_id=6, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=6, attempts=curr_attempt)
            scores.append(newScore)

        #Question 7
        if( quizform.question7.data).lower() == "puppis":
            newScore = Score(user_id=user_id, score=1, question_id=7, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=7, attempts=curr_attempt)
            scores.append(newScore)

        #Question 8
        if( quizform.question8.data).lower() == "vela":
            newScore = Score(user_id=user_id, score=1, question_id=8, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=8, attempts=curr_attempt)
            scores.append(newScore)

        #Question 9
        if( quizform.question9.data).lower() == "centaurus":
            newScore = Score(user_id=user_id, score=1, question_id=9, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=9, attempts=curr_attempt)
            scores.append(newScore)

        #Question 10
        if (quizform.question10.data).lower() == "orion":
            newScore = Score(user_id=user_id, score=1, question_id=10, attempts=curr_attempt)
            scores.append(newScore)
        else:
            newScore = Score(user_id=user_id, score=0, question_id=10, attempts=curr_attempt)
            scores.append(newScore)

        db.session.add_all(scores)
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))
    return render_template('quiz.html', title='Quiz', quizform=quizform)

# Routes the user to the Login Page
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
        return redirect(url_for('user', username=current_user.username))
    return render_template('login.html', title='Sign In', form=form)

# Logs out the current user
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

# Register a new user
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

# Routes the current user to their profile page
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    user_id = current_user.get_id()
    attempts_list = Score.query.with_entities(Score.attempts).where(Score.user_id == user_id).all()
    scores = []
    #generating list of attempts
    if attempts_list:
            attempts = max(attempts_list)[0]
            for i in list(range(attempts)):
                ls = []
                score = Score.query.filter(and_(Score.user_id==user_id,Score.attempts == i+1)).all()
                scoret = Score.query.filter(and_(Score.user_id==user_id,Score.score==1,Score.attempts == i+1)).count()
                #looping through each attempt and generating a score list
                for x in list(range(len(score))):
                    if str(score[x]) == "<score 0>":
                        ls.append("Q" + str(x + 1) + ": " + '\u274C')
                    if str(score[x]) == "<score 1>":
                        ls.append("Q" + str(x + 1) + ": " + '\u2714')
                ls.append("TOTAL : " + str(scoret) + "/10")
                scores.append({'body':ls})
    else:
        scores=[{'body':"Have not attempted the quiz"}]
    
    return render_template('profile.html', user=user, scores=scores)

# Lets the brower know
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# Routes the user to the reset password page
@app.route('/reset', methods=['GET', 'POST'])
@login_required
def reset():
    user = current_user
    form = ResetForm()
    if form.validate_on_submit():
        if not user.checkpw(form.password_o.data):
            flash("Password Incorrect")
            return redirect(url_for('reset'))
        user.setpw(form.password_n.data)
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))
    return render_template('reset.html', title= 'Reset Password', form=form)