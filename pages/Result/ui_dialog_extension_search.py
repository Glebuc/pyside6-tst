# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extension_search.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
        Dialog.resize(280, 380)
        Dialog.setMinimumSize(QSize(280, 380))
        Dialog.setMaximumSize(QSize(280, 380))
        Dialog.setStyleSheet(u"")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.N_comboBox = QComboBox(self.frame)
        self.N_comboBox.setObjectName(u"N_comboBox")
        self.N_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.N_comboBox, 6, 5, 1, 5)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 10)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 10)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 10)

        self.test_comboBox = QComboBox(self.frame)
        self.test_comboBox.setObjectName(u"test_comboBox")
        self.test_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.test_comboBox, 1, 0, 1, 10)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_6, 8, 4, 1, 1)

        self.from_dateEdit = QDateEdit(self.frame)
        self.from_dateEdit.setObjectName(u"from_dateEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.from_dateEdit.sizePolicy().hasHeightForWidth())
        self.from_dateEdit.setSizePolicy(sizePolicy2)
        self.from_dateEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.from_dateEdit.setMinimumDateTime(QDateTime(QDate(2023, 9, 13), QTime(9, 0, 0)))
        self.from_dateEdit.setMinimumDate(QDate(2023, 9, 13))

        self.gridLayout.addWidget(self.from_dateEdit, 8, 1, 1, 3)

        self.user_comboBox = QComboBox(self.frame)
        self.user_comboBox.setObjectName(u"user_comboBox")
        self.user_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.user_comboBox, 3, 0, 1, 10)

        self.before_dateEdit = QDateEdit(self.frame)
        self.before_dateEdit.setObjectName(u"before_dateEdit")
        sizePolicy2.setHeightForWidth(self.before_dateEdit.sizePolicy().hasHeightForWidth())
        self.before_dateEdit.setSizePolicy(sizePolicy2)
        self.before_dateEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.before_dateEdit.setMinimumDateTime(QDateTime(QDate(2023, 9, 13), QTime(9, 0, 0)))
        self.before_dateEdit.setMinimumDate(QDate(2023, 9, 13))

        self.gridLayout.addWidget(self.before_dateEdit, 8, 5, 1, 5)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 10)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_9, 5, 5, 1, 5)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 4)

        self.np_comboBox = QComboBox(self.frame)
        self.np_comboBox.setObjectName(u"np_comboBox")
        self.np_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.np_comboBox, 6, 0, 1, 4)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.accept_btn = QPushButton(self.frame)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.accept_btn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0442\u0435\u0441\u0442\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u0441\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044f\u0434\u0435\u0440", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0442\u043e\u043a\u043e\u0432", None))
        self.accept_btn.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
    # retranslateUi

