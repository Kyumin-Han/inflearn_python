from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480+600+250")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없다면 계속 위로 올라간다
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()