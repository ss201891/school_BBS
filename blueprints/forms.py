import wtforms
from wtforms.validators import Length, EqualTo, InputRequired


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=20, message='用户名格式错误！')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message='密码格式错误！')])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=20, message='用户名格式错误！')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message='密码格式错误！')])


class QuestionForm(wtforms.Form):
    resume_name = wtforms.StringField(validators=[Length(min=2, max=20, message='简历名格式错误！')])
    introduce = wtforms.StringField(validators=[Length(max=200, message='字数超出上限！')])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(max=100, message='字数超出上限！')])
    question_id = wtforms.IntegerField(validators=[InputRequired(message='必须要传入问题id')])