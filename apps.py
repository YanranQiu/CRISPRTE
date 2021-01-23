from flask import Flask, redirect, render_template, request, url_for, seession
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "session"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@127.0.0.1:3306/flasktest1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ORM
db = SQLAlchemy(app)

class GRNA(db.Model):
    __tablename__ = 'grna'
    id = db.Column(db.Integer, primary_key=True)
    chr = db.Column(db.Integer)
    star = db.Column(db.Integer)
    ed = db.Column(db.Integer)
    pam = db.Column(db.VARCHAR(30))
    ngg = db.Column(db.String(3))
    info = db.Column(db.VARCHAR(300))
    ont = db.Column(db.Integer)
    offt = db.Column(db.Integer)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/design')
def design():
    return render_template("design.html", values = User.query.all())


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
        if find is not None:
            return render_template("result.html", result=find)
        else:
            return render_template("notfound.html")
    else:
        if "result" in session:
            return render_template("result.html", result=find)
        else:
            return redirect(url_for("design"))



if __name__ == '__main__':
    app.run(debug=True)