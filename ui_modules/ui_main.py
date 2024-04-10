# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"QFrame {\n"
"border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(130, 130, 130);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"	background-image: none;\n"
"}\n"
"\n"
"QGraphicsView {\n"
"	background-color: rgb(35, 40, 49);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(50, 54, 62);\n"
"	border: 2px solid rgb(30, 34, 42);\n"
"	padding:5px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 34, 42);\n"
"	border: 2px solid rgb(50, 54, 62);\n"
"}\n"
"QPush"
                        "Button:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	border-image: url(:/icons/images/icons/aramid.svg) 0 0 0 0 stretch stretch;\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#topLogoInfo {\n"
"background-color: rgb(119, 118, 123);\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	b"
                        "order: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	borde"
                        "r-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
""
                        "#extraCloseColumnBtn:hover { background-color: rgb(40, 44, 52); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(35, 40, 49); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { backgr"
                        "ound-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-"
                        "left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selec"
                        "tion-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    borde"
                        "r: none;\n"
"    background: rgb(150, 150, 150);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(130, 130, 130);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(100, 100, 100);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(100, 100, 100);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
""
                        "}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(220, 220, 220);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(50, 50, 50);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(200, 200, 200);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(200, 200, 200);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
                        "\n"
"     background: none;\n"
" }\n"
"QScrollArea {\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background:rgb(100, 100, 100);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
""
                        "    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255"
                        ");	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove"
                        ":vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(35, 40, 49);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
""
                        "#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#extraLeftBox QPushButton {\n"
"	background-color: rgb(35, 40, 49);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#result_page {\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"#chart_page{\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"#report_page{\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"#note_page {\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"#result_page QPushButton {\n"
"	background-color: rgb(35, 40, 49);\n"
"	padding: 5px;\n"
"}\n"
"#chart_page QPushButton {\n"
"	background-color: rgb(35, 40, 49);\n"
"	padding: 5px;\n"
"}\n"
"#note_page QPushButton {\n"
"	background-color: rgb(35, 40, 49);\n"
""
                        "	padding: 5px;\n"
"}\n"
"#report_page QPushButton {\n"
"	background-color: rgb(35, 40, 49);\n"
"	padding: 5px;\n"
"}\n"
"QTableView {\n"
"	background-color: rgb(35, 40, 49);\n"
"}\n"
"#pagesContainer  {\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"\n"
"#btn_report {\n"
"	background-image: url(:/icons/images/icons/cil-file.png);\n"
"}\n"
"#btn_bar {\n"
"background-image: url(:/icons/images/icons/cil-chart-pie.png);\n"
"}\n"
"#btn_result {\n"
"	background-image: url(:/icons/images/icons/cil-task.png);\n"
"}\n"
"#btn_note {\n"
"	background-image: url(:/icons/images/icons/cil-pen-alt.png);\n"
"}\n"
"#save_chart_btn{\n"
"	background-image: url(:/icons/images/icons/cil-save.png);\n"
"}\n"
"#zoom_in_chart_btn{\n"
"	background-image: url(:/icons/images/icons/cil-zoom-in.png);\n"
"}\n"
"#zoom_out_chart_btn{\n"
"	background-image: url(:/icons/images/icons/cil-zoom-out.png);\n"
"}\n"
"#up_chart_btn {\n"
"	background-image: url(:/icons/images/icons/cil-caret-top.png);\n"
"}\n"
"#down_chart_btn {\n"
"	background-imag"
                        "e: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"}\n"
"#left_chart_btn {\n"
"	background-image: url(:/icons/images/icons/cil-caret-left.png);\n"
"}\n"
"#right_chart_btn {\n"
"	background-image: url(:/icons/images/icons/cil-caret-right.png);\n"
"}\n"
"#reset_chart_btn{\n"
"	\n"
"	background-image: url(:/icons/images/icons/cil-loop-circular.png);\n"
"}\n"
"#list_test {\n"
"	color:#ffffff;\n"
"}\n"
"\n"
"#change_view_chart_btn {\n"
"	background-image: url(:/icons/images/icons/cil-settings.png);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.styleSheet)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 40))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 40))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.topLogoInfo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(35, 30))
        self.topLogo.setMaximumSize(QSize(30, 30))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.topLogo)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-right.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_report = QPushButton(self.topMenu)
        self.btn_report.setObjectName(u"btn_report")
        sizePolicy.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy)
        self.btn_report.setMinimumSize(QSize(0, 45))
        self.btn_report.setFont(font)
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_report.setLayoutDirection(Qt.LeftToRight)
        self.btn_report.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_report)

        self.btn_bar = QPushButton(self.topMenu)
        self.btn_bar.setObjectName(u"btn_bar")
        sizePolicy.setHeightForWidth(self.btn_bar.sizePolicy().hasHeightForWidth())
        self.btn_bar.setSizePolicy(sizePolicy)
        self.btn_bar.setMinimumSize(QSize(0, 45))
        self.btn_bar.setFont(font)
        self.btn_bar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bar.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.btn_bar)

        self.btn_result = QPushButton(self.topMenu)
        self.btn_result.setObjectName(u"btn_result")
        sizePolicy.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy)
        self.btn_result.setMinimumSize(QSize(0, 45))
        self.btn_result.setFont(font)
        self.btn_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_result.setLayoutDirection(Qt.LeftToRight)
        self.btn_result.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.btn_result)

        self.btn_note = QPushButton(self.topMenu)
        self.btn_note.setObjectName(u"btn_note")
        self.btn_note.setMinimumSize(QSize(0, 45))
        self.btn_note.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pen-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_note.setIcon(icon)

        self.verticalLayout_8.addWidget(self.btn_note)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"#toggleLeftBox {\n"
"background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"QToolTip {\n"
"background-image: none;\n"
"}")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 40))
        self.extraTopBg.setMaximumSize(QSize(16777215, 40))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_theme = QLabel(self.extraCenter)
        self.label_theme.setObjectName(u"label_theme")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_theme.sizePolicy().hasHeightForWidth())
        self.label_theme.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.label_theme)

        self.comboBox_theme = QComboBox(self.extraCenter)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        self.comboBox_theme.setFont(font)
        self.comboBox_theme.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_theme.setAutoFillBackground(False)
        self.comboBox_theme.setStyleSheet(u"")
        self.comboBox_theme.setIconSize(QSize(16, 16))
        self.comboBox_theme.setFrame(True)

        self.verticalLayout_10.addWidget(self.comboBox_theme)

        self.label_language = QLabel(self.extraCenter)
        self.label_language.setObjectName(u"label_language")
        sizePolicy1.setHeightForWidth(self.label_language.sizePolicy().hasHeightForWidth())
        self.label_language.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.label_language)

        self.comboBox_language = QComboBox(self.extraCenter)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")
        self.comboBox_language.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.comboBox_language)

        self.label_config = QLabel(self.extraCenter)
        self.label_config.setObjectName(u"label_config")
        sizePolicy1.setHeightForWidth(self.label_config.sizePolicy().hasHeightForWidth())
        self.label_config.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.label_config)

        self.btn_config_DB = QPushButton(self.extraCenter)
        self.btn_config_DB.setObjectName(u"btn_config_DB")
        self.btn_config_DB.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_config_DB.setIcon(icon2)

        self.verticalLayout_10.addWidget(self.btn_config_DB)

        self.label_extra = QLabel(self.extraCenter)
        self.label_extra.setObjectName(u"label_extra")
        sizePolicy1.setHeightForWidth(self.label_extra.sizePolicy().hasHeightForWidth())
        self.label_extra.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.label_extra)

        self.btn_user_guide = QPushButton(self.extraCenter)
        self.btn_user_guide.setObjectName(u"btn_user_guide")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_user_guide.sizePolicy().hasHeightForWidth())
        self.btn_user_guide.setSizePolicy(sizePolicy2)
        self.btn_user_guide.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btn_user_guide.setFont(font1)
        self.btn_user_guide.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user_guide.setIcon(icon3)

        self.verticalLayout_10.addWidget(self.btn_user_guide)

        self.btn_hot_keys = QPushButton(self.extraCenter)
        self.btn_hot_keys.setObjectName(u"btn_hot_keys")
        self.btn_hot_keys.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-keyboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_hot_keys.setIcon(icon4)

        self.verticalLayout_10.addWidget(self.btn_hot_keys)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraBottom)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_save_settings = QPushButton(self.extraBottom)
        self.btn_save_settings.setObjectName(u"btn_save_settings")
        self.btn_save_settings.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_save_settings)

        self.label_version_application = QLabel(self.extraBottom)
        self.label_version_application.setObjectName(u"label_version_application")
        sizePolicy1.setHeightForWidth(self.label_version_application.sizePolicy().hasHeightForWidth())
        self.label_version_application.setSizePolicy(sizePolicy1)
        self.label_version_application.setAlignment(Qt.AlignCenter)
        self.label_version_application.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_version_application)


        self.verticalLayout_12.addWidget(self.extraBottom, 0, Qt.AlignBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 5)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.verticalLayout_11 = QVBoxLayout(self.report_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.report_page)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)

        self.listView = QListView(self.report_page)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_11.addWidget(self.listView)

        self.pushButton_2 = QPushButton(self.report_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.report_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.report_page)
        self.chart_page = QWidget()
        self.chart_page.setObjectName(u"chart_page")
        self.chart_page.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.chart_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.chart_page)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.list_test_chart = QComboBox(self.frame_3)
        self.list_test_chart.setObjectName(u"list_test_chart")
        self.list_test_chart.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.list_test_chart)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.label_3)

        self.list_param_test = QComboBox(self.frame_3)
        self.list_param_test.setObjectName(u"list_param_test")
        self.list_param_test.setMinimumSize(QSize(170, 0))
        self.list_param_test.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.list_param_test)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.change_view_chart_btn = QPushButton(self.frame_3)
        self.change_view_chart_btn.setObjectName(u"change_view_chart_btn")
        self.change_view_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.change_view_chart_btn)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_chart = QFrame(self.chart_page)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setMinimumSize(QSize(0, 150))
        self.frame_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_chart)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_2 = QFrame(self.frame_chart)
        self.frame_chart_2.setObjectName(u"frame_chart_2")
        self.frame_chart_2.setMinimumSize(QSize(400, 0))
        self.frame_chart_2.setFrameShape(QFrame.StyledPanel)
        self.frame_chart_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_chart_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_chart_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(50, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 5, 0)
        self.up_chart_btn = QPushButton(self.frame_5)
        self.up_chart_btn.setObjectName(u"up_chart_btn")
        self.up_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.up_chart_btn)

        self.down_chart_btn = QPushButton(self.frame_5)
        self.down_chart_btn.setObjectName(u"down_chart_btn")
        self.down_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.down_chart_btn)

        self.right_chart_btn = QPushButton(self.frame_5)
        self.right_chart_btn.setObjectName(u"right_chart_btn")
        self.right_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.right_chart_btn)

        self.left_chart_btn = QPushButton(self.frame_5)
        self.left_chart_btn.setObjectName(u"left_chart_btn")
        self.left_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.left_chart_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.zoom_out_chart_btn = QPushButton(self.frame_5)
        self.zoom_out_chart_btn.setObjectName(u"zoom_out_chart_btn")
        self.zoom_out_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.zoom_out_chart_btn)

        self.zoom_in_chart_btn = QPushButton(self.frame_5)
        self.zoom_in_chart_btn.setObjectName(u"zoom_in_chart_btn")
        self.zoom_in_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.zoom_in_chart_btn)

        self.reset_chart_btn = QPushButton(self.frame_5)
        self.reset_chart_btn.setObjectName(u"reset_chart_btn")
        self.reset_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.reset_chart_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.save_chart_btn = QPushButton(self.frame_5)
        self.save_chart_btn.setObjectName(u"save_chart_btn")
        self.save_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.save_chart_btn)


        self.horizontalLayout_10.addWidget(self.frame_5)

        self.graphicsView = QChartView(self.frame_chart_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_10.addWidget(self.graphicsView)


        self.horizontalLayout_12.addWidget(self.frame_chart_2)


        self.verticalLayout.addWidget(self.frame_chart)

        self.stackedWidget.addWidget(self.chart_page)
        self.result_page = QWidget()
        self.result_page.setObjectName(u"result_page")
        self.verticalLayout_20 = QVBoxLayout(self.result_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.result_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.list_test_result = QComboBox(self.frame)
        self.list_test_result.setObjectName(u"list_test_result")
        self.list_test_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.list_test_result.setFrame(False)

        self.horizontalLayout_7.addWidget(self.list_test_result)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_extension_search = QPushButton(self.frame)
        self.btn_extension_search.setObjectName(u"btn_extension_search")
        self.btn_extension_search.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extension_search.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.btn_extension_search)


        self.verticalLayout_20.addWidget(self.frame)

        self.resultView = QTableView(self.result_page)
        self.resultView.setObjectName(u"resultView")
        self.resultView.setSortingEnabled(True)

        self.verticalLayout_20.addWidget(self.resultView)

        self.frame_2 = QFrame(self.result_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.btn_change_view = QPushButton(self.frame_2)
        self.btn_change_view.setObjectName(u"btn_change_view")
        self.btn_change_view.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-equalizer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_change_view.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.btn_change_view)

        self.btn_save_view = QPushButton(self.frame_2)
        self.btn_save_view.setObjectName(u"btn_save_view")
        self.btn_save_view.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_view.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.btn_save_view)


        self.verticalLayout_20.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.result_page)
        self.note_page = QWidget()
        self.note_page.setObjectName(u"note_page")
        self.verticalLayout_14 = QVBoxLayout(self.note_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 9, 0, 0)
        self.frame_4 = QFrame(self.note_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_14.addWidget(self.frame_4)

        self.scrollArea = QScrollArea(self.note_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 858, 464))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.treeWidget = QTreeWidget(self.scrollAreaWidgetContents)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setBackground(0, QColor(104, 104, 104));
        __qtreewidgetitem.setForeground(0, brush);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"color:#000")

        self.verticalLayout_16.addWidget(self.treeWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.note_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 15))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 10))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.creditsLabel.setFont(font2)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_3.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.comboBox_theme.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
#if QT_CONFIG(shortcut)
        self.toggleButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_report.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
#if QT_CONFIG(shortcut)
        self.btn_report.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_bar.setToolTip(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.btn_bar.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
#if QT_CONFIG(shortcut)
        self.btn_bar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_result.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.btn_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
#if QT_CONFIG(shortcut)
        self.btn_result.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_note.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
#if QT_CONFIG(shortcut)
        self.btn_note.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.toggleLeftBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#if QT_CONFIG(shortcut)
        self.toggleLeftBox.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.label_theme.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))

        self.label_language.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))

        self.label_config.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u0411\u0414", None))
        self.btn_config_DB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u0411\u0414", None))
        self.label_extra.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.btn_user_guide.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.btn_hot_keys.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.btn_save_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_version_application.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f Aramid TsT Graph v0.0.1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0447\u0435\u0442\u043e\u0432", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0442\u0435\u0441\u0442\u0430:", None))
#if QT_CONFIG(tooltip)
        self.change_view_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.change_view_chart_btn.setText("")
#if QT_CONFIG(tooltip)
        self.up_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u043d\u0430\u0432\u0435\u0440\u0445", None))
#endif // QT_CONFIG(tooltip)
        self.up_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.up_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Up", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.down_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432\u043d\u0438\u0437", None))
#endif // QT_CONFIG(tooltip)
        self.down_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.down_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Down", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.right_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432\u043f\u0440\u0430\u0432\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.right_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.right_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.left_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432\u043b\u0435\u0432\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.left_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.left_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Left", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.zoom_out_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u044c \u043c\u0430\u0441\u0448\u0442\u0430\u0431", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_out_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.zoom_out_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.zoom_in_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c \u043c\u0430\u0441\u0448\u0442\u0430\u0431", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_in_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.zoom_in_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+=", None))
#endif // QT_CONFIG(shortcut)
        self.reset_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.reset_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+/", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.save_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
#endif // QT_CONFIG(tooltip)
        self.save_chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.save_chart_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442: ", None))
        self.btn_extension_search.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
#if QT_CONFIG(tooltip)
        self.btn_change_view.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_change_view.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.btn_save_view.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c..", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b...", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u044c\u044e...", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u044b", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"HPCG", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"IMB", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"HPL", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"b_eff", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"STREAM", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"IOZONE", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem1.child(6)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"SPEC HPC", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem1.child(7)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"IO-500", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u0442\u0435\u0441\u0442\u043e\u0432", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043d\u0430\u0438\u043b\u0443\u0447\u0448\u0438\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0434\u043b\u044f HPL", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

