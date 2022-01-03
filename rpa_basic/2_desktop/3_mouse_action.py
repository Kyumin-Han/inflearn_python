import pyautogui
pyautogui.sleep(3)
# print(pyautogui.position())

# pyautogui.click(118, 5, duration=1) # 1초동안 (118, 5) 좌표로 이동 후 마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=2)

# pyautogui.rightClick() # 우클릭
# pyautogui.middleClick() # scroll

# pyautogui.moveTo()
# pyautogui.drag() # 현재 위치 기준으로 x, y만큼 드래그
# pyautogui.dragTo() # 절대 좌표 기준으로 x, y 만큼 드래그

pyautogui.scroll(-100) # 위 방향으로 300만큼 스크롤
# -300: 아래 방향으로 300만큼 스크롤