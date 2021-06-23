from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'this is a secret key'


@app.route('/')
def index():
    sumSessionCounter()
    return render_template('index.html')

def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1



@app.route('/destroy_session')
def destroy():
    session.clear()	
    return render_template('index.html')


if __name__=="__main__":   
        app.run(debug=True)    