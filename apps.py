from flask import Flask, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "session"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:pg1960@127.0.0.1:7760//CRISPRTEdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ORM
db = SQLAlchemy(app)

class GRNA(db.Model):
    __tablename__ = 'grna'
    id = db.Column(db.Integer, primary_key=True)
    chr = db.Column(db.String(2))
    star = db.Column(db.Integer)
    ed = db.Column(db.Integer)
    seq = db.Column(db.String(20))
    ngg = db.Column(db.String(3))
    info = db.Column(db.VARCHAR(300))
    ont = db.Column(db.Integer)
    offt = db.Column(db.Integer)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/single')
def single():
    return render_template("single.html")


@app.route('/combination')
def combination():
    return render_template("combination.html")


@app.route('/result-single', methods=["POST"])
def result_single():
    # if request.method == "POST":
    item = request.form.get("item")
    print(item)
    if item includes 'dup':
        find = GRNA.query.filter(GRNA.info.contains(item)).limit(5).all()
        if find:
            return redirect(url_for("result_single_dup"), =find)
        else:
            return render_template("help.html")
    else:
        find = GRNA.query.filter(GRNA.info.contains(item)).limit(5).all()
        if find:
            return redirect(url_for("result_single_subclass"), =find)
        else:
            return render_template("help.html")
    # else:
    #     if "result_single" in session:
    #         return render_template("result-single.html", result=session.get("result_single"))
    #     else:
    #         return redirect(url_for("single"))

@app.route('/result-single-dup', methods=["POST"])
def result_single_dup(find):
    return render_template("result-single-dup.html")

@app.route('/result-single-subclass', methods=["POST"])
def result_single_subclass():
    return render_template("result-single-subclass.html")

@app.route('/result-combination', methods=["POST"])
def result_combination():
    # if request.method == "POST":
    item = request.form.get("item")
    print(item)
    find = GRNA.query.filter(GRNA.info.contains(item)).limit(5).all()
    session["result_combination"] = find
    if find:
        return render_template("result-combination.html", result=find)
    else:
        return render_template("help.html")
    # else:
    #     if "result_combination" in session:
    #         return render_template("result-combination.html", result=session.get("result_combination"))
    #     else:
    #         return redirect(url_for("combination"))

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/detail/<grna>')
def detail():
    return render_template("detail.html",grna=grna)

if __name__ == "__main__":
    app.run(debug=True)
