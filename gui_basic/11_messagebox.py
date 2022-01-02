from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("First GUI")
root.geometry("640x480+600+250")

# 기차 예매 시스템의 메세지
def info():
    msgbox.showinfo("알림", "예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 노선은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제오류가 발생하였습니다.")
    
def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아 동반석입니다. 예매 하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1: # 재시도
        print("재시도")
    elif response == 0:
        print("취소")
def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향 좌석입니다. 예매 하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장되지 않았습니다. 저장 후 종료하시겠습니까?")
    # 예 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소
    print("응답:", response) # True, False, None -> 예 : 1, 아니오 : 0, 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()


Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()