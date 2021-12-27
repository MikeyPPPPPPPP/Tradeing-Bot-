from os import times_result
from flask import Flask, render_template, request, redirect
from model import db, StockData, stockHistory, CurrentGains
from libs import testing, calculations
from libs.trade import machine
import logging
import sys

#logging.basicConfig(filename='app.log', filemode='r', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')
logger = logging.getLogger()
handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
#logger = logging.getLogger()

'''this is the main app where the pages will be handled'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_all():
    '''This function is vary important and is the bane of my existence'''
    db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    global logger
    # note that we set the 404 status explicitly
    logger.error('Error 404')
    return render_template('errors/404.html'), 404


@app.route('/', methods=['GET'])
def index():
    '''this page will return the currently monitored stock, gains, and history'''
    try:
        currentStockId = [x for x in StockData.query.all()][0]
        StockInfo = StockData.query.filter_by(id=currentStockId.id)
        logging.warning(f'Returning Info On A Stock')

        StockHistory = StockData.query.all()

        currentGainss = [x for x in CurrentGains.query.all()][0]
        showGains = CurrentGains.query.filter_by(id=currentGainss.id)

        return render_template('home.html', values=StockInfo, history=StockHistory, am=showGains)
    except IndexError:
        logging.warning(f'Database May Be Empty')
        return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    '''This page will add a stock the the current page and put the current stock in the histoy'''
    if request.method == 'POST':
        stock = request.form.get('Stock')
        buyAt = int(request.form.get('buyAt'))
        sellAt = int(request.form.get('sellAt'))
        try:
            machine.Buy(stock.upper())
        except:
            logger.critical('Stock not bought')
            pass

        current = 0
        try:
            for x in CurrentGains.query.all():
                current = x.price
        except:
            logging.warning(f'Database May Be Empty')
            pass
        gains = calculations.getAmmountMade(buyAt, sellAt)
        newGains = CurrentGains(price=abs(gains+current))
        print(gains+current)
        newStockretreved = StockData(stock=stock, buyPrice=buyAt, sellPrice=sellAt)
        db.session.add(newGains)
        db.session.add(newStockretreved)
        db.session.commit()
        logging.warning(f'New Stock {stock} Added')
        logging.warning(f'New gains {gains}')
        return redirect('/')

    return render_template('add.html')


if __name__ == '__main__':
    try:
        app.run()#host='0.0.0.0')
    except Exception as e:
        logger.error(f'Caught Exception: line: {sys.exc_info()[2].tb_lineno} {sys.exc_info()[0]} {sys.exc_info()[1]}')
        exit()
