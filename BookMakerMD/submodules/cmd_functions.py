# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:10:59 2017

@author: soma
"""
import os
import tarfile
import shutil
from PyQt5 import QtWidgets

class keyCommends(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.root = parent

    def shortcut_cmd(self, key):
        if key == "Ctrl+S":
            self.cmd_save()
        elif key == "Ctrl+O":
            self.cmd_open()

    def cmd_save(self):
        if self.root.Edit_file_path == "":
            dialog = QtWidgets.QFileDialog.getSaveFileName
            fileName, _ = dialog(self,"QFileDialog.getSaveFileName()","","모든 파일 (*)")
        else:
            fileName = self.root.Edit_file_path
        if fileName:
            os.mkdir(fileName)
            self.root.Edit_file_path = fileName
            text = self.root.tabs.view_editor.editor.toPlainText()
            with open(os.path.join(fileName,"text.md"), "w+", encoding='utf8') as f:
                f.write(text)
            tar = tarfile.open("{}.mdbk".format(self.root.Edit_file_path), "w:gz")
            TarName = os.path.basename(os.path.normpath(self.root.Edit_file_path))
            tar.add(self.root.Edit_file_path, arcname=TarName)
            tar.close()
            shutil.rmtree(self.root.Edit_file_path)

    def cmd_open(self):
        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setNameFilter("책 파일 (*.mdbk);;모든 파일 (*)")
        fileName, _ = fileDialog.getOpenFileName()
        if fileName:
            self.root.Edit_file_path = fileName
            tar = tarfile.open(fileName)
            members = tar.getmembers()
            tar_name = members[0].name
            for member in members[1:]:
                if member.name == tar_name + '/text.md':
                    f = tar.extractfile(member)
                    content = f.read()
                    self.root.tabs.view_editor.editor.setText(content.decode("utf-8"))

