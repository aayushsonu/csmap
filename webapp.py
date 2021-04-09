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
    title=db.Column(db.String(200),nullable=False)
    content=db.Column(db.String(1000),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sid}/{self.title}"


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


@app.route('/contact')
def contact():
    allQuery=MainCSMAP.query.all()
    return render_template('contact.html',allQuery=allQuery)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)