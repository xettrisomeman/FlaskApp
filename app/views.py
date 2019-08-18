from flask import render_template,request , redirect , url_for , flash
from app import app
from app.forms import NameForm
from app.models import Name ,db
from flask_login import login_required





@app.route('/')
def home():
    names = Name.query.all()
    total_users = len(names)
    return render_template('home.htm' , names=names , total=total_users)



@app.route('/form' , methods=['GET', 'POST'])
@login_required
def form():
    form= NameForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['name']
            surname = request.form['surname']
            age = request.form['age'] 
            user = Name(name = name , surname=surname , age=age)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('nameform.htm' , form=form)





@app.route('/deleteform/<int:id>' , methods=['GET' , 'POST'])
@login_required
def deleteform(id):
    query = Name.query.get(id)
    if request.method == 'POST':
        db.session.delete(query)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('deleteform.htm' , data=query)





@app.route('/detailform/<int:id>')
@login_required
def detailform(id):
    query= Name.query.get(id)
    return render_template('detailform.htm' , data=query)



@app.route("/updateform/<int:id>", methods=["GET","POST"])
def updateform(id):
    query = Name.query.get(id)
    if query:
        form = NameForm(request.form,obj=query)
        if request.method == 'POST' and form.validate_on_submit:
            name = request.form['name']
            surname = request.form['surname']
            age = request.form['age']
            query.name = name
            query.surname = surname
            query.age = age
            db.session.add(query)
            db.session.commit()
            flash('Name updated successfully')
            return redirect(url_for('home'))
    return render_template('updateform.htm', form=form)

