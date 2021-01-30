# -*- coding:utf-8 -*-
#
# 代码高亮部分来源：
# https://blog.csdn.net/xiaoyangyang20/article/details/68923133
#
# 窗口交互逻辑为本人原创，转载请注明出处！
#
# 自动补全借用了Jedi库，能够达到不错的体验。
# 文本编辑器采用了一个QThread作为后台线程，避免补全过程发生卡顿。后台线程会延迟结果返回，
# 返回时如果光标位置未发生变化，则可以显示补全菜单，否则认为文本已经改变，就应当进行下一次补全操作。

# @Time: 2021/1/18 8:03
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: editor.py

from qtpy.QtWidgets import QApplication, QListWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextBrowser
from typing import Dict
from qtpyeditor.codeeditor import PMGBaseEditor
from qtpyeditor.codeedit import PMBaseCodeEdit, PMPythonCodeEdit


class PMGPythonEditor(PMGBaseEditor):
    def __init__(self, parent: 'PMGPythonEditor' = None):
        super().__init__(parent=parent)
        self.edit = PMPythonCodeEdit(self)
        self.line_number_area = QWidget()
        self.line_number_area.setMaximumHeight(60)
        self.line_number_area.setMinimumHeight(20)
        self.status_label = QLabel()
        line_number_area_layout = QHBoxLayout()
        line_number_area_layout.addWidget(self.status_label)
        line_number_area_layout.setContentsMargins(0, 0, 0, 0)
        self.line_number_area.setLayout(line_number_area_layout)
        self.modified_status_label = QLabel()
        self.modified_status_label.setText('')
        line_number_area_layout.addWidget(self.modified_status_label)

        self.edit.cursorPositionChanged.connect(self.show_cursor_pos)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.edit)
        layout.addWidget(self.line_number_area)

        self.setLayout(layout)

        self.set_edit(self.edit)
        self.text_edit: PMPythonCodeEdit = self.edit

    def show_cursor_pos(self):
        row = self.edit.textCursor().block().blockNumber()
        col = self.edit.textCursor().columnNumber()
        self.status_label.setText(
            '行：{row},列:{col}'.format(row=row + 1, col=col + 1))

    def update_settings(self, settings: Dict[str, str]):
        pass

    def open(self, path: str):
        pass

    def autocomp_stop(self):
        print('autocomp stopped')
        self.text_edit.autocomp_thread.on_exit()


if __name__ == '__main__':
    app = QApplication([])
    editor = PMPythonCodeEdit()
    editor.show()

    editor.setPlainText("abcdefg = 123\n" * 100)
    editor.highlighter.registerHighlight(5, 3, 7, editor.highlighter.DEHIGHLIGHT, 'This is an Dehighlight')
    editor.highlighter.registerHighlight(3, 1, 7, editor.highlighter.WARNING, 'This is an warning')
    editor.highlighter.rehighlight()

    app.exec_()
