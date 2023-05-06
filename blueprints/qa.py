from flask import Blueprint, render_template, request, g, redirect, url_for
from .forms import QuestionForm, AnswerForm
from models import QuestionModel, AnswerModel
from exts import db
from decorators import login_required

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/test')
def sd():
    return render_template('login.html')


@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template('index.html', questions=questions)


@bp.route('/qa/public', methods=['GET', 'POST'])
@login_required
def public_question():
    # if not g.user:
    #     return redirect(url_for('auth.login'))
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            resume_name = form.resume_name.data
            introduce = form.introduce.data
            question = QuestionModel(resume_name=resume_name, introduce=introduce, merchant=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            print(form.errors)
            return redirect(url_for('qa.public_question'))


@bp.route('/qa/detail/<qa_id>')
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template('detail.html', question=question)


# @bp.route('/answer/public', methods=['POST'])
@bp.post('/answer/public')
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, question_id=question_id, cuisine_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('qa.qa_detail', qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for('qa.qa_detail', qa_id=request.form.get('question_id')))


@bp.route('/search')
def search():
    q = request.args.get('q')
    questions = QuestionModel.query.filter(QuestionModel.resume_name.contains(q)).all()
    return render_template('index.html', questions=questions)