from tkinter import *
import os

root = Tk()
root.title("First GUI")
root.geometry("640x480+600+250")
root.title("제목 없음 - Windows 메모장")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 메모 입력
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

def opentxt():
    if os.path.isfile("mynote.txt"):
        with open("mynote.txt", "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())


def storetxt():
    store_file = open("mynote.txt", "w", encoding="utf8")
    store_file.write(txt.get("1.0", END))
    store_file.close()

menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=opentxt)
menu_file.add_command(label="저장", command=storetxt)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집 메뉴
menu.add_cascade(label="편집")

# 서식 메뉴
menu.add_cascade(label="서식")

# 보기 메뉴
menu.add_cascade(label="보기")

# 도움말 메뉴
menu.add_cascade(label="도움말")

root.config(menu=menu)
root.mainloop()