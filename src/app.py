from flask import Flask,  render_template, session, request, current_app
from config import Config
from database.db import init_db
from models.quiz import Question, Option
from populate_db import populate_db

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    highest_score = session.get('highest_score', 0)

    if request.method == 'POST':
        # 
        answers = request.form.to_dict()
        score = 0
        results = []

        for question_id, option_id in answers.items():
            question = Question.query.get(int(question_id.split('_')[1]))
            selected_option = Option.query.get(int(option_id))
            correct_option = next((opt for opt in question.options if opt.is_correct), None)

            if selected_option.is_correct:
                score += 5

            results.append((question.question_text, selected_option.option_text, correct_option.option_text))

        total_questions = len(results)
        
        if score > highest_score:
            session['highest_score'] = score

        return render_template('results.html', score=score,  highest_score=highest_score, total_questions=total_questions, results=results)

    questions = Question.query.all()
    return render_template('quiz.html', questions=questions, highest_score=highest_score)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    highest_score = session.get('highest_score', 0)
    
    answers = request.form.to_dict()
    score = 0
    results = []

    for question_id, option_id in answers.items():
        question = Question.query.get(int(question_id.split('_')[1]))
        selected_option = Option.query.get(int(option_id))
        correct_option = next((opt for opt in question.options if opt.is_correct), None)

        if selected_option.is_correct:
            score += 5

        results.append((question.question_text, selected_option.option_text, correct_option.option_text))

    total_questions = len(results)

    if score > highest_score:
        session['highest_score'] = score

    return render_template('results.html', highest_score=highest_score, score=score, total_questions=total_questions, results=results)

@app.route('/results', methods=['GET'])
def results():
   
    return render_template('results.html')

@app.route('/populate', methods=['GET', 'POST'])
def populate():
    if request.method == 'POST':
        populate_db(current_app)
    return render_template('populate.html')

if __name__ == '__main__':
    app.run(debug=True)