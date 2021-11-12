import ctypes
from ctypes import wintypes as w
import win32gui
import win32con
import win32api
import pyautogui

user32 = ctypes.WinDLL('user32')
user32.GetForegroundWindow.argtypes = ()
user32.GetForegroundWindow.restype = w.HWND
user32.ShowWindow.argtypes = w.HWND,w.BOOL
user32.ShowWindow.restype = w.BOOL

# From https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow
SW_MAXIMIZE = 3
SW_MINIMIZE = 6

hWnd = ctypes.windll.user32.FindWindowW(0, "エクスプローラー")
user32.ShowWindow(hWnd, SW_MAXIMIZE)
win32gui.SetWindowPos(hWnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
left, top, right, bottom = win32gui.GetWindowRect(hWnd)
pyautogui.moveTo(left+60, top + 10)
pyautogui.click()