from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("First GUI")
root.geometry("640x480+600+250")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(5) # 10ms마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 실수형으로 저장
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100 까지
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # GUI 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()