import flask 
from login import*

app = flask.Flask(__name__)
# app.run(host="0.0.0.0",port=80)
@app.route('/', methods=['GET', 'POST'])

def index():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['pwd']
        print(username, password)
        if login(username, password):
            # return flask.render_template('home.html')
            return flask.redirect(flask.url_for('home'))
        else:
            return flask.render_template('signup.html')
    else:
        return flask.render_template('index.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'GET /home.html':
        return flask.render_template('home.html')
    return flask.render_template('home.html')

@app.route('/denv', methods=['GET', 'POST'])
def denv():
    return flask.render_template('denv.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80, debug=False)

