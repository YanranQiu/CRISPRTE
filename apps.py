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


@app.route('/design')
def design():
    return render_template("design.html")


@app.route('/target')
def target():
    return render_template("target.html")


@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == "POST":
        item = request.form.get("item")
        print(item)
        find = User.query.filter(User.name == item).all()
        session["result"] = find
        if find:
            return render_template("result.html", result=find)
        else:
            return render_template("notfound.html")
    else:
        if "result" in session:
            return render_template("result.html", result=find)
        else:
            return redirect(url_for("design"))

#@app.route('/detail')
#def detail():

if __name__ == "__main__":
    app.run(debug=True)
