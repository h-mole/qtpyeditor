# -*- coding:utf-8 -*-
# @Time: 2021/1/30 11:44
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: test.py
from qtpy.QtWidgets import QApplication

from qtpyeditor.codeedit import PMPythonCodeEdit

if __name__ == '__main__':
    app = QApplication([])
    e = PMPythonCodeEdit()
    e.show()
    app.exec_()
