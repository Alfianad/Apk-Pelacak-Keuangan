from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    description = db.Column(db.String(200))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def summary():
    income = db.session.query(db.func.sum(Transaction.amount)).filter_by(type='income').scalar() or 0
    expense = db.session.query(db.func.sum(Transaction.amount)).filter_by(type='expense').scalar() or 0
    balance = income - expense

    income_transactions = Transaction.query.filter_by(type='income').all()
    expense_transactions = Transaction.query.filter_by(type='expense').all()

    return render_template('summary.html', income=income, expense=expense, balance=balance,
                           income_transactions=income_transactions, expense_transactions=expense_transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    type = request.form['type']
    category = request.form['category']
    amount = float(request.form['amount'])
    description = request.form['description']
    new_transaction = Transaction(type=type, category=category, amount=amount, description=description)
    db.session.add(new_transaction)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)