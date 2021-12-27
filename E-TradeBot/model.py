from flask_sqlalchemy import SQLAlchemy
'''This is the model for the (relational) database'''
db = SQLAlchemy()

class StockData(db.Model):
    '''
    This is the init of a new stock

    id -> int
    stock -> string
    buy price -> int
    sell price -> int
    '''
    __tablename__ = 'stockData'
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(10), unique=True)
    buyPrice = db.Column(db.Integer)
    sellPrice = db.Column(db.Integer)
    history = db.relationship('stockHistory', backref='owner', lazy='dynamic') 

class stockHistory(db.Model):
    '''this will hold the history of the price of the stock
    
    id -> int
    date -> String
    price -> string
    '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    price = db.Column(db.String(10))
    owner_id = db.Column(db.Integer, db.ForeignKey('stockData.id'))

class CurrentGains(db.Model):
    '''
    This will be for the gains
    id -> int
    currentPrice -> int
    '''
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

