# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kustic_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 591)
        MainWindow.setStyleSheet("border: none ;\n"
"background-color: transparent;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setMinimumSize(QtCore.QSize(913, 590))
        self.frame_main.setStyleSheet("QFrame {\n"
"border:none;\n"
"border-bottom-radius:25px;\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QtCore.QSize(851, 51))
        self.frame_top.setStyleSheet("QFrame {\n"
"background-color: rgb(57, 46, 69);\n"
"border:none;\n"
"border-top-radius: 30px;\n"
"}")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_top)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_top_2 = QtWidgets.QFrame(self.frame_top)
        self.frame_top_2.setMinimumSize(QtCore.QSize(851, 21))
        self.frame_top_2.setStyleSheet("border:none;\n"
"background-color: rgb(184, 40, 0);")
        self.frame_top_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_2.setObjectName("frame_top_2")
        self.gridLayout_3.addWidget(self.frame_top_2, 1, 0, 1, 3)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_top)
        self.btn_minimize.setMinimumSize(QtCore.QSize(31, 31))
        self.btn_minimize.setMaximumSize(QtCore.QSize(31, 31))
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 142, 73);\n"
"}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QtCore.QSize(20, 20))
        self.btn_minimize.setObjectName("btn_minimize")
        self.gridLayout_3.addWidget(self.btn_minimize, 0, 1, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.frame_top)
        self.btn_close.setMinimumSize(QtCore.QSize(31, 31))
        self.btn_close.setMaximumSize(QtCore.QSize(31, 31))
        self.btn_close.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 142, 73);\n"
"}")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(20, 20))
        self.btn_close.setObjectName("btn_close")
        self.gridLayout_3.addWidget(self.btn_close, 0, 0, 1, 1)
        self.frame_top_1 = QtWidgets.QFrame(self.frame_top)
        self.frame_top_1.setMinimumSize(QtCore.QSize(791, 31))
        self.frame_top_1.setStyleSheet("background-color: rgb(184, 40, 0);")
        self.frame_top_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_1.setObjectName("frame_top_1")
        self.gridLayout_3.addWidget(self.frame_top_1, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_top, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setStyleSheet("QStackedWidget{\n"
"border: none;\n"
"background-color: rgb(44, 44, 44);\n"
"/* background-color: transparent; */\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pg_home = QtWidgets.QWidget()
        self.pg_home.setStyleSheet("")
        self.pg_home.setObjectName("pg_home")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pg_home)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_btn = QtWidgets.QPushButton(self.pg_home)
        self.frame_btn.setMinimumSize(QtCore.QSize(811, 521))
        self.frame_btn.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border:none;\n"
"}")
        self.frame_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/kasqued.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frame_btn.setIcon(icon2)
        self.frame_btn.setIconSize(QtCore.QSize(900, 900))
        self.frame_btn.setFlat(True)
        self.frame_btn.setObjectName("frame_btn")
        self.gridLayout_4.addWidget(self.frame_btn, 0, 0, 1, 1)
        self.btn_music2 = QtWidgets.QPushButton(self.pg_home)
        self.btn_music2.setGeometry(QtCore.QRect(390, 210, 141, 141))
        self.btn_music2.setStyleSheet("QPushButton{\n"
"background-color: rgb(46, 32, 58);\n"
"border-radius: 60px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(57, 46, 69);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(112, 0, 132);\n"
"}")
        self.btn_music2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/media-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_music2.setIcon(icon3)
        self.btn_music2.setIconSize(QtCore.QSize(400, 400))
        self.btn_music2.setAutoRepeatInterval(100)
        self.btn_music2.setObjectName("btn_music2")
        self.stackedWidget.addWidget(self.pg_home)
        self.pg_music = QtWidgets.QWidget()
        self.pg_music.setObjectName("pg_music")
        self.frame_2 = QtWidgets.QFrame(self.pg_music)
        self.frame_2.setGeometry(QtCore.QRect(19, 30, 811, 371))
        self.frame_2.setStyleSheet("background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"border-radius:25px ;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listView = QtWidgets.QListView(self.frame_2)
        self.listView.setGeometry(QtCore.QRect(10, 10, 401, 351))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.listView.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listView.setFont(font)
        self.listView.setStyleSheet("")
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.music_photo = QtWidgets.QLabel(self.frame_2)
        self.music_photo.setGeometry(QtCore.QRect(430, 10, 361, 351))
        self.music_photo.setText("")
        self.music_photo.setPixmap(QtGui.QPixmap("icons/vinyl.png"))
        self.music_photo.setScaledContents(True)
        self.music_photo.setObjectName("music_photo")
        self.horizontalSlider = QtWidgets.QSlider(self.pg_music)
        self.horizontalSlider.setGeometry(QtCore.QRect(19, 430, 811, 31))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(811, 31))
        self.horizontalSlider.setStyleSheet("background-color: rgb(242, 92, 25);\n"
"color: rgb(181, 144, 204);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.btn_play = QtWidgets.QPushButton(self.pg_music)
        self.btn_play.setGeometry(QtCore.QRect(400, 460, 61, 41))
        self.btn_play.setStyleSheet("QPushButton{\n"
"background-color:rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 142, 73);\n"
"}")
        self.btn_play.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/music-note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon4)
        self.btn_play.setIconSize(QtCore.QSize(24, 24))
        self.btn_play.setObjectName("btn_play")
        self.btn_back = QtWidgets.QPushButton(self.pg_music)
        self.btn_back.setGeometry(QtCore.QRect(300, 460, 61, 41))
        self.btn_back.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 142, 73);\n"
"}")
        self.btn_back.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/media-step-backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon5)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setObjectName("btn_back")
        self.btn_next = QtWidgets.QPushButton(self.pg_music)
        self.btn_next.setGeometry(QtCore.QRect(500, 460, 61, 41))
        self.btn_next.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 142, 73);\n"
"}")
        self.btn_next.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/media-step-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon6)
        self.btn_next.setIconSize(QtCore.QSize(24, 24))
        self.btn_next.setObjectName("btn_next")
        self.stackedWidget.addWidget(self.pg_music)
        self.pg_setting = QtWidgets.QWidget()
        self.pg_setting.setObjectName("pg_setting")
        self.label_info = QtWidgets.QLabel(self.pg_setting)
        self.label_info.setGeometry(QtCore.QRect(10, 10, 391, 481))
        self.label_info.setObjectName("label_info")
        self.frame = QtWidgets.QFrame(self.pg_setting)
        self.frame.setGeometry(QtCore.QRect(419, 10, 421, 511))
        self.frame.setStyleSheet("background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"border-radius:25px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.photo_settings = QtWidgets.QLabel(self.frame)
        self.photo_settings.setGeometry(QtCore.QRect(16, 12, 391, 481))
        self.photo_settings.setText("")
        self.photo_settings.setPixmap(QtGui.QPixmap("icons/guitar.jpg"))
        self.photo_settings.setScaledContents(True)
        self.photo_settings.setWordWrap(False)
        self.photo_settings.setObjectName("photo_settings")
        self.label_2 = QtWidgets.QLabel(self.pg_setting)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 381, 19))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.pg_setting)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.frame_left = QtWidgets.QFrame(self.frame_main)
        self.frame_left.setMinimumSize(QtCore.QSize(61, 541))
        self.frame_left.setStyleSheet("QFrame {\n"
"background-color:rgb(44, 44, 44);\n"
"border-bottom-left-radius: 30px;\n"
"border:none;\n"
"border-radius:0px;\n"
"}")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_left)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_goto = QtWidgets.QPushButton(self.frame_left)
        self.btn_goto.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_goto.setStyleSheet("QPushButton{\n"
"background-color:rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 142, 73);\n"
"}")
        self.btn_goto.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/equalizer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_goto.setIcon(icon7)
        self.btn_goto.setIconSize(QtCore.QSize(24, 24))
        self.btn_goto.setObjectName("btn_goto")
        self.gridLayout_5.addWidget(self.btn_goto, 2, 0, 1, 1)
        self.btn_go_to_setting = QtWidgets.QPushButton(self.frame_left)
        self.btn_go_to_setting.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_go_to_setting.setStyleSheet("QPushButton{\n"
"background-color:rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(255, 142, 73);\n"
"}")
        self.btn_go_to_setting.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_go_to_setting.setIcon(icon8)
        self.btn_go_to_setting.setIconSize(QtCore.QSize(24, 24))
        self.btn_go_to_setting.setObjectName("btn_go_to_setting")
        self.gridLayout_5.addWidget(self.btn_go_to_setting, 3, 0, 1, 1)
        self.btn_music = QtWidgets.QPushButton(self.frame_left)
        self.btn_music.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_music.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_music.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(255, 142, 73);\n"
"}")
        self.btn_music.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/headphones.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_music.setIcon(icon9)
        self.btn_music.setIconSize(QtCore.QSize(24, 24))
        self.btn_music.setObjectName("btn_music")
        self.gridLayout_5.addWidget(self.btn_music, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_left, 1, 1, 1, 1)
        self.btn_togle = QtWidgets.QPushButton(self.frame_main)
        self.btn_togle.setMinimumSize(QtCore.QSize(61, 51))
        self.btn_togle.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 40, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(242, 92, 25);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(255, 142, 73);\n"
"}")
        self.btn_togle.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_togle.setIcon(icon10)
        self.btn_togle.setIconSize(QtCore.QSize(24, 24))
        self.btn_togle.setObjectName("btn_togle")
        self.gridLayout_2.addWidget(self.btn_togle, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_info.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#f25c19;\">Kustic Player</span></p><p><span style=\" font-size:14pt;\">MEEC</span></p><p><span style=\" font-size:14pt;\">Advanced Robotics</span></p><p><span style=\" font-size:14pt;\">Group I</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b590cc;\">v 0.0.1</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
