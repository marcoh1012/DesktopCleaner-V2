# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesktopCleaner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import Icons, DesktopCleanerCode, os, subprocess,ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
from ctypes import wintypes

class Ui_DesktopCleaner(object):

        lpBuffer = wintypes.LPWSTR()
        AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
        AppUserModelID(ctypes.cast(ctypes.byref(lpBuffer), wintypes.LPWSTR))
        appid = lpBuffer.value
        ctypes.windll.kernel32.LocalFree(lpBuffer)
        def setupUi(self, DesktopCleaner):
                DesktopCleaner.setObjectName("DesktopCleaner")
                DesktopCleaner.setFixedSize(615, 563)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap( ":/Banner/Pictures/CleanerIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                DesktopCleaner.setWindowIcon(icon)
                DesktopCleaner.setStyleSheet("background-color: rgb(0, 0, 255);")
                self.centralwidget = QtWidgets.QWidget(DesktopCleaner)
                self.centralwidget.setObjectName("centralwidget")
                self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
                self.cleanButton.setGeometry(QtCore.QRect(340, 380, 251, 131))
                font = QtGui.QFont()
                font.setPointSize(50)
                font.setBold(True)
                font.setWeight(75)
                self.cleanButton.setFont(font)
                self.cleanButton.setStyleSheet("background-image: url(:/Banner/Pictures/Clean Button.png);\n"
        "background-color: rgb(0, 85, 255);\n"
        "selection-background-color: rgb(0, 0, 255);")
                self.cleanButton.setText("")
                self.cleanButton.setObjectName("cleanButton")
                self.revomeFolderButton = QtWidgets.QPushButton(self.centralwidget)
                self.revomeFolderButton.setGeometry(QtCore.QRect(20, 430, 261, 21))
                self.revomeFolderButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
        "selection-background-color: rgb(0, 0, 255);")
                self.revomeFolderButton.setObjectName("revomeFolderButton")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(340, 200, 261, 20))
                font = QtGui.QFont("fixed")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(340, 255, 261, 20))
                font = QtGui.QFont("fixed")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.availableFolders = QtWidgets.QListWidget(self.centralwidget)
                self.availableFolders.setGeometry(QtCore.QRect(20, 160, 261, 261))
                self.availableFolders.setStyleSheet("background-color: rgb(213, 213, 213);")
                self.availableFolders.setObjectName("availableFolders")
                self.folderName = QtWidgets.QTextEdit(self.centralwidget)
                self.folderName.setGeometry(QtCore.QRect(340, 220, 261, 31))
                self.folderName.setStyleSheet("background-color: rgb(213, 213, 213);")
                self.folderName.setTabChangesFocus(True)
                self.folderName.setObjectName("folderName")
                self.saveFolders = QtWidgets.QCheckBox(self.centralwidget)
                self.saveFolders.setGeometry(QtCore.QRect(340, 320, 231, 17))
                font = QtGui.QFont("fixed")
                font.setPointSize(7)
                font.setBold(True)
                font.setWeight(75)
                self.saveFolders.setFont(font)
                self.saveFolders.setObjectName("saveFolders")
                self.folderExtension = QtWidgets.QPlainTextEdit(self.centralwidget)
                self.folderExtension.setEnabled(True)
                self.folderExtension.setGeometry(QtCore.QRect(340, 280, 261, 31))
                self.folderExtension.setStyleSheet("background-color: rgb(213, 213, 213);")
                self.folderExtension.setTabChangesFocus(True)
                self.folderExtension.setPlainText("")
                self.folderExtension.setOverwriteMode(False)
                self.folderExtension.setObjectName("folderExtension")
                self.addButtonButton = QtWidgets.QPushButton(self.centralwidget)
                self.addButtonButton.setGeometry(QtCore.QRect(520, 340, 75, 23))
                self.addButtonButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
        "selection-background-color: rgb(0, 0, 255);")
                self.addButtonButton.setObjectName("addButtonButton")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(20, 0, 581, 121))
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(20, 110, 261, 45))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(340, 150, 241, 41))
                self.label_5.setObjectName("label_5")
                DesktopCleaner.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(DesktopCleaner)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
                self.menubar.setStyleSheet("background-color: rgb(153, 153, 153);")
                self.menubar.setObjectName("menubar")
                self.menuHelp = QtWidgets.QMenu(self.menubar)
                self.menuHelp.setObjectName("menuHelp")
                self.menuQuit = QtWidgets.QMenu(self.menubar)
                self.menuQuit.setObjectName("menuQuit")
                DesktopCleaner.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(DesktopCleaner)
                self.statusbar.setObjectName("statusbar")
                DesktopCleaner.setStatusBar(self.statusbar)
                self.actionQuit = QtWidgets.QAction(DesktopCleaner)
                self.actionQuit.setEnabled(True)
                self.actionQuit.setObjectName("actionQuit")
                self.actionHelp = QtWidgets.QAction(DesktopCleaner)
                self.actionHelp.setObjectName("actionHelp")
                self.menubar.addAction('Help',self.helpPage)
                self.menubar.addAction('Quit',self.Quit)

                self.retranslateUi(DesktopCleaner)
                QtCore.QMetaObject.connectSlotsByName(DesktopCleaner)

        def retranslateUi(self, DesktopCleaner):
                _translate = QtCore.QCoreApplication.translate
                DesktopCleaner.setWindowTitle(_translate("DesktopCleaner", "DesktopCleaner"))
                self.revomeFolderButton.setText(_translate("DesktopCleaner", "Remove Selected Folder"))
                self.label.setText(_translate("DesktopCleaner", "<html><head/><body><p><span style=\" color:#ffffff;\">Folder Name:</span></p></body></html>"))
                self.label_2.setText(_translate("DesktopCleaner", "<html><head/><body><p><span style=\" color:#ffffff;\">Extensions (i.e. .jpg, .wmv, .docx):</span></p></body></html>"))
                self.folderName.setHtml(_translate("DesktopCleaner", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.saveFolders.setText(_translate("DesktopCleaner", "Check to save Folders for future use"))
                self.addButtonButton.setText(_translate("DesktopCleaner", "Add Folder"))
                self.label_3.setText(_translate("DesktopCleaner", "<html><head/><body><p><img src=\":/Banner/Pictures/DesktopCleanerBanner.png\"/></p></body></html>"))
                self.label_4.setText(_translate("DesktopCleaner", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-style:italic; text-decoration: underline;\">Folders:</span></p></body></html>"))
                self.label_5.setText(_translate("DesktopCleaner", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-style:italic; text-decoration: underline;\">Add A Folder</span></p></body></html>"))
                self.menuHelp.setTitle(_translate("DesktopCleaner", "Help"))
                self.menuQuit.setTitle(_translate("DesktopCleaner", "Quit"))
                self.actionQuit.setText(_translate("DesktopCleaner", "Quit"))
                self.actionHelp.setText(_translate("DesktopCleaner", "Help"))

                self.printfolders()

                self.cleanButton.clicked.connect(self.cleanDesktop)
                self.addButtonButton.clicked.connect(self.addfolder)
                self.revomeFolderButton.clicked.connect(self.removeFolder)

        def helpPage(self):
                helpFile=DesktopCleanerCode.currentdir + r'\Help.txt'
                subprocess.Popen(['notepad.exe', helpFile])

        def printfolders(self):
                folders=DesktopCleanerCode.getFolders()
                #print("printing")  
                for folder in folders:
                        self.availableFolders.addItem(folder[0])
                self.availableFolders.addItem("Other")
                self.availableFolders.show()

        def addfolder(self):
                DesktopCleanerCode.create_folder(self.folderName.toPlainText(),self.folderExtension.toPlainText())
                self.folderName.clear()
                self.folderExtension.clear()
                self.availableFolders.clear()
                self.printfolders()
                
        def removeFolder(self):
                folder =self.availableFolders.currentItem().text()
                print(folder)
                DesktopCleanerCode.remove_folder(folder)
                self.availableFolders.clear()
                self.printfolders()

        def cleanDesktop(self):
                if self.saveFolders.isChecked():
                        DesktopCleanerCode.saveFolders()
                DesktopCleanerCode.CleanDesktop()
                self.availableFolders.clear()
                self.printfolders()

        def Quit(self):
                sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DesktopCleaner = QtWidgets.QMainWindow()
    ui = Ui_DesktopCleaner()
    ui.setupUi(DesktopCleaner)
    DesktopCleaner.show()
    sys.exit(app.exec_())
