# -*- coding: utf-8 -*-
import re
import markdown
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWebKitWidgets


class gui_frame_tabs(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(QtWidgets.QTabWidget, self).__init__(parent)
        self.view_editor = ui_tab_edit()
        self.view_option = ui_tab_option()
        self.addTab(self.view_editor, "편집")
        #self.addTab(self.view_option, "옵션")


class ui_tab_edit(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        # UI Object init
        self.treeview = QtWidgets.QTreeView(self)
        self.treeview.header().hide()
        self.treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeview.setIndentation(5)
        self.editor = QtWidgets.QTextEdit(self)
        self.editor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.preview = QtWebKitWidgets.QWebView(self)
        self.preview.setUrl(QtCore.QUrl("about:blank"))
        # UI Geometry init
        self.treeview.setGeometry(QtCore.QRect(0, 0, 200, 400))
        self.editor.setGeometry(QtCore.QRect(200, 0, 300, 400))
        self.preview.setGeometry(QtCore.QRect(500, 0, 300, 400))
        # Evants
        self.onEdit()
        self.editor.textChanged.connect(self.onEdit)

    def onResize(self, event):
        new_width = event.size().width()-200
        new_height = event.size().height()
        self.treeview.resize(QtCore.QSize(200, new_height))
        self.editor.setGeometry(QtCore.QRect(200, 0, new_width/2, new_height))
        self.preview.setGeometry(QtCore.QRect(200+new_width/2, 0, new_width/2, new_height))

    def onEdit(self):
        # Preview Update
        text = self.editor.toPlainText()
        html = markdown.markdown(text)#html_format(markdown.markdown(text))
        self.preview.setHtml(html)
        # TOC Update
        re_toc = re.compile(u"^(#+)(.+)", re.MULTILINE)
        tree_model = QtGui.QStandardItemModel()
        rootNode = tree_model.invisibleRootItem()
        toc_content = []
        for _level, _str in re_toc.findall(text):
            _str = _str.strip()
            if len(_level) == 1:
                toc_content.append((_str, []))
            elif len(_level) == 2:
                try:
                    toc_content[-1][1].append((_str, []))
                except:
                    toc_content.append((_str, []))
            else:
                continue
        self.__Add_Item(rootNode, toc_content)
        self.treeview.setModel(tree_model)

    def __Add_Item(self, parent, content):
        # Tree View TOC Update Subfunction
        for _str, _sub in content:
            item = QtGui.QStandardItem(_str)
            parent.appendRow(item)
            if _sub:
                self.__Add_Item(item, _sub)

class ui_tab_option(QtWidgets.QTabWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()