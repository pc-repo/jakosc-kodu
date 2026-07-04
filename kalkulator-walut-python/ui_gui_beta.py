# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_beta.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateTimeEdit,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, CalcYea):
        if not CalcYea.objectName():
            CalcYea.setObjectName(u"CalcYea")
        CalcYea.resize(1084, 431)
        CalcYea.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(31, 31, 0);\n"
"color: white;")
        self.centralwidget = QWidget(CalcYea)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.blok1 = QWidget(self.widget1)
        self.blok1.setObjectName(u"blok1")
        self.blok1.setGeometry(QRect(10, 30, 250, 321))
        self.blok1.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.blok1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.marzaS = QLabel(self.blok1)
        self.marzaS.setObjectName(u"marzaS")
        self.marzaS.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.marzaS, 0, Qt.AlignHCenter)

        self.inputS = QLineEdit(self.blok1)
        self.inputS.setObjectName(u"inputS")
        self.inputS.setStyleSheet(u" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")
        self.inputS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.inputS)

        self.kwota = QLabel(self.blok1)
        self.kwota.setObjectName(u"kwota")

        self.verticalLayout_2.addWidget(self.kwota, 0, Qt.AlignHCenter)

        self.inputKota = QLineEdit(self.blok1)
        self.inputKota.setObjectName(u"inputKota")
        self.inputKota.setStyleSheet(u"padding: 10px 0 10px 0;\n"
" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")
        self.inputKota.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.inputKota)

        self.marzaK = QLabel(self.blok1)
        self.marzaK.setObjectName(u"marzaK")

        self.verticalLayout_2.addWidget(self.marzaK, 0, Qt.AlignHCenter)

        self.inputK = QLineEdit(self.blok1)
        self.inputK.setObjectName(u"inputK")
        self.inputK.setStyleSheet(u" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")
        self.inputK.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.inputK)

        self.blok2 = QWidget(self.widget1)
        self.blok2.setObjectName(u"blok2")
        self.blok2.setGeometry(QRect(280, 30, 250, 321))
        self.blok2.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.blok2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.wartoscS = QLabel(self.blok2)
        self.wartoscS.setObjectName(u"wartoscS")

        self.verticalLayout_5.addWidget(self.wartoscS, 0, Qt.AlignHCenter)

        self.inputS_2 = QLineEdit(self.blok2)
        self.inputS_2.setObjectName(u"inputS_2")
        self.inputS_2.setStyleSheet(u" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")
        self.inputS_2.setAlignment(Qt.AlignCenter)
        self.inputS_2.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.inputS_2)

        self.wartoscP = QLabel(self.blok2)
        self.wartoscP.setObjectName(u"wartoscP")

        self.verticalLayout_5.addWidget(self.wartoscP, 0, Qt.AlignHCenter)

        self.inputWartosc = QLineEdit(self.blok2)
        self.inputWartosc.setObjectName(u"inputWartosc")
        self.inputWartosc.setStyleSheet(u"padding: 10px 0 10px 0;\n"
" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")
        self.inputWartosc.setAlignment(Qt.AlignCenter)
        self.inputWartosc.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.inputWartosc)

        self.wartoscK = QLabel(self.blok2)
        self.wartoscK.setObjectName(u"wartoscK")

        self.verticalLayout_5.addWidget(self.wartoscK, 0, Qt.AlignHCenter)

        self.inputK_2 = QLineEdit(self.blok2)
        self.inputK_2.setObjectName(u"inputK_2")
        self.inputK_2.setStyleSheet(u" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")
        self.inputK_2.setAlignment(Qt.AlignCenter)
        self.inputK_2.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.inputK_2)


        self.horizontalLayout.addWidget(self.widget1)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.blok3 = QWidget(self.widget2)
        self.blok3.setObjectName(u"blok3")
        self.blok3.setGeometry(QRect(50, 40, 468, 351))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.blok3.setFont(font)
        self.verticalLayout = QVBoxLayout(self.blok3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_10 = QWidget(self.blok3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(450, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.synchroBtn = QPushButton(self.widget_10)
        self.synchroBtn.setObjectName(u"synchroBtn")
        self.synchroBtn.setMinimumSize(QSize(420, 0))
        self.synchroBtn.setMaximumSize(QSize(100, 16777215))
        self.synchroBtn.setFont(font)
        self.synchroBtn.setStyleSheet(u"padding-top: 10px;\n"
"border-color: rgb(255, 255, 255);\n"
"padding-bottom: 10px;\n"
"\n"
" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")

        self.horizontalLayout_4.addWidget(self.synchroBtn)


        self.verticalLayout.addWidget(self.widget_10)

        self.widget_7 = QWidget(self.blok3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(450, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateNow = QDateTimeEdit(self.widget_7)
        self.dateNow.setObjectName(u"dateNow")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateNow.sizePolicy().hasHeightForWidth())
        self.dateNow.setSizePolicy(sizePolicy)
        self.dateNow.setMinimumSize(QSize(200, 0))
        self.dateNow.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(31, 31, 0);\n"
"border: none;\n"
"padding-left: 33px;")
        self.dateNow.setReadOnly(True)
        self.dateNow.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_3.addWidget(self.dateNow)

        self.dateKurs = QDateTimeEdit(self.widget_7)
        self.dateKurs.setObjectName(u"dateKurs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateKurs.sizePolicy().hasHeightForWidth())
        self.dateKurs.setSizePolicy(sizePolicy1)
        self.dateKurs.setMinimumSize(QSize(200, 0))
        self.dateKurs.setFont(font)
        self.dateKurs.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(31, 31, 0);\n"
"border: none;")
        self.dateKurs.setReadOnly(True)
        self.dateKurs.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateKurs.setMinimumDate(QDate(1752, 9, 15))
        self.dateKurs.setMinimumTime(QTime(0, 0, 0))
        self.dateKurs.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateKurs.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_3.addWidget(self.dateKurs, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.widget_7)

        self.widget_5 = QWidget(self.blok3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(450, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(160, 0))
        self.widget_6.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioPLN = QRadioButton(self.widget_6)
        self.radioPLN.setObjectName(u"radioPLN")
        self.radioPLN.setFont(font)

        self.verticalLayout_3.addWidget(self.radioPLN)

        self.radioObca = QRadioButton(self.widget_6)
        self.radioObca.setObjectName(u"radioObca")
        self.radioObca.setFont(font)

        self.verticalLayout_3.addWidget(self.radioObca)


        self.horizontalLayout_2.addWidget(self.widget_6)

        self.listaWalut = QComboBox(self.widget_5)
        self.listaWalut.setObjectName(u"listaWalut")
        sizePolicy1.setHeightForWidth(self.listaWalut.sizePolicy().hasHeightForWidth())
        self.listaWalut.setSizePolicy(sizePolicy1)
        self.listaWalut.setMinimumSize(QSize(0, 35))
        self.listaWalut.setMaximumSize(QSize(250, 16777215))
        self.listaWalut.setStyleSheet(u"""
    QComboBox {
        font: 75 12pt "MS Shell Dlg 2";
        background-color: rgb(31, 31, 0);
        border: white 2px solid;
        padding-left: 10px; /* Dodatkowy padding, jeśli tekst zaczyna się za blisko krawędzi */
    }

    QComboBox::drop-down {
        /* Stylizuje strzałkę rozwijającą listę, aby nie zakłócać centrowania tekstu */
        border: none; /* Usuwa domyślną ramkę wokół strzałki */
    }

    QComboBox QAbstractItemView {
        text-align: right; /* Wyśrodkowuje tekst w elementach listy rozwijanej */
        selection-background-color: rgb(50, 50, 50); /* Kolor tła wybranego elementu na liście */
        color: white; /* Kolor tekstu elementów listy */
        background-color: rgb(31, 31, 0); /* Kolor tła całej listy rozwijanej */
    }
""")
        self.horizontalLayout_2.addWidget(self.listaWalut)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.blok3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(450, 0))
        self.widget_3.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.convertBtn = QPushButton(self.widget_3)
        self.convertBtn.setObjectName(u"convertBtn")
        self.convertBtn.setMinimumSize(QSize(170, 0))
        self.convertBtn.setMaximumSize(QSize(120, 16777215))
        self.convertBtn.setFont(font)
        self.convertBtn.setStyleSheet(u"padding-top: 10px;\n"
"border-color: rgb(255, 255, 255);\n"
"padding-bottom: 10px;\n"
"\n"
" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")

        self.horizontalLayout_5.addWidget(self.convertBtn, 0, Qt.AlignLeft)

        self.exitBtn = QPushButton(self.widget_3)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMaximumSize(QSize(170, 16777215))
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(u"padding-top: 10px;\n"
"padding-bottom: 10px;\n"
"\n"
" border-style: outset;\n"
" border-width: 2px;\n"
" border-color: white;")

        self.horizontalLayout_5.addWidget(self.exitBtn)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget2)

        CalcYea.setCentralWidget(self.centralwidget)

        self.retranslateUi(CalcYea)

        QMetaObject.connectSlotsByName(CalcYea)
    # setupUi

    def retranslateUi(self, CalcYea):
        CalcYea.setWindowTitle(QCoreApplication.translate("CalcYea", u"MainWindow", None))
        self.marzaS.setText(QCoreApplication.translate("CalcYea", u"Mar\u017ca sprzeda\u017cy", None))
        self.inputS.setPlaceholderText(QCoreApplication.translate("CalcYea", u"1.0000", None))
        self.kwota.setText(QCoreApplication.translate("CalcYea", u"Kwota do przeliczenia", None))
        self.marzaK.setText(QCoreApplication.translate("CalcYea", u"Mar\u017ca kupna", None))
        self.inputK.setPlaceholderText(QCoreApplication.translate("CalcYea", u"1.0000", None))
        self.wartoscS.setText(QCoreApplication.translate("CalcYea", u"Warto\u015b\u0107 sprzeda\u017cy", None))
        self.wartoscP.setText(QCoreApplication.translate("CalcYea", u"Warto\u015b\u0107 w przeliczeniu", None))
        self.wartoscK.setText(QCoreApplication.translate("CalcYea", u"Warto\u015b\u0107c kupna", None))
        self.synchroBtn.setText(QCoreApplication.translate("CalcYea", u"SYNCHRONIZUJ", None))
        self.radioPLN.setText(QCoreApplication.translate("CalcYea", u"Obca na PLN", None))
        self.radioObca.setText(QCoreApplication.translate("CalcYea", u"PLN na obc\u0105", None))
#if QT_CONFIG(accessibility)
        self.listaWalut.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.convertBtn.setText(QCoreApplication.translate("CalcYea", u"POLICZ", None))
        self.exitBtn.setText(QCoreApplication.translate("CalcYea", u"WYJD\u0179", None))
    # retranslateUi

