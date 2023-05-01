from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route('/')
def start():
    return redirect('/friendships')

@app.route('/friendships')
def index():
    all_friendships = user.User.show_all_friendships()
    all_users = user.User.show_all_users()
    return render_template('index.html', users=all_users, friendships=all_friendships)

@app.route('/users/add', methods=['POST'])
def add_new_user():
    user.User.add_user(request.form)
    return redirect ('/')

@app.route('/users')
def show_users():
    users = user.User.show_all_friendships()
    return render_template('users.html', all_users=users)

@app.route('/users/new/friendship', methods=['POST'])
def create_friendship():
    friendships = user.User.show_friendship_ids()
    
    for data in friendships:
        # print(request.form['user_id'], data['user_id'], int(request.form['user_id']) == int(data['user_id']))
        if int(request.form['user_id']) == int(data['user_id']) and int(request.form['friend_id']) == int(data['friend_id']):
            session['error_msg'] = 'Friendship already exists!'
            return redirect('/')
    session['error_msg'] = ''
    user.User.new_friendship(request.form)
    return redirect('/')
