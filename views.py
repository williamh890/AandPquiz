from flask import request, render_template, url_for
from app import app
import json

@app.route('/')
def start():
    return render_template('index.html')

class Answer:
    def __init__(self, qText, submitied, correct):
        self.question_text = qText
        self.submitied_answer = submitied
        self.isCorrect = correct


@app.route('/questions', methods=['GET', 'POST'])
def questions():
    #open the json file
    with open("AandPQuestions.json") as questions:
        quiz=json.load(questions)['quiz']

        if request.method == 'GET':
                #pass the json dicitonary to the template
                return render_template("question.html", quiz=quiz)

        #the information is being submitied
        if request.method == 'POST':
            submissions = []
            total_correct = 0
            isCorrect = False
            #look through the answers

            for question, submitted_answer in request.form.items():

                if quiz[question]["answer"] == submitted_answer:
                    isCorrect = True
                    total_correct += 1
                else:
                    isCorrect = False
                submissions.append(Answer(question, submitted_answer, isCorrect))

            #return "%f, %f, %f" % (total_correct, len(quiz), (total_correct / len(quiz)) * 100)
            return render_template("submission.html", submissions=submissions,
                                                      total_correct=total_correct,
                                                      length=len(quiz),
                                                      percentage=((total_correct / len(quiz) * 100)))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
