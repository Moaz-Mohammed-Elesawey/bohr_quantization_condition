# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    print('[INFO] using PyQt5 backend')

except ImportError as e:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    print('[INFO] using PySide2 backend')



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 650)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 500))
        self.centralwidget.setStyleSheet(u"QSplitter::handle{\n"
"	background-color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QSplitter::handle:hover{\n"
"	background-color: rgb(186, 189, 182)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setItalic(True)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.equation = QLineEdit(self.groupBox)
        self.equation.setObjectName(u"equation")
        self.equation.setEnabled(False)
        self.equation.setMinimumSize(QSize(0, 40))
        self.equation.setFont(font)
        self.equation.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QLineEdit:disbaled{\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout.addWidget(self.equation, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.R_inp = QDoubleSpinBox(self.groupBox_2)
        self.R_inp.setObjectName(u"R_inp")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_inp.sizePolicy().hasHeightForWidth())
        self.R_inp.setSizePolicy(sizePolicy)
        self.R_inp.setMinimumSize(QSize(0, 30))
        self.R_inp.setMinimum(-100.000000000000000)
        self.R_inp.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.R_inp, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.n_slider = QSlider(self.groupBox_2)
        self.n_slider.setObjectName(u"n_slider")
        self.n_slider.setMinimumSize(QSize(0, 30))
        self.n_slider.setMinimum(-100)
        self.n_slider.setMaximum(100)
        self.n_slider.setSingleStep(1)
        self.n_slider.setPageStep(1)
        self.n_slider.setOrientation(Qt.Horizontal)
        self.n_slider.setTickPosition(QSlider.TicksBothSides)
        self.n_slider.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.n_slider)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.A_inp = QDoubleSpinBox(self.groupBox_2)
        self.A_inp.setObjectName(u"A_inp")
        sizePolicy.setHeightForWidth(self.A_inp.sizePolicy().hasHeightForWidth())
        self.A_inp.setSizePolicy(sizePolicy)
        self.A_inp.setMinimumSize(QSize(0, 30))
        self.A_inp.setMinimum(-100.000000000000000)
        self.A_inp.setValue(0.150000000000000)

        self.gridLayout_2.addWidget(self.A_inp, 2, 1, 1, 1)

        self.n_inp = QDoubleSpinBox(self.groupBox_2)
        self.n_inp.setObjectName(u"n_inp")
        sizePolicy.setHeightForWidth(self.n_inp.sizePolicy().hasHeightForWidth())
        self.n_inp.setSizePolicy(sizePolicy)
        self.n_inp.setMinimumSize(QSize(0, 30))
        self.n_inp.setMinimum(-100.000000000000000)
        self.n_inp.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.n_inp, 4, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.A_slider = QSlider(self.groupBox_2)
        self.A_slider.setObjectName(u"A_slider")
        self.A_slider.setMinimumSize(QSize(0, 30))
        self.A_slider.setMinimum(-100)
        self.A_slider.setMaximum(100)
        self.A_slider.setSingleStep(1)
        self.A_slider.setPageStep(.5)
        self.A_slider.setOrientation(Qt.Horizontal)
        self.A_slider.setTickPosition(QSlider.TicksBothSides)
        self.A_slider.setTickInterval(10)

        self.horizontalLayout_3.addWidget(self.A_slider)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_6.addWidget(self.label_17)

        self.R_slider = QSlider(self.groupBox_2)
        self.R_slider.setObjectName(u"R_slider")
        self.R_slider.setMinimumSize(QSize(0, 30))
        self.R_slider.setMinimum(-100)
        self.R_slider.setMaximum(100)
        self.R_slider.setSingleStep(.5)
        self.R_slider.setPageStep(.5)
        self.R_slider.setOrientation(Qt.Horizontal)
        self.R_slider.setTickPosition(QSlider.TicksBothSides)
        self.R_slider.setTickInterval(10)

        self.horizontalLayout_6.addWidget(self.R_slider)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_6.addWidget(self.label_18)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.groupBox_2, 0, Qt.AlignTop)

        self.plot_btn = QPushButton(self.frame_2)
        self.plot_btn.setObjectName(u"plot_btn")
        self.plot_btn.setMinimumSize(QSize(100, 35))

        self.verticalLayout.addWidget(self.plot_btn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.splitter.addWidget(self.frame_2)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"DejaVu Math TeX Gyre")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.splitter.addWidget(self.frame)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Boher Quantization Condition", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Docs", None))
#if QT_CONFIG(shortcut)
        self.actionDocs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Bohr Quatizaition Condition", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EQ:", None))
        self.equation.setText(QCoreApplication.translate("MainWindow", u"r = R + A sin(n\u03b8)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.n_inp.setPrefix("")
        self.n_inp.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.plot_btn.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Interactive Plot", None))
    # retranslateUi

