import subprocess
import time

def install(package):
    subprocess.call(['pip','install',package])

install('pandas')
install('numpy')
install('matplotlib')
install('tensorflow')
install('opencv-python')
install('seaborn')
install('pytesseract')


time.sleep(1)
subprocess.call('start',shell=True)
