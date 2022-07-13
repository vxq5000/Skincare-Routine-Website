from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.models.product import Product
from flask_app.models.user import User

@app.route('/post/routine', methods=['POST'])
def add():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Product.is_valid(request.form):
        return redirect ('/routine/new')
    data={
        "time_of_day":request.form["time_of_day"],
        "cleanser":request.form["cleanser"],
        "serum":request.form["serum"],
        "moisturizer":request.form["moisturizer"],
        "treatment":request.form["treatment"],
        "user_id":session["user_id"]        
    }
    Product.save(data)
    return redirect ('/home')

@app.route('/routine/new')
def create():
    if 'user_id' not in session:
        return redirect ('/')
    data={
        "id":session['user_id']
    }
    return render_template('add.html', user=User.get_by_id(data))

@app.route('/routine/edit/<int:id>')
def editroutine(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        "id":id
    }
    user_data={
        "id":session['user_id']
    }
    return render_template("edit.html",user=User.get_by_id(user_data), product=Product.get_one(data))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Product.is_valid(request.form):
        return redirect ('/home')
    data={
        "time_of_day":request.form["time_of_day"],
        "cleanser":request.form["cleanser"],
        "serum":request.form["serum"],
        "moisturizer":request.form["moisturizer"],
        "treatment":request.form["treatment"],
        "id":id
    }
    Product.update(data)
    return redirect ('/home')

@app.route('/destroy/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Product.delete(data)
    return redirect('/home')