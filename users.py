from flask import Blueprint
from flask import render_template, request
from flask.typing import RouteCallable
from models import User
from database import db


users_bp = Blueprint('Users', __name__, template_folder = 'templates')

@users_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create_users.html')

    if request.method == 'POST':
        name = request.form.get('name')
        cpf = request.form.get('cpf')
        birth = request.form.get('birth')
        gender = request.form.get('gender')
        register = request.form.get('register')

        gender = gender.upper()

        if gender == 'M':
          gender = 'Male'
        elif gender == 'F':
            gender = 'Female'
        else:
          gender = 'Neutral'
      
        try:
            u = User(name, cpf, birth, register, gender)
            db.session.add(u)
            db.session.commit()
            return render_template('create_success.html')
        except Exception as e:
            # Verificar erros na db
            db.session.rollback()
            return f"Error: {str(e)}"

# @users_bp.route('/recovery')
# def recovery():
#   users = User.query.all()
#   return render_template('users_recovery.html', users = users)


@users_bp.route('/show')
def show():
  users = User.query.all()
  return render_template('show_students.html', users = users)


@users_bp.route('/search', methods = ['GET', 'POST'])
def search_student():
  if request.method == 'GET':
    return render_template('search_student.html')

  if request.method == 'POST':
    register_to_find = request.form.get('register')

    student = User.query.filter_by(register = register_to_find).first()

    if student:
        return render_template('student_details.html', student = student)
    else:
        return render_template('not_found.html')
      

@users_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
  if request.method == 'GET':
    u = User.query.get(id)
    return render_template('update_users.html', u = u)

  if request.method == 'POST':
    u = User.query.get(id)
    name = request.form.get('name')
    cpf = request.form.get('cpf')
    birth = request.form.get('birth')
    gender = request.form.get('gender')
    register = request.form.get('register')
    
    gender = gender.upper()

    if gender == 'M':
      gender = 'Male'
    elif gender == 'F':
        gender = 'Female'
    else:
      gender = 'Neutral'
    
    u.name = name
    u.cpf = cpf
    u.birth = birth
    u.gender = gender
    u.register = register
    db.session.add(u)
    db.session.commit()
    return render_template('update_success.html')
    


@users_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
  if request.method == 'GET':
    u = User.query.get(id)
    return render_template('delete_users.html', u = u)

  if request.method == 'POST':
    u = User.query.get(id)
    db.session.delete(u)
    db.session.commit()
    return render_template('delete_success.html')