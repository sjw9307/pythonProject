# 필요한 모듈들을 임포트합니다.
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser
import datetime

def save_memo():
    # 사용자가 입력한 메모를 가져옵니다. '1.0'은 텍스트 위젯의 시작 위치를, 'end-1c'는 텍스트의 끝 위치를 나타냅니다.
    memo = text_input.get("1.0", 'end-1c')

    # 현재 날짜와 시간을 가져오고, 이를 문자열로 변환하여 파일명과 파일 내용에 사용할 날짜 문자열을 만듭니다.
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d%H%M%S.txt")
    date_string = now.strftime("%Y년 %m월%d일 – %H:%M")

    # 메모를 파일에 저장합니다. 파일 이름은 현재 날짜와 시간으로 설정하였습니다.
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'<{filename} 파일 내용>\n\n{date_string}\n{memo}')

    # 메모 저장이 완료되면 메시지 박스를 통해 사용자에게 알립니다.
    messagebox.showinfo("메모 저장", f"'{filename}'에 메모를 저장하였습니다.")

def load_memo():
    # 비밀번호 입력창을 표시하고 입력값을 가져옵니다. 입력된 비밀번호가 올바른지 확인합니다.
    password = simpledialog.askstring("비밀번호 입력", "비밀번호를 입력하세요:", show='*')
    if password == 'pythonlove':
        # 파일 선택 대화상자를 열고 사용자가 선택한 파일의 내용을 가져옵니다.
        filename = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        text_input.delete('1.0', tk.END)
        text_input.insert('1.0', content)
    else:
        # 비밀번호가 틀렸을 경우 메시지 박스를 통해 사용자에게 알립니다.
        messagebox.showinfo("비밀번호 오류", "비밀번호가 일치하지 않습니다.")

def change_color():
    # 색상 선택 대화상자를 열고 사용자가 선택한 색상을 가져옵니다. 텍스트 위젯의 전경색을 선택된 색상으로 변경합니다.
    color = colorchooser.askcolor()[1]
    text_input.config(fg=color)

def find_text():
    # 사용자가 찾을 텍스트를 입력하도록 합니다.
    target = simpledialog.askstring("텍스트 찾기", "찾을 텍스트를 입력하세요:")
    if target:
        # 텍스트 위젯에서 해당 텍스트를 찾습니다.
        where = text_input.search(target, '1.0', stopindex=tk.END)
        if where:
            # 찾은 텍스트를 노란색으로 강조합니다.
            text_input.tag_add('highlight', where, f"{where}+{len(target)}c")
            text_input.tag_config('highlight', background='yellow')
        else:
            # 찾는 텍스트가 없을 경우 메시지 박스를 통해 사용자에게 알립니다.
            messagebox.showinfo("텍스트 찾기", f"'{target}'를 찾을 수 없습니다.")

# Tk 객체를 생성하고, 창의 제목을 설정합니다.
window = tk.Tk()
window.title("메모장")

# Text 위젯을 생성하고, 그리드 레이아웃의 0행 0열부터 4열까지 차지하도록 설정합니다.
text_input = tk.Text(window)
text_input.grid(row=0, column=0, columnspan=4)

# 각 버튼을 생성하고, 그리드 레이아웃의 1행에 차례로 배치합니다. 각 버튼에는 해당 기능을 수행하는 함수를 연결합니다.
save_button = tk.Button(window, text="저장", command=save_memo)
save_button.grid(row=1, column=0)

load_button = tk.Button(window, text="불러오기", command=load_memo)
load_button.grid(row=1, column=1)

color_button = tk.Button(window, text="색상 선택", command=change_color)
color_button.grid(row=1, column=2)

find_button = tk.Button(window, text="텍스트 찾기", command=find_text)
find_button.grid(row=1, column=3)

# Tk 객체의 메인 루프를 시작합니다. 이는 사용자가 창을 닫을 때까지 프로그램을 실행하게 합니다.
window.mainloop()
