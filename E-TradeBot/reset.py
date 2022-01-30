import subprocess
import time

'''disregard this, turns out I was pressing control x instead of control c'''

def reset():
    '''this will kill the app.py program so we don need to do it manually every time'''
    proc = []
    kill = ''
    out = subprocess.Popen(['ps'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(.5)
    stdout,stderr = out.communicate()
    proc = list(stdout.decode().split('\n'))

    for x in proc:
        if 'app.py' in x:
            kill = x.split(' ')[0]
    subprocess.Popen(['kill',kill])
    


reset()
