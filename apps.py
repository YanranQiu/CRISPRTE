from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '19999900'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/flasktest1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ORM
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role:%s>" % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))

    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return "<User:%s,%s,%s,%s>" % (self.id, self.name, self.email, self.password)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/design')
def design():
    return render_template("design.html", values = User.query.all())


@app.route('/target')
def target():
    return render_template("target.html")


@app.route('/result', methods=["GET", "POST"])
def result():
    item = request.form.get("item")
    print(item)
    find = User.query.filter(User.name == item).all()
    if find is not None:
        #print(find.email)
        return render_template("result.html", result=find)
    else:
        return render_template("notfound.html")


if __name__ == '__main__':
    app.run(debug=True)
