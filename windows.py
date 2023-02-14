import win32gui
import win32con


class Windows:
    def __init__(self, cls, name):
        self.cls = cls
        self.name = name

    def top(self):
        # 查找子窗口，返回值为0表示未找到子窗口  "Qt5QWindowIcon", u"约战竞技场-游戏(活跃)"
        hwnd = win32gui.FindWindow(self.cls, self.name)
        # hwnd = win32gui.FindWindow("Notepad", u"无标题 - 记事本")
        if hwnd:
            if win32gui.IsIconic(hwnd):
                win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
            else:
                # win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)
                win32gui.SetForegroundWindow(hwnd)
        else:
            raise Exception("未打开窗口！")
