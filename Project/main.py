from flask import Flask, redirect, url_for, render_template
from functionCall import *
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/battingstats")
def batstats():
    return render_template("battingstats.html", content1=predictedBat())

@app.route("/bowlingstats")
def bowlstats():
    return render_template("bowlingstats.html", content2=predictedBall())

@app.route("/allroundstats")
def allroundstats():
    return render_template("allroundstats.html", content3=predictedAllRound())

@app.route("/battingtop")
def battop():
    return render_template("battingtop.html", content4=topBat())

@app.route("/bowlingtop")
def bowltop():
    return render_template("bowlingtop.html", content5=topBall())

@app.route("/allroundtop")
def allroundtop():
    return render_template("allroundtop.html", content6=topAllRound())

if __name__ ==  '__main__':
    app.run(debug=True)