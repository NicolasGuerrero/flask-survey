from flask import Flask, render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES_KEY = 'response'

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def questions_page():
    return render_template("/start_survey.html", survey=survey)

@app.route("/start_survey", methods=["POST"])
def start_survey():
    session[RESPONSES_KEY] = []
    return redirect("/questions/0")


@app.route("/questions/<int:qid>")
def ask_question(qid):
    if qid != len(session[RESPONSES_KEY]):
        return redirect(f"/questions/{len(session[RESPONSES_KEY])}") 
    if len(session[RESPONSES_KEY]) == len(survey.questions):
        return redirect("/complete")
    question = survey.questions[qid].question
    choice_0 = survey.questions[qid].choices[0]
    choice_1 = survey.questions[qid].choices[1]
    return render_template("/question_template.html", question=question,
    option_0=choice_0, option_1=choice_1)

@app.route("/complete")
def completed_survey():
    return render_template('complete.html')

# @app.route("/questions/<int:qid>", methods=["POST"])
# def ask_question():
#     question_1 = survey.questions[qid].question
#     choice_0 = survey.questions[qid].choice[0]
#     choice_1 = survey.questions[qid].choice[1]
#     return redirect("/questions/2", question=question_qid, option_0=choice_0, option_1=choice_1)


# @app.route("/questions/2", methods=["POST"])
# def ask_question_2():
#     question_2 = survey.questions[2].question
#     choice_0 = survey.questions[2].choice[0]
#     choice_1 = survey.questions[2].choice[1]
#     return redirect("/questions/3", question=question_2, option_0=choice_0, option_1=choice_1)


# @app.route("/questions/3", methods=["POST"])
# def ask_question_3():
#     question_3 = survey.questions[3].question
#     choice_0 = survey.questions[3].choice[0]
#     choice_1 = survey.questions[3].choice[1]
#     return redirect("/questions/3", question=question_3, option_0=choice_0, option_1=choice_1)
#     return redirect("/thanks")

@app.route("/answer", methods=["POST"])
def answer_handler():
    answer = request.form['choice']
    
    responses = session[RESPONSES_KEY]
    responses.append(answer)
    session[RESPONSES_KEY] = responses

    print('responses =', responses)

    if (len(responses) == len(survey.questions)):
        return redirect('/complete')

    else:
        return redirect(f"/questions/{len(responses)}")