import pyautogui as pg
import time

pg.hotkey('winleft')
time.sleep(2)
pg.typewrite('chrome\n',0.5)
pg.typewrite('www.youtube.com\n',0.2)
pg.hotkey('winleft','up')
pg.hotkey('ctrl','t')