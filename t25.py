import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import datetime


def save_memo():
    # 사용자로부터 메모를 입력 받습니다.
    memo = text_input.get("1.0", 'end-1c')

    # 현재 날짜와 시간을 문자열로 변환합니다.
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d%H%M%S.txt")
    date_string = now.strftime("%Y년 %m월%d일 – %H:%M")

    # 파일을 쓰기 모드로 열고 메모를 저장합니다.
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'<{filename} 파일 내용>\n\n{date_string}\n{memo}')

    # 메모 저장 완료 메시지 박스를 출력합니다.
    messagebox.showinfo("메모 저장", f"'{filename}'에 메모를 저장하였습니다.")


def load_memo():
    # 사용자로부터 비밀번호를 입력 받습니다.
    password = simpledialog.askstring("Password-required", "Enter password:", show='*')

    # 비밀번호가 일치하는지 확인합니다.
    if password == 'pythonlove':
        # 파일 선택 다이얼로그를 열어 사용자가 파일을 선택하도록 합니다.
        filename = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

        # 선택한 파일을 읽습니다.
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # 텍스트 영역에 파일 내용을 출력합니다.
        text_input.delete('1.0', tk.END)
        text_input.insert('1.0', content)
    else:
        messagebox.showinfo("비밀번호 오류", "비밀번호가 일치하지 않습니다.")


window = tk.Tk()
window.title("메모장")

text_input = tk.Text(window)
text_input.grid(row=0, column=0, columnspan=2)

save_button = tk.Button(window, text="저장", command=save_memo)
save_button.grid(row=1, column=0)

load_button = tk.Button(window, text="불러오기", command=load_memo)
load_button.grid(row=1, column=1)

window.mainloop()