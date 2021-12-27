import tensorflow as tf
import tensorflow.compat.v1 as tf  #these two line are very important
tf.disable_v2_behavior()
import logging
'''this modual uses tensorflow to calculate the current gains'''

#logging.basicConfig(filename='calculations.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.warning('This will get logged to a file')
#logging.info('Admin logged in')
#logging.error('raised an error')

def getAmmountMade(buy, sold):
    '''this function subtracts the bought and sold price, then adds the current price'''
    bought = tf.Variable(buy, name="bought")#database query
    solds = tf.Variable(sold, name="sold")#database query
    newCurrent = (bought-sold)

    sess = tf.Session()
    sess.run(bought.initializer)
    sess.run(solds.initializer)
    result = sess.run(newCurrent)
    return result
