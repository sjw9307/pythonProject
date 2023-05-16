import PySimpleGUI as sg

# 창 레이아웃 정의
layout = [
    [sg.Text("간단한 Python UI 프로그램 예제")],
    [sg.Button("OK")],
    [sg.Button("Cancel")],
]

# 창 생성
window = sg.Window("Python UI 프로그램", layout)

# 이벤트 루프
while True:
    event, values = window.read()

    # 창을 닫거나 "Cancel" 버튼을 누를 때 종료
    if event == sg.WIN_CLOSED or event == "Cancel":
        break

# 창 닫기
window.close()
