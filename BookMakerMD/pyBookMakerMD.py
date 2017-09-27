# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from submodules.gui_frame_tabs import gui_frame_tabs
from submodules.cmd_functions import keyCommends



class run_program(QtWidgets.QMainWindow):
    Program = "Book Maker"
    Version = "0.0.1"
    Edit_file_path = ""
    keyPressed = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.cmd = keyCommends(self)
        self.setWindowTitle(self.Program+" "+self.Version)
        self.setStyleSheet("font: 12pt")
        self.resize(600, 400)
        self.tabs = gui_frame_tabs(self)
        self.resizeEvent = self.onResize
        self.setCentralWidget(self.tabs)
        self.show()

    def onResize(self, event):
        self.tabs.view_editor.onResize(event)

    def keyPressEvent(self, event):
        keyname = ''
        key = event.key()
        modifiers = int(event.modifiers())
        MOD_MASK = (QtCore.Qt.CTRL | QtCore.Qt.ALT | QtCore.Qt.SHIFT | QtCore.Qt.META)
        if (modifiers and modifiers & MOD_MASK == modifiers and
            key > 0 and key != QtCore.Qt.Key_Shift and key != QtCore.Qt.Key_Alt and
            key != QtCore.Qt.Key_Control and key != QtCore.Qt.Key_Meta):
            self.cmd.shortcut_cmd(QtGui.QKeySequence(modifiers + key).toString())
        self.keyPressed.emit(keyname)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    locale = QtCore.QLocale.system().name()
    qtTranslator = QtCore.QTranslator()
    if qtTranslator.load("qt_"+locale):
        app.installTranslator(qtTranslator)

    gui = run_program()
    sys.exit(app.exec_())
