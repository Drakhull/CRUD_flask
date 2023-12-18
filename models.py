from database import db


class User(db.Model):
  __tablename__= 'user'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  cpf = db.Column(db.String(11))
  birth = db.Column(db.String(10))
  gender = db.Column(db.String(1))
  register = db.Column(db.String(11))
  

  def __init__(self, name, cpf, birth, register, gender):
    self.name = name
    self.cpf = cpf
    self.birth = birth
    self.gender = gender
    self.register = register

  def __repr__(self):
    return f'User: {self.name}'