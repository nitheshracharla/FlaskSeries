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

@app.route('/demos')
def demo():
    return "Demosss!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4300,debug=True)