from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def users():
    userList = User.get_all()
    return render_template('/users.html', users=userList)

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

if __name__ == "__main__":
    app.run(debug=True)