# -*- coding:utf-8 -*-
# @Time: 2021/1/30 11:44
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: test.py
import os
from qtpy.QtWidgets import QApplication

from qtpyeditor.codeedit import PMPythonCodeEdit
from qtpyeditor import PMGPythonEditor

if __name__ == '__main__':
    app = QApplication([])
    e = PMGPythonEditor()
    e.show()
    e.load_file(os.path.join(os.path.dirname(__file__), 'test_files', 'test_file.py'))
    app.exec_()
