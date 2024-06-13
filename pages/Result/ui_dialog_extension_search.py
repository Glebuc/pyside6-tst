# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extension_search.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 450)
        Dialog.setMinimumSize(QSize(350, 450))
        Dialog.setMaximumSize(QSize(350, 450))
        Dialog.setStyleSheet(u"/* \u0426\u0432\u0435\u0442\u0430 \u0438 \u0448\u0440\u0438\u0444\u0442\u044b */\n"
"    QDateEdit QCalendarWidget {\n"
"        background-color: #2c3e50; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        color: #ecf0f1; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"        font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    }\n"
"    \n"
"    /* \u041a\u043d\u043e\u043f\u043a\u0438 \u0432\u0432\u0435\u0440\u0445/\u0432\u043d\u0438\u0437 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043c\u0435\u0441\u044f\u0446\u0435\u0432/\u0433\u043e\u0434\u043e\u0432 */\n"
"    QDateEdit QCalendarWidget QAbstractItemView {\n"
"        background-color: #34495e; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        color: #ecf0f1; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }\n"
"\n"
"    /* \u041a\u043d\u043e\u043f\u043a\u0438 \u043f\u0435\u0440\u0435\u043a\u043b"
                        "\u044e\u0447\u0435\u043d\u0438\u044f \u043c\u0435\u0441\u044f\u0446\u0435\u0432/\u0433\u043e\u0434\u043e\u0432 */\n"
"    QDateEdit QCalendarWidget QToolButton {\n"
"        background-color: #2c3e50; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        color: #ecf0f1; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }\n"
"\n"
"    /* \u041a\u043d\u043e\u043f\u043a\u0438 \u0432\u0441\u043f\u043b\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u043e\u043a\u043d\u0430 */\n"
"    QDateEdit QCalendarWidget QToolButton:hover {\n"
"        background-color: #4a69bd; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    }\n"
"\n"
"    /* \u0424\u043e\u043d \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u0434\u0430\u0442\u044b */\n"
"    QDateEdit QCalendarWidget QTableView:selected {\n"
"        background-color: #4a69bd; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
""
                        "        color: #ecf0f1; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }\n"
"\n"
"    /* \u0424\u043e\u043d \u0434\u043b\u044f \u0432\u044b\u0445\u043e\u0434\u043d\u044b\u0445 \u0434\u043d\u0435\u0439 */\n"
"    QDateEdit QCalendarWidget QTableView:!disabled {\n"
"        alternate-background-color: #34495e; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    }\n"
"    \n"
"    /* \u0413\u0440\u0430\u043d\u0438\u0446\u044b \u044f\u0447\u0435\u0435\u043a */\n"
"    QDateEdit QCalendarWidget QTableView {\n"
"        border: 1px solid #34495e; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446 */\n"
"    }\n"
"\n"
"QDateEdit QCalendarWidget QHeaderView {\n"
"        background-color: #ffffff; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        color: #ecf0f1; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }\n"
"\n"
"    /* \u041f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u0438 \u043c\u0435\u0441"
                        "\u044f\u0446\u0435\u0432 \u0438 \u0433\u043e\u0434\u043e\u0432 */\n"
"    QDateEdit QCalendarWidget QToolButton {\n"
"        background-color: #2c3e50; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        color: #ecf0f1; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }\n"
"\n"
"    /* \u041f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u0438 \u043c\u0435\u0441\u044f\u0446\u0435\u0432 \u0438 \u0433\u043e\u0434\u043e\u0432 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    QDateEdit QCalendarWidget QToolButton:hover {\n"
"        background-color: #4a69bd; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    }")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.before_dateEdit = QDateEdit(self.frame)
        self.before_dateEdit.setObjectName(u"before_dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.before_dateEdit.sizePolicy().hasHeightForWidth())
        self.before_dateEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.before_dateEdit.setFont(font)
        self.before_dateEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.before_dateEdit.setMinimumDateTime(QDateTime(QDate(2023, 9, 13), QTime(9, 0, 0)))
        self.before_dateEdit.setMinimumDate(QDate(2023, 9, 13))
        self.before_dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.before_dateEdit, 11, 4, 1, 2)

        self.from_dateEdit = QDateEdit(self.frame)
        self.from_dateEdit.setObjectName(u"from_dateEdit")
        sizePolicy.setHeightForWidth(self.from_dateEdit.sizePolicy().hasHeightForWidth())
        self.from_dateEdit.setSizePolicy(sizePolicy)
        self.from_dateEdit.setFont(font)
        self.from_dateEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.from_dateEdit.setMinimumDateTime(QDateTime(QDate(2023, 9, 13), QTime(9, 0, 0)))
        self.from_dateEdit.setMinimumDate(QDate(2023, 9, 13))
        self.from_dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.from_dateEdit, 11, 1, 1, 2)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(13)
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 6)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 6)

        self.test_comboBox = QComboBox(self.frame)
        self.test_comboBox.addItem("")
        self.test_comboBox.setObjectName(u"test_comboBox")
        self.test_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.test_comboBox, 1, 0, 1, 6)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 6)

        self.version_os_comboBox = QComboBox(self.frame)
        self.version_os_comboBox.addItem("")
        self.version_os_comboBox.setObjectName(u"version_os_comboBox")
        self.version_os_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.version_os_comboBox, 3, 0, 1, 6)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_6, 11, 3, 1, 1)

        self.machine_comboBox = QComboBox(self.frame)
        self.machine_comboBox.addItem("")
        self.machine_comboBox.setObjectName(u"machine_comboBox")

        self.gridLayout.addWidget(self.machine_comboBox, 5, 0, 1, 6)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 6)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 6)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.parametrs_tests = QComboBox(self.frame)
        self.parametrs_tests.setObjectName(u"parametrs_tests")

        self.gridLayout.addWidget(self.parametrs_tests, 7, 0, 1, 6)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.accept_btn = QPushButton(self.frame)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setFont(font)
        self.accept_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.accept_btn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u0441\u0442", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0442\u0435\u0441\u0442\u043e\u0432", None))
        self.test_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435 \u0442\u0435\u0441\u0442\u044b", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.version_os_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435 \u0432\u0435\u0440\u0441\u0438\u0438", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e", None))
        self.machine_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435 \u043c\u0430\u0448\u0438\u043d\u044b", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0448\u0438\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0441\u0438\u044f \u041e\u0421\"\u0410\u0440\u0430\u043c\u0438\u0434\"", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442", None))
        self.accept_btn.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
    # retranslateUi

