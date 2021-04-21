from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from modules import CaeserCipher as cc


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///csmapMain.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# Initialize database
db=SQLAlchemy(app)

# Create db model
class MainCSMAP(db.Model):
    sid=db.Column(db.Integer,primary_key=True)
    sname=db.Column(db.String(50),nullable=False)
    semail=db.Column(db.String(75),nullable=False)
    comment=db.Column(db.String(200))
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sname}/{self.semail},{self.comment}"


# database
# maincsmap=MainCSMAP(title="",content=data)
# db.session.add(maincsmap)
# db.session.commit()
# print(allQuery)

# Web application end points
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/portScanner')
def portScanner():
    return render_template('portScanner.html')


@app.route('/arpSpoofer')
def arpSpoofer():
    return render_template('arpSpoofer.html')


@app.route('/macSpoofer')
def macSpoofer():
    return render_template('macSpoofer.html')


@app.route('/passGenerator')
def passGenerator():
    return render_template('passGenerator.html')


@app.route('/caesercipher')
def caesercipher():
    return render_template('caesercipher.html')

@app.route('/caesercipher/<endpoint>',methods=['GET','POST'])
def ccEncrypt(endpoint):
    if request.method=='GET':
        if endpoint=='encrypt':
            return render_template('ccCrypto.html',endpoint=endpoint)
        elif endpoint=='decrypt':
            return render_template('ccCrypto.html',endpoint=endpoint)
        else:
            return render_template('caesercipher.html')
    if request.method=='POST':
        text=request.form.get("text")
        key=request.form.get("key")
        c=cc(text,key)
        if endpoint=='encrypt':
            result=c.encrypt()
        elif endpoint=='decrypt':
            result=c.decrypt()
        else:
            return render_template('caesercipher.html')
        return render_template('ccCrypto.html',result={'result':result,'text':text,'key':key},endpoint=endpoint)
    return render_template('ccCrypto.html',endpoint=endpoint)


@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='GET':
        return render_template('contact.html')
    elif request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        comment=request.form.get('comment')
        maincsmap=MainCSMAP(sname=name,semail=email,comment=comment)
        db.session.add(maincsmap)
        db.session.commit()
        return render_template('contact.html')
        # allQuery=MainCSMAP.query.all()
        # print(allQuery)



@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)