from tkinter import *
# 이벤트 처리 함수를 정의한다.
def process():
    tf = float(e1.get())
    tc = (tf) * 1200.0

    e2.delete(0, END)
    e2.insert(0, str(tc))

# e1에서 문자열을 읽어서 부동소수점형으로 변경 # 화씨 온도를 섭씨 온도로 변환한다.
# 처음부터 끝까지 지운다.
# tc 변수의 값을 문자열로 변환하여 추가한다.
window = Tk()

Label(window, text="한화").grid(row=0, column=0)
Label(window, text="미화").grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text="한화->미화", command=process).grid(row=2, column=1)
window.mainloop()