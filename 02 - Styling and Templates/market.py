from flask import Flask, render_template
app = Flask(__name__)
#  demo
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/demo')
def demo():
    return "Demo!"