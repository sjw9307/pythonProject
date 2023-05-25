import tkinter as tk
from tkinter import *
import datetime

# 저장 버튼 클릭 시 실행되는 함수
def save_memo():
    # 사용자로부터 메모를 입력 받습니다.
    memo = text_input.get("1.0", 'end-1c')

    # 현재 날짜와 시간을 문자열로 변환합니다.
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d%H%M%S.txt")
    date_string = now.strftime("%Y년 %m월%d일 – %H:%M")

    # 파일을 쓰기 모드로 열고 메모를 저장합니다.
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(date_string + "\n" + memo)

    # 메모 저장 완료 메시지 박스를 출력합니다.
    messagebox.showinfo("메모 저장", f"'{filename}'에 메모를 저장하였습니다.")

# 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")

# 텍스트 입력 영역 생성
text_input = tk.Text(window)
text_input.pack()

# 저장 버튼 생성
save_button = tk.Button(window, text="저장", command=save_memo)
save_button.pack()

# 메인 윈도우 실행
window.mainloop()
