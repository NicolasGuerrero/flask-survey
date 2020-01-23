from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

responses = []

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/")
def questions_page():
    return render_template("/base.html")
    
def start_survey():
    return redirect("/questions/0")

@app.route("/questions/0", methods=["POST"])
def ask_question_0():
    question_0 = surveys["satisfaction"].questions[0].question
    choice_0 = surveys["satisfaction"].questions[0].choice[0]
    choice_1 = surveys["satisfaction"].questions[0].choice[1]

    return render_template("/question_template", question=question_0, option_0=choice_0, option_1=choice_1)
    responses.append(request.form["choice"])

    return redirect("/questions/1")

@app.route("/questions/1", methods=["POST"])
def ask_question_1():
    question_1 = surveys["satisfaction"].questions[1].question
    choice_0 = surveys["satisfaction"].questions[1].choice[0]
    choice_1 = surveys["satisfaction"].questions[1].choice[1]
    
    return redirect("/questions/2", question=question_1, option_0=choice_0, option_1=choice_1)

@app.route("/questions/2", methods=["POST"])
def ask_question_2():
    question_2 = surveys["satisfaction"].questions[2].question
    choice_0 = surveys["satisfaction"].questions[2].choice[0]
    choice_1 = surveys["satisfaction"].questions[2].choice[1]
    
    return redirect("/questions/3", question=question_2, option_0=choice_0, option_1=choice_1)


@app.route("/questions/3", methods=["POST"])
def ask_question_3():
    question_3 = surveys["satisfaction"].questions[3].question
    choice_0 = surveys["satisfaction"].questions[3].choice[0]
    choice_1 = surveys["satisfaction"].questions[3].choice[1]
    
    return redirect("/questions/3", question=question_3, option_0=choice_0, option_1=choice_1)
    return redirect("/thanks")