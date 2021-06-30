import pyautogui as pg
import time
from datetime import datetime

pg.hotkey('winleft')
time.sleep(1)
pg.typewrite('word\n',0.5)
time.sleep(2.5)
pg.hotkey('winleft','up')
pg.hotkey('enter')
pg.typewrite('This is auto writing test from pyautogui PYTHON\n',0.3)
pg.hotkey('ctrl','s')
pg.moveTo(213,400,0.5)
pg.click()
now = datetime.now()
filename = 'Autopython_' + now.strftime("%d_%m_%Y %H_%M_%S")
pg.typewrite(filename)
pg.moveTo(994,664,0.5)
pg.click()
time.sleep(3)
pg.hotkey('altleft','space', 'c')