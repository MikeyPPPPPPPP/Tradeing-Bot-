import logging

#logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')



def DBisEmpty(databaseToTest) -> str:
    if len(databaseToTest.query.all()) == 0:
        return f'{databaseToTest} is Empty'
    return f'{databaseToTest} is Not Empty'
    

