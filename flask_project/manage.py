from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def welcome_page():
    return render_template('welcome.htm')

@app.route('/greetings/')
def greetings():
    return render_template('greetings.htm')

@app.route('/greetings/christmas/')
def christmas():
    return render_template('christmas.htm')

@app.route('/greetings/newyear/')
def new_years():
    return render_template('new_year.htm')

if __name__ == '__main__':
    app.run(debug = True)
