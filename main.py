import flask 
from login import*
from services.denv_back_end import*


app = flask.Flask(__name__)
# app.run(host="0.0.0.0",port=80)
app.secret_key = 'any_random_string'
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

@app.route('/use_denv', methods=['GET','POST'])
def use_denv():
    if flask.request.method == 'POST':
        date_onset = str(flask.request.form['Date_onset'])
        verify_val = {0:flask.request.form['nm'],1:flask.request.form['Counta'],2:flask.request.form['Count_b'],3:flask.request.form['Age'],4:0,5:flask.request.form['Date_a'],6:flask.request.form['Date_b']}
        denv_result = estimate(verify_val)
        lc = denv_result[3]
        level = np.min(lc)
        advice = advise(level)
        hc = denv_result[2]
        confidence = denv_result[4]
        name = str(verify_val[0])
        age = str(verify_val[3])
        return flask.render_template('result_denv.html',Name = name, Age = age, Date_onset = date_onset,LC1 = str(lc[0]),LC2 = str(lc[1]),LC3 = str(lc[2]),LC4 = str(lc[3]),LC5 = str(lc[4]),LC6 = str(lc[5]),LC7 = str(lc[6]),LC8 = str(lc[7]),LC9 = str(lc[8]),LC10 = str(lc[9]),LC11 = str(lc[10]),HC1 = str(hc[0]),HC2 = str(hc[1]),HC3 = str(hc[2]),HC4 = str(hc[3]),HC5 = str(hc[4]),HC6 = str(hc[5]),HC7 = str(hc[6]),HC8 = str(hc[7]),HC9 = str(hc[8]),HC10 = str(hc[9]),HC11 = str(hc[10]),Confidence = str(confidence),Advice = advice)
        
    return flask.render_template('use_denv.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host = "0.0.0.0",port=80,debug=True)
