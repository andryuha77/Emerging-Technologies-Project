# adapted from : http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
from flask import render_template
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

#Main method.
if __name__ == "__main__":  
    #Run the app.
    app.run()