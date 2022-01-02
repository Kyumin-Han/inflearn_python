import keyboard
from PIL import ImageGrab
import time

def screenshot():
    #현재 시간을 받아온다
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot) # F9키를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 때 까지 프로그램 수행