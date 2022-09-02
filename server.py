from flask import Flask, render_template, request, redirect
from user import User
import time

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def users():
    userList = User.get_all()
    return render_template('/users.html', users=userList)

@app.route('/user/<int:userId>')
def show_user(userId):
    data = {'id': userId}
    user_data = User.get_user(data)
    return render_template('/user.html',user=user_data)

@app.route('/user/new')
def new_user():
    return render_template('/new.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        'fname': request.form.get('fname'),
        'lname': request.form.get('lname'),
        'email': request.form.get('email')
        } 
    User.add(data)
    return redirect('/users')

@app.route('/user/<int:userId>/edit')
def edit_user(userId):
    data = {'id' : userId}
    user_data = User.get_user(data)
    return render_template('/edit.html',user=user_data)

@app.route('/user/<int:userId>/update', methods=['POST'])
def update_user(userId):
    data = {
        'id': request.form.get('id'),
        'fname': request.form.get('fname'),
        'lname': request.form.get('lname'),
        'email': request.form.get('email')
    }
    User.update(data)
    return redirect(f'/user/{userId}')

@app.route('/user/<int:userId>/delete')
def delete_user(userId):
    data = {'id': userId}
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)