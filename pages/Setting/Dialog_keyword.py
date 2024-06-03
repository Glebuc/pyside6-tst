# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keywords.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHeaderView, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 300)
        Dialog.setMinimumSize(QSize(450, 300))
        Dialog.setMaximumSize(QSize(450, 300))
        Dialog.setStyleSheet(u"")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255, 0));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 1, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(8)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'Q'", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0443 \"\u041e\u0442\u0447\u0435\u0442\u043e\u0432\"", None));
        ___qtablewidgetitem4 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'-'", None));
        ___qtablewidgetitem5 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u0423\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u044c \u043c\u0430\u0441\u0448\u0442\u0430\u0431 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None));
        ___qtablewidgetitem6 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'='", None));
        ___qtablewidgetitem7 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c \u043c\u0430\u0441\u0448\u0442\u0430\u0431 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None));
        ___qtablewidgetitem8 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'W'", None));
        ___qtablewidgetitem9 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0443 \"\u0413\u0440\u0430\u0444\u0438\u043a\u0438\"", None));
        ___qtablewidgetitem10 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'E'", None));
        ___qtablewidgetitem11 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0443 \"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b\"", None));
        ___qtablewidgetitem12 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'R'", None));
        ___qtablewidgetitem13 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0443 \"\u0417\u0430\u043c\u0435\u0442\u043a\u0438\"", None));
        ___qtablewidgetitem14 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"'Ctrl'+'T'", None));
        ___qtablewidgetitem15 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0443 \"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438\"", None));
        ___qtablewidgetitem16 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"Ctrl+'Space'", None));
        ___qtablewidgetitem17 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c/\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043c\u0435\u043d\u044e", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

