# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_config_db.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 400)
        Dialog.setMinimumSize(QSize(350, 400))
        Dialog.setMaximumSize(QSize(350, 400))
        Dialog.setStyleSheet(u"")
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.name_db_edit = QLineEdit(self.frame)
        self.name_db_edit.setObjectName(u"name_db_edit")

        self.verticalLayout_2.addWidget(self.name_db_edit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.user_db_edit = QLineEdit(self.frame)
        self.user_db_edit.setObjectName(u"user_db_edit")

        self.verticalLayout_2.addWidget(self.user_db_edit)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_3)

        self.password_db_edit = QLineEdit(self.frame)
        self.password_db_edit.setObjectName(u"password_db_edit")
        self.password_db_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_db_edit)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_4)

        self.port_db_spin = QSpinBox(self.frame)
        self.port_db_spin.setObjectName(u"port_db_spin")
        self.port_db_spin.setMaximum(1000000)
        self.port_db_spin.setValue(5432)

        self.verticalLayout_2.addWidget(self.port_db_spin)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_5)

        self.host_db_edit = QLineEdit(self.frame)
        self.host_db_edit.setObjectName(u"host_db_edit")

        self.verticalLayout_2.addWidget(self.host_db_edit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.submit_db_param_btn = QPushButton(self.frame)
        self.submit_db_param_btn.setObjectName(u"submit_db_param_btn")
        self.submit_db_param_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.submit_db_param_btn)

        self.check_connect_db_btn = QPushButton(self.frame)
        self.check_connect_db_btn.setObjectName(u"check_connect_db_btn")
        self.check_connect_db_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.check_connect_db_btn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u0411\u0414:", None))
        self.name_db_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0411\u0414", None))
        self.user_db_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0411\u0414:", None))
        self.password_db_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u0442 \u0411\u0414:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0425\u043e\u0441\u0442 \u0411\u0414:", None))
        self.host_db_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0425\u043e\u0441\u0442 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445...", None))
        self.submit_db_param_btn.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.check_connect_db_btn.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435", None))
    # retranslateUi

