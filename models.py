from exts import db
from datetime import datetime


# 数据库映射三部曲
# flask db init：只需要执行一次
# flask db migrate：将orm模型生成迁移脚本
# flask db upgrade：将迁移脚本映射到数据库中

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class QuestionModel(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resume_name = db.Column(db.String(20), nullable=False)
    introduce = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now())

    # 外键
    merchant_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    merchant = db.relationship(UserModel, backref='questions')


class AnswerModel(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())

    # 外键
    question_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    cuisine_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # 关系
    question = db.relationship(QuestionModel, backref=db.backref('answers', order_by=create_time.desc()))
    merchant = db.relationship(UserModel, backref='answers')