from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480+650+250") # 가로 * 세로 크기 지정 + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()