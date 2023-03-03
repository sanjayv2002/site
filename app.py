from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import cross_origin

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
@cross_origin()
def home():  
    return render_template("index.html")

@app.route("/loading")
@cross_origin()
def loading():

    return render_template("loading.html")

@app.route("/assistant")
@cross_origin()
def assistant():

    return render_template("assistant.html")

@app.route("/intro")
@cross_origin()
def intro():
    return render_template("intro.html")


@app.route("/round1")
@cross_origin()
def display_round1():
    return render_template("round1.html")

@app.route("/submitround1", methods=["POST"])
@cross_origin()
def submit_round1():
    submission = request.form['submission']

    if submission == 'DUMmy':
        flash("Success","info")
        return redirect(url_for("display_round2"))
    else:
        flash("Try Again!, you got this!","error")
        return redirect(url_for("display_round1"))

@app.route("/round2")
@cross_origin()
def display_round2():
    return render_template("round2.html")

@app.route("/submitround2", methods=["POST"])
@cross_origin()
def submit_round2():
    submission = request.form['submission']

    if submission == 'DUMmy':
        flash("Success","info")
        return redirect(url_for("display_round3"))
    else:
        flash("Try Again!, you got this!","error")
        return redirect(url_for("display_round2"))
    
@app.route("/round3")
@cross_origin()
def display_round3():
    return render_template("round3.html")

@app.route("/submitround3", methods=["POST"])
@cross_origin()
def submit_round3():
    submission = request.form['submission']

    if submission == 'DUMmy':
        flash("Success","info")
        return redirect(url_for("display_round4"))
    else:
        flash("Try Again!, you got this!","error") 
        return redirect(url_for("display_round3"))
    
@app.route("/round4")
@cross_origin()
def display_round4():
    return render_template("round4.html")

@app.route("/submitround4", methods=["POST"])
@cross_origin()
def submit_round4():
    submission = request.form['submission']

    if submission == 'DUMmy':
        flash("Success","info")
        return redirect(url_for("success"))
    else:
        flash("Try Again!, you got this!","error") 
        return redirect(url_for("display_round4"))


@app.route('/success')
@cross_origin()
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)

