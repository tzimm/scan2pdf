# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScanIntoPdf_gui.ui'
#
# Created: Mon Mar 11 17:06:52 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 641)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.list_FilesToJoin = QtGui.QListWidget(self.centralwidget)
        self.list_FilesToJoin.setEnabled(True)
        self.list_FilesToJoin.setObjectName("list_FilesToJoin")
        self.verticalLayout_4.addWidget(self.list_FilesToJoin)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_FileToList = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_FileToList.sizePolicy().hasHeightForWidth())
        self.txt_FileToList.setSizePolicy(sizePolicy)
        self.txt_FileToList.setMaximumSize(QtCore.QSize(16777215, 27))
        self.txt_FileToList.setLineWidth(1)
        self.txt_FileToList.setMidLineWidth(0)
        self.txt_FileToList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_FileToList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_FileToList.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txt_FileToList.setObjectName("txt_FileToList")
        self.horizontalLayout.addWidget(self.txt_FileToList)
        self.pb_search = QtGui.QPushButton(self.centralwidget)
        self.pb_search.setObjectName("pb_search")
        self.horizontalLayout.addWidget(self.pb_search)
        self.pb_add = QtGui.QPushButton(self.centralwidget)
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout.addWidget(self.pb_add)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkbx_flip = QtGui.QCheckBox(self.centralwidget)
        self.checkbx_flip.setObjectName("checkbx_flip")
        self.verticalLayout.addWidget(self.checkbx_flip)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 20))
        self.label.setMaximumSize(QtCore.QSize(80, 20))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.slider_contrast = QtGui.QSlider(self.centralwidget)
        self.slider_contrast.setMinimum(0)
        self.slider_contrast.setMaximum(20)
        self.slider_contrast.setSliderPosition(20)
        self.slider_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contrast.setTickPosition(QtGui.QSlider.TicksBelow)
        self.slider_contrast.setObjectName("slider_contrast")
        self.horizontalLayout_3.addWidget(self.slider_contrast)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(80, 20))
        self.label_3.setMaximumSize(QtCore.QSize(80, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.slider_sharpness = QtGui.QSlider(self.centralwidget)
        self.slider_sharpness.setMinimum(0)
        self.slider_sharpness.setMaximum(20)
        self.slider_sharpness.setProperty("value", 20)
        self.slider_sharpness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_sharpness.setTickPosition(QtGui.QSlider.TicksBelow)
        self.slider_sharpness.setObjectName("slider_sharpness")
        self.horizontalLayout_5.addWidget(self.slider_sharpness)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(80, 20))
        self.label_2.setMaximumSize(QtCore.QSize(80, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.slider_brightness = QtGui.QSlider(self.centralwidget)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(20)
        self.slider_brightness.setSliderPosition(20)
        self.slider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brightness.setTickPosition(QtGui.QSlider.TicksBelow)
        self.slider_brightness.setObjectName("slider_brightness")
        self.horizontalLayout_4.addWidget(self.slider_brightness)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_outputpdf = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_outputpdf.sizePolicy().hasHeightForWidth())
        self.txt_outputpdf.setSizePolicy(sizePolicy)
        self.txt_outputpdf.setMinimumSize(QtCore.QSize(0, 27))
        self.txt_outputpdf.setMaximumSize(QtCore.QSize(16777215, 27))
        self.txt_outputpdf.setObjectName("txt_outputpdf")
        self.horizontalLayout_2.addWidget(self.txt_outputpdf)
        self.pb_join = QtGui.QPushButton(self.centralwidget)
        self.pb_join.setObjectName("pb_join")
        self.horizontalLayout_2.addWidget(self.pb_join)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 27, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_status = QtGui.QLabel(self.centralwidget)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.verticalLayout_4.addWidget(self.label_status)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.list_FilesToJoin.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ScanIntoPdf", None, QtGui.QApplication.UnicodeUTF8))
        self.list_FilesToJoin.setSortingEnabled(True)
        self.txt_FileToList.setPlainText(QtGui.QApplication.translate("MainWindow", "/home/add.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_search.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbx_flip.setText(QtGui.QApplication.translate("MainWindow", "flip pictures", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "contrast", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "sharpness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "brightness", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_outputpdf.setPlainText(QtGui.QApplication.translate("MainWindow", "output.pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_join.setText(QtGui.QApplication.translate("MainWindow", "Convert!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status.setText(QtGui.QApplication.translate("MainWindow", "test", None, QtGui.QApplication.UnicodeUTF8))

