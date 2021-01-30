# -*- coding:utf-8 -*-
# @Time: 2021/1/30 11:40
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: autocomp.py
import time
from qtpy.QtCore import QThread, Signal


class AutoCompThread(QThread):
    '''
    当一段时间没有补全需求之后，后台自动补全线程会进入休眠模式。下一次补全请求则会唤醒该后台线程。
    '''
    trigger = Signal(tuple, list)

    def __init__(self):
        super(AutoCompThread, self).__init__()
        self.text = ''
        self.text_cursor_pos = (0, 1)
        self.activated = True
        self.stop_flag = False

    def run(self):
        text = ''
        last_complete_time = time.time()
        try:
            import jedi
        except ImportError:
            print('Jedi not installed.install jedi for better auto-completion!')
            return
        while (1):
            if self.stop_flag:
                return
            pos = self.text_cursor_pos

            if self.text == text:
                if time.time() - last_complete_time >= 30:
                    self.activated = False
                time.sleep(0.02 if self.activated else 0.1)
                continue

            try:
                script = jedi.Script(self.text)
                l = script.complete(*self.text_cursor_pos)
            except:
                import traceback
                traceback.print_exc()
                l = []
            self.trigger.emit(pos, l)
            last_complete_time = time.time()

            self.activated = True
            text = self.text

    def on_exit(self):
        self.stop_flag = True
        self.exit(0)
        if self.isRunning():
            self.quit()
        self.wait(500)
