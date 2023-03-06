from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_cors import cross_origin
import os

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

    if submission == '992.6.8.1':
        flash("Success","info")
        return redirect(url_for("round2pre"))
    else:
        flash("Try Again!, you got this!","error")
        return redirect(url_for("display_round1"))
    
@app.route("/round2pre")
@cross_origin()
def round2pre():
    return render_template("page5.html")


@app.route("/round2")
@cross_origin()
def display_round2():
    return render_template("round2.html")

@app.route("/submitround2", methods=["POST"])
@cross_origin()
def submit_round2():
    submission = request.form['submission']

    if submission == 'pbueufmvducghopamv':
        flash("Success","info")
        return redirect(url_for("round3pre"))
    else:
        flash("Try Again!, you got this!","error")
        return redirect(url_for("display_round2"))
    
@app.route("/round3pre")
@cross_origin()
def round3pre():
    return render_template("page7.html")


@app.route("/round3")
@cross_origin()
def display_round3():
    return render_template("round3.html")

@app.route("/download")
@cross_origin()
def download():
    path_file = "../static/Archive.rar"
    # path_file = os.path.join(os.getcwd, path_file)
    filename = "Archive.rar"
    return send_file(path_file, as_attachment=True)


@app.route("/submitround3", methods=["POST"])
@cross_origin()
def submit_round3():
    submission = request.form['submission']

    if submission == '(0u9_D3_gRa{3_[YRU5':
        flash("Success","info")
        return redirect(url_for("round4pre"))
    else:
        flash("Try Again!, you got this!","error") 
        return redirect(url_for("display_round3"))
    
@app.route("/round4pre")
@cross_origin()
def round4pre():
    return render_template("page9.html")
    
@app.route("/round4")
@cross_origin()
def display_round4():
    return render_template("round4.html")

@app.route("/submitround4", methods=["POST"])
@cross_origin()
def submit_round4():
    submission = request.form['submission']

    if submission == r'flag{411_ur_37h_15_m1n3}':
        flash("Success","info")
        return redirect(url_for("success"))
    else:
        flash("Try Again!, you got this!","error") 
        return redirect(url_for("display_round4"))


@app.route('/success')
@cross_origin()
def success():
    return render_template("success.html")

@app.route("/bubyee")
@cross_origin()
def bubyee():
    return render_template("bye.html")


if __name__ == "__main__":
    app.run(debug = False, port = os.getenv("PORT", default = 5000))

