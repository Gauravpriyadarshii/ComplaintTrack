#app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_superuser = db.Column(db.Boolean, default=False)

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(36), unique=True, nullable=False)
    complaint_text = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complaint', methods=['POST'])
def register_complaint():
    complaint_text = request.form['complaint']
    token = str(uuid.uuid4())
    new_complaint = Complaint(token=token, complaint_text=complaint_text)
    db.session.add(new_complaint)
    db.session.commit()
    return redirect(url_for('complaint_status', token=token))

@app.route('/complaint/<token>')
def complaint_status(token):
    complaint = Complaint.query.filter_by(token=token).first()
    if complaint:
        return render_template('status.html', complaint=complaint)
    else:
        return "Complaint not found"

@app.route('/check_status')
def check_status():
    return render_template('check_status.html')

@app.route('/check_complaint_status', methods=['POST'])
def check_complaint_status():
    token = request.form.get('token')
    complaint = Complaint.query.filter_by(token=token).first()
    if complaint:
        return render_template('complaint_status.html', complaint=complaint)
    else:
        return "Complaint not found"

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user and user.is_superuser:
            complaints = Complaint.query.all()
            return render_template('admin_panel.html', complaints=complaints)
    return render_template('admin_login.html', message="Invalid credentials")

@app.route('/admin/action/<token>/<action>')
def admin_action(token, action):
    complaint = Complaint.query.filter_by(token=token).first()
    if complaint:
        complaint.status = action
        db.session.commit()
        return redirect(url_for('admin_panel'))
    return "Complaint not found"

@app.route('/create_superuser')
def create_superuser():
    existing_superuser = User.query.filter_by(username='admin').first()
    if existing_superuser:
        return "Superuser already exists."
    else:
        superuser = User(username="admin", password="password", email="admin@example.com", is_superuser=True)
        db.session.add(superuser)
        db.session.commit()
        return "Superuser created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
