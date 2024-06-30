import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'lab9.db')
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('lab9.html')

@app.route('/find', methods=['POST'])
def find(name='', telephone=''):
    name = request.form['name']
    telephone = request.form['telephone']
    if name != '':
        entities = Entity.query.filter_by(name=name).all()
        return render_template('lab9.html', entities=entities)
    elif telephone != '':
        entities = Entity.query.filter_by(telephone=telephone).all()
        return render_template('lab9.html', entities=entities)
    else:
        return render_template('lab9.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    telephone = request.form['telephone']
    entity = Entity(name=name, telephone=telephone)
    db.session.add(entity)
    db.session.commit()
    return render_template('lab9.html')

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    telephone = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Entity {self.name}>'
