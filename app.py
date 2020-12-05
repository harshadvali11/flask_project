from flask import Flask,render_template,request

from flask_wtf import Form

from wtforms import StringField,SubmitField

from wtforms.validators import Required

app=Flask(__name__)

app.config['SECRET_KEY']='encryption'


@app.route('/function1/')
def function1():
    return 'hai Falsk Project'

@app.route('/template/')
def template():
    return render_template('first.html',name='Flask')

@app.route('/wish/<name>')
def wish(name):
    return 'hai hello how are U MR/MS {}'.format(name)


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        form_data=request.form
        return form_data['username']

    return render_template('form.html')


class NameForm(Form):
    name=StringField('Enter name',validators=[Required()])
    submit=SubmitField()

@app.route('/webform',methods=['GET',"POST"])
def webform():
    form=NameForm()
    if form.validate_on_submit():
        return form.data['name']
    return render_template('webform.html',form=form)













if __name__ == "__main__":
    
    app.run(debug=True,host='192.168.56.1',port=5001)