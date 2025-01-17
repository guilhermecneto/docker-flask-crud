'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''
# Adicionar Tracing
from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database

# Adicionar tracing
app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

# Adicionar LOG
#Adicionar tracing
@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/')
#Adicionar Traccing
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
# Four Golden Signal por endpoint
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")
#Adicionar Tracing/*
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
# Four Golden Signal por endpoint
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)
        #Adicionar Tracing/*

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    # Four Golden Signal por endpoint
    if request.method == 'POST' and request.form['update']:
        # Adicionar LOG
        #Adicionar Tracing/*
        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
# Four Golden Signal por endpoint
def delete(id):
    data = db.read(id);
    #Adicionar LOG
    #Adicionar Tracing/*
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
# Four Golden Signal por endpoint
def deletephone():
    if request.method == 'POST' and request.form['delete']:
#Adicionar Tracing/*
        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted')
#Adicionar Tracing/*
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
# Four Golden Signal por endpoint
def page_not_found(error):
    return render_template('error.html')
#Adicionar LOG
if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
