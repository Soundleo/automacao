# impotaçãchrome
# o da biblioteca 
import pyautogui as auto
import time

# define tempo de espera para cada comando auto
auto.PAUSE = 0.5

# abre o menu iniciar

# abre o edge
auto.hotkey('win')
auto.write('chrome')
auto.press('enter')
auto.hotkey('alt', 'space')
auto.press('x')
auto.press('enter')
time.sleep(1)
auto.write('github.com')
auto.press('enter')
auto.hotkey('ctrl', 't')
time.sleep(1)
auto.write('classroom.google.com')
auto.press('enter')
auto.hotkey('win', 'r')
auto.write('shutdown -s')
auto.press('enter')

