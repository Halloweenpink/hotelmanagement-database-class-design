# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyPwd.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MpwdWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n"
"*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"}\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}\n"
"#centralwidget{\n"
"border-image:url(D:/pictures/login4.jpg) strectch；\n"
"}\n"
"\n"
"QToolButton{\n"
"background:red;\n"
"border-radius:60px;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"QPushButton{\n"
"background:red;;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#333;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 60, 491, 511))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_oldpasswd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_oldpasswd.setGeometry(QtCore.QRect(70, 250, 361, 31))
        self.lineEdit_oldpasswd.setText("")
        self.lineEdit_oldpasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_oldpasswd.setObjectName("lineEdit_oldpasswd")
        self.commitButton = QtWidgets.QPushButton(self.frame)
        self.commitButton.setGeometry(QtCore.QRect(40, 430, 421, 51))
        self.commitButton.setStyleSheet("background-color: rgb(117, 200, 255);")
        self.commitButton.setObjectName("commitButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 300, 121, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_newpwd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_newpwd.setGeometry(QtCore.QRect(70, 340, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.lineEdit_newpwd.setFont(font)
        self.lineEdit_newpwd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_newpwd.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.lineEdit_newpwd.setText("")
        self.lineEdit_newpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_newpwd.setObjectName("lineEdit_newpwd")
        self.lineEdit_sid = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_sid.setGeometry(QtCore.QRect(70, 160, 361, 31))
        self.lineEdit_sid.setText("")
        self.lineEdit_sid.setObjectName("lineEdit_sid")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(350, 0, 121, 121))
        self.toolButton.setStyleSheet("background-color: rgb(2, 222, 255);")
        self.toolButton.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(150, 150))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "员工修改密码"))
        self.label.setText(_translate("MainWindow", "修改密码"))
        self.lineEdit_oldpasswd.setPlaceholderText(_translate("MainWindow", "old password"))
        self.commitButton.setText(_translate("MainWindow", "确认修改"))
        self.label_2.setText(_translate("MainWindow", "旧密码"))
        self.label_4.setText(_translate("MainWindow", "新密码"))
        self.lineEdit_newpwd.setPlaceholderText(_translate("MainWindow", "new password"))
        self.lineEdit_sid.setPlaceholderText(_translate("MainWindow", "编号"))
        self.label_3.setText(_translate("MainWindow", "员工编号"))
