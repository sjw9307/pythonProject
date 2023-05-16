import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='간단한 Python UI 프로그램 예제')
        self.panel = wx.Panel(self)

        self.ok_button = wx.Button(self.panel, label='OK')
        self.cancel_button = wx.Button(self.panel, label='Cancel')

        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.ok_button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.cancel_button, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(sizer)
        self.Show()

    def on_ok(self, event):
        print("OK 버튼을 눌렀습니다.")

    def on_cancel(self, event):
        self.Close()

 if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
