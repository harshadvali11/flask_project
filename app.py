from flask import Flask,render_template

app=Flask(__name__)


@app.route('/function1/')
def function1():
    return 'hai Falsk Project'

@app.route('/template/')
def template():
    return render_template('first.html',name='Flask')

@app.route('/wish/<name>')
def wish(name):
    return 'hai hello how are U MR/MS {}'.format(name)


if __name__ == "__main__":
    
    app.run(debug=True,host='192.168.56.1',port=5001)