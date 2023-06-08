from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route("/certifications")
def certificates():
    return render_template("certifications.html")

@app.route('/projects')
def projects():
    return render_template("portfolio.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/contact')
def contact():
    return render_template('footer.html')

if __name__ == "__main__":
    freezer.freeze()