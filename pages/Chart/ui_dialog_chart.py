# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart_view_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(366, 550)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label)

        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_2)

        self.comboBox_4 = QComboBox(self.frame)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_4.addWidget(self.comboBox_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.comboBox_5 = QComboBox(self.frame)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_4.addWidget(self.comboBox_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.comboBox_7 = QComboBox(self.frame_3)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.verticalLayout_6.addWidget(self.comboBox_7)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)

        self.comboBox_8 = QComboBox(self.frame_3)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.verticalLayout_6.addWidget(self.comboBox_8)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.comboBox_9 = QComboBox(self.frame_3)
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.verticalLayout_6.addWidget(self.comboBox_9)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_7.addWidget(self.pushButton_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0435\u0441\u0442:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"HPL", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"HPCG", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 2 \u043d\u0435\u0434\u0435\u043b\u0438", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043a\u0432\u0430\u0440\u0442\u0430\u043b", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043f\u043e\u043b\u0443\u0433\u043e\u0434\u0438\u0435", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0433\u043e\u0434", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\u041b\u0438\u043d\u0435\u0439\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0435\u0441\u0442:", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Dialog", u"HPL", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Dialog", u"HPCG", None))

        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430:", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 2 \u043d\u0435\u0434\u0435\u043b\u0438", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043a\u0432\u0430\u0440\u0442\u0430\u043b", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u043f\u043e\u043b\u0443\u0433\u043e\u0434\u0438\u0435", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0433\u043e\u0434", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0432\u0441\u0435 \u0432\u0440\u0435\u043c\u044f", None))

        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430:", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435", None))

        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u043b\u0431\u0447\u0430\u0442\u0430\u044f \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
    # retranslateUi

