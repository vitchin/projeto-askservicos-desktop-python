# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignAsk.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        if not JanelaPrincipal.objectName():
            JanelaPrincipal.setObjectName(u"JanelaPrincipal")
        JanelaPrincipal.resize(801, 663)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JanelaPrincipal.sizePolicy().hasHeightForWidth())
        JanelaPrincipal.setSizePolicy(sizePolicy)
        JanelaPrincipal.setMinimumSize(QSize(0, 600))
        JanelaPrincipal.setMaximumSize(QSize(16777215, 663))
        JanelaPrincipal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(JanelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameAcimaDeTodos = QFrame(self.centralwidget)
        self.FrameAcimaDeTodos.setObjectName(u"FrameAcimaDeTodos")
        self.FrameAcimaDeTodos.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;\n"
"background-color: rgb(24, 12, 59);")
        self.FrameAcimaDeTodos.setFrameShape(QFrame.StyledPanel)
        self.FrameAcimaDeTodos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FrameAcimaDeTodos)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.FrameAcimaDeTodos)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 0, 10)
        self.Titulo = QLabel(self.frame_12)
        self.Titulo.setObjectName(u"Titulo")
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        font.setPointSize(16)
        font.setBold(False)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(135, 163, 255);")
        self.Titulo.setTextFormat(Qt.PlainText)
        self.Titulo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.Titulo)

        self.Titulo_2 = QLabel(self.frame_12)
        self.Titulo_2.setObjectName(u"Titulo_2")
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.Titulo_2.setFont(font1)
        self.Titulo_2.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Titulo_2.setTextFormat(Qt.PlainText)
        self.Titulo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.Titulo_2)


        self.horizontalLayout.addWidget(self.frame_12)

        self.horizontalSpacer = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCasa = QPushButton(self.FrameAcimaDeTodos)
        self.btnCasa.setObjectName(u"btnCasa")
        sizePolicy.setHeightForWidth(self.btnCasa.sizePolicy().hasHeightForWidth())
        self.btnCasa.setSizePolicy(sizePolicy)
        self.btnCasa.setMinimumSize(QSize(100, 0))
        self.btnCasa.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Leelawadee UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.btnCasa.setFont(font2)
        self.btnCasa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCasa.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	color: \"white\";\n"
"	letter-spacing:1px;\n"
"	font-weight: 500;\n"
"	background-color: transparent;\n"
"	font: \"Leelawadee\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}")

        self.horizontalLayout.addWidget(self.btnCasa)

        self.btnSobre = QPushButton(self.FrameAcimaDeTodos)
        self.btnSobre.setObjectName(u"btnSobre")
        sizePolicy.setHeightForWidth(self.btnSobre.sizePolicy().hasHeightForWidth())
        self.btnSobre.setSizePolicy(sizePolicy)
        self.btnSobre.setMinimumSize(QSize(100, 0))
        self.btnSobre.setMaximumSize(QSize(100, 16777215))
        self.btnSobre.setFont(font2)
        self.btnSobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSobre.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	color: \"white\";\n"
"	letter-spacing:1px;\n"
"	font-weight: 500;\n"
"	background-color: transparent;\n"
"	font: \"Leelawadee\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}")

        self.horizontalLayout.addWidget(self.btnSobre)

        self.btnContato = QPushButton(self.FrameAcimaDeTodos)
        self.btnContato.setObjectName(u"btnContato")
        sizePolicy.setHeightForWidth(self.btnContato.sizePolicy().hasHeightForWidth())
        self.btnContato.setSizePolicy(sizePolicy)
        self.btnContato.setMinimumSize(QSize(100, 0))
        self.btnContato.setMaximumSize(QSize(100, 16777215))
        self.btnContato.setFont(font2)
        self.btnContato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnContato.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	color: \"white\";\n"
"	letter-spacing:1px;\n"
"	font-weight: 500;\n"
"	background-color: transparent;\n"
"	font: \"Leelawadee\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}")

        self.horizontalLayout.addWidget(self.btnContato)


        self.verticalLayout.addWidget(self.FrameAcimaDeTodos)

        self.Paginas = QStackedWidget(self.centralwidget)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setMaximumSize(QSize(16777211, 16777215))
        self.Paginas.setStyleSheet(u"border-radius:2px;\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(0, 16, 223, 0), stop:0.994318 rgba(105, 80, 219, 0));\n"
"")
        self.pg_inicial = QWidget()
        self.pg_inicial.setObjectName(u"pg_inicial")
        self.verticalLayout_2 = QVBoxLayout(self.pg_inicial)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.FrameSearch = QFrame(self.pg_inicial)
        self.FrameSearch.setObjectName(u"FrameSearch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FrameSearch.sizePolicy().hasHeightForWidth())
        self.FrameSearch.setSizePolicy(sizePolicy1)
        self.FrameSearch.setLayoutDirection(Qt.LeftToRight)
        self.FrameSearch.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);")
        self.FrameSearch.setFrameShape(QFrame.StyledPanel)
        self.FrameSearch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameSearch)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnPesquisar = QPushButton(self.FrameSearch)
        self.btnPesquisar.setObjectName(u"btnPesquisar")
        font3 = QFont()
        font3.setFamilies([u"Leelawadee UI"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.btnPesquisar.setFont(font3)
        self.btnPesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPesquisar.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius: 0px;	\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnPesquisar)

        self.CampoPesquisa = QLineEdit(self.FrameSearch)
        self.CampoPesquisa.setObjectName(u"CampoPesquisa")
        self.CampoPesquisa.setMinimumSize(QSize(0, 40))
        self.CampoPesquisa.setMaximumSize(QSize(16777215, 40))
        self.CampoPesquisa.setFont(font3)
        self.CampoPesquisa.setStyleSheet(u"margin: 0px;\n"
"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:0px;")
        self.CampoPesquisa.setMaxLength(50)
        self.CampoPesquisa.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.CampoPesquisa)

        self.btnCadastrar = QPushButton(self.FrameSearch)
        self.btnCadastrar.setObjectName(u"btnCadastrar")
        self.btnCadastrar.setFont(font3)
        self.btnCadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCadastrar.setLayoutDirection(Qt.LeftToRight)
        self.btnCadastrar.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-top-left-radius:0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnCadastrar)
        self.verticalLayout_2.addWidget(self.FrameSearch)

        self.tb_usuarios = QTableWidget(self.pg_inicial)
        if (self.tb_usuarios.columnCount() < 10):
            self.tb_usuarios.setColumnCount(10)
            
        font4 = QFont()
        font4.setFamilies([u"Leelawadee UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font4);
        self.tb_usuarios.setColumnHidden(0, True)
        self.tb_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font5 = QFont()
        font5.setFamilies([u"Leelawadee UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font5);
        self.tb_usuarios.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tb_usuarios.setObjectName(u"tb_usuarios")
        sizePolicy.setHeightForWidth(self.tb_usuarios.sizePolicy().hasHeightForWidth())
        self.tb_usuarios.setSizePolicy(sizePolicy)

        self.tb_usuarios.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tb_usuarios.setStyleSheet(u"QHeaderView:section{\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: transparent;\n"
"	border-right: 1px solid rgb(199, 199, 199);\n"
"	border-bottom: 1px solid rgb(199, 199, 199);\n"
"}\n"
"QHeaderView:section:hover{\n"
"	background-color: rgb(231, 231, 239);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(199, 199, 199);\n"
"}\n"
"\n"
"/*Mexendo no scrollbar*/\n"
"\n"
"QScrollBar:horizontal{\n"
"	border: transparent;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(231, 231, 239);\n"
"	height: 13px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(24, 12, 59);\n"
"	/*min-height: 10px;*/\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"\n"
"/*Mexendo na seta direita*/\n"
"QScollBar::sub-line:horizontal{\n"
"	border:transparent;\n"
"	background-color: rgba(203, 204, 210, 150);\n"
"	height: 15px;\n"
"	bor"
                        "der-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScollBar::sub-line:horizontal:hover {\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"\n"
"/*Mexendo na seta esquerda*/\n"
"QScollBar::add-line:vertical {\n"
"	border:none;\n"
"    background-color: rgba(203, 204, 210, 150);		\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScollBar::add-line:horizontal:hover {\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"\n"
"/*Mexendo nas setas direita e esquerda*/\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                        " stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.tb_usuarios.horizontalHeader().setMinimumSectionSize(120)
        self.tb_usuarios.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.tb_usuarios)

        self.Paginas.addWidget(self.pg_inicial)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_sobre)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.pg_sobre)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.ConteudoSobre = QTextBrowser(self.frame_5)
        self.ConteudoSobre.setObjectName(u"ConteudoSobre")
        font6 = QFont()
        font6.setFamilies([u"Leelawadee UI"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.ConteudoSobre.setFont(font6)
        self.ConteudoSobre.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.ConteudoSobre.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"color: rgb(21, 21, 21);\n"
"border: 1px solid rgb(199, 199, 199);\n"
"border-radius:10px;\n"
"font: \"Leelawadee UI\";")

        self.verticalLayout_3.addWidget(self.ConteudoSobre)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.Paginas.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_contato)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.pg_contato)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.ConteudoContato = QTextBrowser(self.frame_4)
        self.ConteudoContato.setObjectName(u"ConteudoContato")
        font7 = QFont()
        font7.setFamilies([u"Liberation Sans"])
        font7.setBold(False)
        font7.setItalic(False)
        self.ConteudoContato.setFont(font7)
        self.ConteudoContato.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.ConteudoContato.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"color: rgb(21, 21, 21);\n"
"border: 1px solid rgb(199, 199, 199);\n"
"border-radius:10px;\n"
"font: \"Leelawadee UI\";")

        self.verticalLayout_6.addWidget(self.ConteudoContato)


        self.horizontalLayout_7.addWidget(self.frame_4)

        self.Paginas.addWidget(self.pg_contato)
        self.pg_escolha = QWidget()
        self.pg_escolha.setObjectName(u"pg_escolha")
        self.horizontalLayout_10 = QHBoxLayout(self.pg_escolha)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.pg_escolha)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMinimumSize(QSize(300, 250))
        self.frame_9.setMaximumSize(QSize(300, 250))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"color: rgb(21, 21, 21);\n"
"border: 1px solid rgb(199, 199, 199);\n"
"border-radius:10px;\n"
"font: \"Leelawadee UI\";")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;\n"
"border-radius: 0px;\n"
"border-bottom: 1px solid \"grey\";")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_18)

        self.btnAnunciar = QPushButton(self.frame_9)
        self.btnAnunciar.setObjectName(u"btnAnunciar")
        self.btnAnunciar.setMinimumSize(QSize(0, 45))
        self.btnAnunciar.setMaximumSize(QSize(16777215, 45))
        self.btnAnunciar.setFont(font2)
        self.btnAnunciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnunciar.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btnAnunciar)

        self.btnSolicitar = QPushButton(self.frame_9)
        self.btnSolicitar.setObjectName(u"btnSolicitar")
        self.btnSolicitar.setMinimumSize(QSize(0, 45))
        self.btnSolicitar.setMaximumSize(QSize(16777215, 45))
        self.btnSolicitar.setFont(font2)
        self.btnSolicitar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSolicitar.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btnSolicitar)

        self.btnVoltarInicio = QPushButton(self.frame_9)
        self.btnVoltarInicio.setObjectName(u"btnVoltarInicio")
        self.btnVoltarInicio.setMinimumSize(QSize(0, 45))
        self.btnVoltarInicio.setMaximumSize(QSize(16777215, 45))
        self.btnVoltarInicio.setFont(font2)
        self.btnVoltarInicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVoltarInicio.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btnVoltarInicio)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.Paginas.addWidget(self.pg_escolha)
        self.pg_cliente = QWidget()
        self.pg_cliente.setObjectName(u"pg_cliente")
        self.pg_cliente.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.pg_cliente)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.pg_cliente)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMinimumSize(QSize(350, 385))
        self.frame_7.setMaximumSize(QSize(350, 385))
        self.frame_7.setStyleSheet(u"margin: 0px;\n"
"padding: 10px;\n"
"border: transparent;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 21, 21);\n"
"border: 1px solid rgb(199, 199, 199);\n"
"border-radius:10px;\n"
"font: \"Leelawadee UI\";")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setFamilies([u"Liberation Sans"])
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"margin: 0px;\n"
"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;\n"
"border-radius: 0px;\n"
"border-bottom: 1px solid \"grey\";\n"
"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_17)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_9.addWidget(self.label_12)

        self.txtNomeCliente = QLineEdit(self.frame_7)
        self.txtNomeCliente.setObjectName(u"txtNomeCliente")
        self.txtNomeCliente.setMinimumSize(QSize(0, 35))
        self.txtNomeCliente.setMaximumSize(QSize(16777215, 35))
        self.txtNomeCliente.setFont(font2)
        self.txtNomeCliente.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtNomeCliente.setMaxLength(32767)
        self.txtNomeCliente.setFrame(True)
        self.txtNomeCliente.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.txtNomeCliente)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_9.addWidget(self.label_13)

        self.txtEmailCliente = QLineEdit(self.frame_7)
        self.txtEmailCliente.setObjectName(u"txtEmailCliente")
        self.txtEmailCliente.setMinimumSize(QSize(0, 35))
        self.txtEmailCliente.setMaximumSize(QSize(16777215, 35))
        self.txtEmailCliente.setFont(font2)
        self.txtEmailCliente.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtEmailCliente.setMaxLength(50)
        self.txtEmailCliente.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.txtEmailCliente)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_9.addWidget(self.label_14)

        self.txtTelefoneCliente = QLineEdit(self.frame_7)
        self.txtTelefoneCliente.setObjectName(u"txtTelefoneCliente")
        self.txtTelefoneCliente.setMinimumSize(QSize(0, 35))
        self.txtTelefoneCliente.setMaximumSize(QSize(16777215, 35))
        self.txtTelefoneCliente.setFont(font2)
        self.txtTelefoneCliente.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtTelefoneCliente.setMaxLength(9)
        self.txtTelefoneCliente.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.txtTelefoneCliente)

        self.splitter = QSplitter(self.frame_7)
        self.splitter.setObjectName(u"splitter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy4)
        self.splitter.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_10 = QFrame(self.splitter)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_5.addWidget(self.label_19)

        self.txtSenhaCliente = QLineEdit(self.frame_10)
        self.txtSenhaCliente.setObjectName(u"txtSenhaCliente")
        self.txtSenhaCliente.setMinimumSize(QSize(0, 35))
        self.txtSenhaCliente.setMaximumSize(QSize(16777215, 35))
        self.txtSenhaCliente.setFont(font2)
        self.txtSenhaCliente.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtSenhaCliente.setMaxLength(5)
        self.txtSenhaCliente.setEchoMode(QLineEdit.Password)
        self.txtSenhaCliente.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.txtSenhaCliente)

        self.splitter.addWidget(self.frame_10)
        self.frame_11 = QFrame(self.splitter)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_8.addWidget(self.label_20)

        self.txtConfirmarSenhaCliente = QLineEdit(self.frame_11)
        self.txtConfirmarSenhaCliente.setObjectName(u"txtConfirmarSenhaCliente")
        self.txtConfirmarSenhaCliente.setMinimumSize(QSize(0, 35))
        self.txtConfirmarSenhaCliente.setMaximumSize(QSize(16777215, 35))
        self.txtConfirmarSenhaCliente.setFont(font2)
        self.txtConfirmarSenhaCliente.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtConfirmarSenhaCliente.setMaxLength(5)
        self.txtConfirmarSenhaCliente.setEchoMode(QLineEdit.Password)
        self.txtConfirmarSenhaCliente.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.txtConfirmarSenhaCliente)

        self.splitter.addWidget(self.frame_11)

        self.verticalLayout_9.addWidget(self.splitter)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnConcluirCliente = QPushButton(self.frame_8)
        self.btnConcluirCliente.setObjectName(u"btnConcluirCliente")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnConcluirCliente.sizePolicy().hasHeightForWidth())
        self.btnConcluirCliente.setSizePolicy(sizePolicy5)
        self.btnConcluirCliente.setMinimumSize(QSize(0, 35))
        self.btnConcluirCliente.setMaximumSize(QSize(16777215, 35))
        self.btnConcluirCliente.setFont(font2)
        self.btnConcluirCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConcluirCliente.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btnConcluirCliente)

        self.btnCancelarCliente = QPushButton(self.frame_8)
        self.btnCancelarCliente.setObjectName(u"btnCancelarCliente")
        sizePolicy5.setHeightForWidth(self.btnCancelarCliente.sizePolicy().hasHeightForWidth())
        self.btnCancelarCliente.setSizePolicy(sizePolicy5)
        self.btnCancelarCliente.setMinimumSize(QSize(0, 35))
        self.btnCancelarCliente.setMaximumSize(QSize(16777215, 35))
        self.btnCancelarCliente.setFont(font2)
        self.btnCancelarCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelarCliente.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btnCancelarCliente)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.horizontalLayout_11.addWidget(self.frame_7)

        self.Paginas.addWidget(self.pg_cliente)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_cadastro)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pg_cadastro)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setStyleSheet(u"margin: 0px;\n"
"padding: 10px;\n"
"border: transparent;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 21, 21);\n"
"border: 1px solid rgb(199, 199, 199);\n"
"border-radius:10px;\n"
"font: \"Leelawadee\";")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font8)
        self.label.setStyleSheet(u"margin: 0px;\n"
"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;\n"
"border-radius: 0px;\n"
"border-bottom: 1px solid \"grey\";\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_4.addWidget(self.label_2)

        self.txtNome = QLineEdit(self.frame)
        self.txtNome.setObjectName(u"txtNome")
        self.txtNome.setMinimumSize(QSize(0, 35))
        self.txtNome.setMaximumSize(QSize(16777215, 35))
        self.txtNome.setFont(font2)
        self.txtNome.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtNome.setMaxLength(50)
        self.txtNome.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtNome)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_4.addWidget(self.label_3)

        self.txtEmail = QLineEdit(self.frame)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setMinimumSize(QSize(0, 35))
        self.txtEmail.setMaximumSize(QSize(16777215, 35))
        self.txtEmail.setFont(font2)
        self.txtEmail.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtEmail.setMaxLength(50)
        self.txtEmail.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtEmail)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.txtTelefone = QLineEdit(self.frame)
        self.txtTelefone.setObjectName(u"txtTelefone")
        self.txtTelefone.setMinimumSize(QSize(0, 35))
        self.txtTelefone.setMaximumSize(QSize(16777215, 35))
        self.txtTelefone.setFont(font2)
        self.txtTelefone.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtTelefone.setMaxLength(9)
        self.txtTelefone.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtTelefone)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.splitter_6 = QSplitter(self.frame_3)
        self.splitter_6.setObjectName(u"splitter_6")
        sizePolicy1.setHeightForWidth(self.splitter_6.sizePolicy().hasHeightForWidth())
        self.splitter_6.setSizePolicy(sizePolicy1)
        self.splitter_6.setOrientation(Qt.Vertical)
        self.label_5 = QLabel(self.splitter_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.splitter_6.addWidget(self.label_5)
        self.txtRua = QLineEdit(self.splitter_6)
        self.txtRua.setObjectName(u"txtRua")
        self.txtRua.setMinimumSize(QSize(0, 35))
        self.txtRua.setMaximumSize(QSize(16777215, 35))
        self.txtRua.setFont(font2)
        self.txtRua.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtRua.setMaxLength(30)
        self.txtRua.setClearButtonEnabled(True)
        self.splitter_6.addWidget(self.txtRua)

        self.horizontalLayout_5.addWidget(self.splitter_6)

        self.splitter_5 = QSplitter(self.frame_3)
        self.splitter_5.setObjectName(u"splitter_5")
        sizePolicy1.setHeightForWidth(self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy1)
        self.splitter_5.setMinimumSize(QSize(0, 30))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_6 = QLabel(self.splitter_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.splitter_5.addWidget(self.label_6)
        self.txtMunicipio = QLineEdit(self.splitter_5)
        self.txtMunicipio.setObjectName(u"txtMunicipio")
        self.txtMunicipio.setMinimumSize(QSize(0, 35))
        self.txtMunicipio.setMaximumSize(QSize(16777215, 35))
        self.txtMunicipio.setFont(font2)
        self.txtMunicipio.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtMunicipio.setMaxLength(30)
        self.txtMunicipio.setClearButtonEnabled(True)
        self.splitter_5.addWidget(self.txtMunicipio)

        self.horizontalLayout_5.addWidget(self.splitter_5)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.splitter_8 = QSplitter(self.frame_6)
        self.splitter_8.setObjectName(u"splitter_8")
        sizePolicy1.setHeightForWidth(self.splitter_8.sizePolicy().hasHeightForWidth())
        self.splitter_8.setSizePolicy(sizePolicy1)
        self.splitter_8.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.splitter_8.setOrientation(Qt.Vertical)
        self.label_10 = QLabel(self.splitter_8)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.splitter_8.addWidget(self.label_10)
        self.txtDias = QLineEdit(self.splitter_8)
        self.txtDias.setObjectName(u"txtDias")
        self.txtDias.setMinimumSize(QSize(0, 35))
        self.txtDias.setMaximumSize(QSize(16777215, 35))
        self.txtDias.setFont(font2)
        self.txtDias.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtDias.setMaxLength(25)
        self.txtDias.setEchoMode(QLineEdit.Normal)
        self.txtDias.setClearButtonEnabled(True)
        self.splitter_8.addWidget(self.txtDias)

        self.horizontalLayout_9.addWidget(self.splitter_8)

        self.splitter_9 = QSplitter(self.frame_6)
        self.splitter_9.setObjectName(u"splitter_9")
        sizePolicy1.setHeightForWidth(self.splitter_9.sizePolicy().hasHeightForWidth())
        self.splitter_9.setSizePolicy(sizePolicy1)
        self.splitter_9.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.splitter_9.setOrientation(Qt.Vertical)
        self.label_11 = QLabel(self.splitter_9)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.splitter_9.addWidget(self.label_11)
        self.txtHora = QLineEdit(self.splitter_9)
        self.txtHora.setObjectName(u"txtHora")
        self.txtHora.setMinimumSize(QSize(0, 35))
        self.txtHora.setMaximumSize(QSize(16777215, 35))
        self.txtHora.setFont(font2)
        self.txtHora.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtHora.setMaxLength(10)
        self.txtHora.setEchoMode(QLineEdit.Normal)
        self.txtHora.setClearButtonEnabled(True)
        self.splitter_9.addWidget(self.txtHora)

        self.horizontalLayout_9.addWidget(self.splitter_9)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_2)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy1.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy1)
        self.splitter_3.setOrientation(Qt.Vertical)
        self.label_7 = QLabel(self.splitter_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.splitter_3.addWidget(self.label_7)
        self.txtSenha = QLineEdit(self.splitter_3)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setMinimumSize(QSize(0, 35))
        self.txtSenha.setMaximumSize(QSize(16777215, 35))
        self.txtSenha.setFont(font2)
        self.txtSenha.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtSenha.setMaxLength(5)
        self.txtSenha.setEchoMode(QLineEdit.Password)
        self.txtSenha.setClearButtonEnabled(True)
        self.splitter_3.addWidget(self.txtSenha)

        self.horizontalLayout_4.addWidget(self.splitter_3)

        self.splitter_4 = QSplitter(self.frame_2)
        self.splitter_4.setObjectName(u"splitter_4")
        sizePolicy1.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy1)
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_8 = QLabel(self.splitter_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.splitter_4.addWidget(self.label_8)
        self.txtConfirmarSenha = QLineEdit(self.splitter_4)
        self.txtConfirmarSenha.setObjectName(u"txtConfirmarSenha")
        self.txtConfirmarSenha.setMinimumSize(QSize(0, 35))
        self.txtConfirmarSenha.setMaximumSize(QSize(16777215, 35))
        self.txtConfirmarSenha.setFont(font2)
        self.txtConfirmarSenha.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtConfirmarSenha.setMaxLength(5)
        self.txtConfirmarSenha.setEchoMode(QLineEdit.Password)
        self.txtConfirmarSenha.setClearButtonEnabled(True)
        self.splitter_4.addWidget(self.txtConfirmarSenha)

        self.horizontalLayout_4.addWidget(self.splitter_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"color: rgb(0, 0, 0);\n"
"border: transparent;")

        self.verticalLayout_4.addWidget(self.label_9)

        self.txtTipoAtividade = QLineEdit(self.frame)
        self.txtTipoAtividade.setObjectName(u"txtTipoAtividade")
        self.txtTipoAtividade.setMinimumSize(QSize(0, 35))
        self.txtTipoAtividade.setMaximumSize(QSize(16777215, 35))
        self.txtTipoAtividade.setFont(font2)
        self.txtTipoAtividade.setStyleSheet(u"padding: 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius:5px;")
        self.txtTipoAtividade.setMaxLength(30)
        self.txtTipoAtividade.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtTipoAtividade)

        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border: transparent;")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.btnConcluir = QPushButton(self.splitter_2)
        self.btnConcluir.setObjectName(u"btnConcluir")
        self.btnConcluir.setMinimumSize(QSize(0, 35))
        self.btnConcluir.setMaximumSize(QSize(16777215, 35))
        self.btnConcluir.setFont(font2)
        self.btnConcluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConcluir.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")
        self.splitter_2.addWidget(self.btnConcluir)
        self.btnCancelar = QPushButton(self.splitter_2)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setMinimumSize(QSize(0, 35))
        self.btnCancelar.setMaximumSize(QSize(16777215, 35))
        self.btnCancelar.setFont(font2)
        self.btnCancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(24, 12, 59);\n"
"	border: transparent;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 76, 161);\n"
"}\n"
"")
        self.splitter_2.addWidget(self.btnCancelar)

        self.verticalLayout_4.addWidget(self.splitter_2)


        self.horizontalLayout_3.addWidget(self.frame)

        self.Paginas.addWidget(self.pg_cadastro)

        self.verticalLayout.addWidget(self.Paginas)

        JanelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaPrincipal)

        self.Paginas.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(JanelaPrincipal)
    # setupUi

    def retranslateUi(self, JanelaPrincipal):
        JanelaPrincipal.setWindowTitle(QCoreApplication.translate("JanelaPrincipal", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("JanelaPrincipal", u"ASK", None))
        self.Titulo_2.setText(QCoreApplication.translate("JanelaPrincipal", u"SERVI\u00c7OS", None))
        self.btnCasa.setText(QCoreApplication.translate("JanelaPrincipal", u"HOME", None))
        self.btnSobre.setText(QCoreApplication.translate("JanelaPrincipal", u"SOBRE", None))
        self.btnContato.setText(QCoreApplication.translate("JanelaPrincipal", u"CONTATO", None))
        self.btnPesquisar.setText(QCoreApplication.translate("JanelaPrincipal", u"Pesquisar", None))
        self.CampoPesquisa.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Pesquise por servi\u00e7os", None))
        self.btnCadastrar.setText(QCoreApplication.translate("JanelaPrincipal", u"Cadastre-se", None))
        ___qtablewidgetitem = self.tb_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("JanelaPrincipal", u"ID", None));
        ___qtablewidgetitem1 = self.tb_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("JanelaPrincipal", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("JanelaPrincipal", u"EMAIL", None));
        ___qtablewidgetitem3 = self.tb_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("JanelaPrincipal", u"TELEFONE", None));
        ___qtablewidgetitem4 = self.tb_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("JanelaPrincipal", u"RUA", None));
        ___qtablewidgetitem5 = self.tb_usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("JanelaPrincipal", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem6 = self.tb_usuarios.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("JanelaPrincipal", u"HOR\u00c1RIO DISPON\u00cdVEL", None));
        ___qtablewidgetitem7 = self.tb_usuarios.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("JanelaPrincipal", u"DIAS DISPON\u00cdVEIS", None));
        ___qtablewidgetitem8 = self.tb_usuarios.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("JanelaPrincipal", u"SENHA", None));
        ___qtablewidgetitem9 = self.tb_usuarios.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("JanelaPrincipal", u"TIPO DE SERVI\u00c7O", None));
        self.ConteudoSobre.setHtml(QCoreApplication.translate("JanelaPrincipal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Leelawadee UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Nirmala UI'; font-size:14pt; font-weight:600;\">SOBRE</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Nirmala UI'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">O que \u00e9 o AskServi\u00e7os?</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">Uma plataforma que permite a promo\u00e7\u00e3o de servi\u00e7os de trabalhadores aut\u00f4nomos de eletr\u00f4nica.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Caso voc\u00ea n\u00e3o saiba:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">Trabalhadores aut\u00f4nomos s\u00e3o aqueles que trabalham por sua pro"
                        "pria conta e risco, sem v\u00ednculo empregat\u00edcio.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Quais os nossos objetivos?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">\u2022 Criar um aplicativo que possibilite o relacionamento entre os servi\u00e7os locais com o "
                        "cliente.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Nirmala UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">\u2022 Possibilitar a divulga\u00e7\u00e3o do trabalho para os prestadores de servi\u00e7os.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Nirmala UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">\u2022 Facilitar o encontro dos clientes com os prestadores de servi\u00e7os, utilizando meios de localiza\u00e7\u00e3o"
                        ".</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Nirmala UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">\u2022 Estabelecer uma rede de servi\u00e7os na localidade.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:11pt;\"><br /></p></body></html>", None))
        self.ConteudoContato.setHtml(QCoreApplication.translate("JanelaPrincipal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Liberation Sans'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Nirmala UI'; font-size:14pt; font-weight:600;\">CONTATO</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">Entre em contato conosco, caso haja algum problema na execu\u00e7\u00e3"
                        "o das funcionalidades do programa, ou tenha alguma indica\u00e7\u00e3o/recomenda\u00e7\u00e3o de melhora para o nosso programa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Instagram</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt;\">@victoroliver_rick</span></p>\n", None))
        self.label_18.setText(QCoreApplication.translate("JanelaPrincipal", u"O QUE DESEJA FAZER?", None))
        self.btnAnunciar.setText(QCoreApplication.translate("JanelaPrincipal", u"AN\u00daNCIAR SERVI\u00c7OS", None))
        self.btnSolicitar.setText(QCoreApplication.translate("JanelaPrincipal", u"SOLICITAR SERVI\u00c7OS", None))
        self.btnVoltarInicio.setText(QCoreApplication.translate("JanelaPrincipal", u"VOLTAR AO IN\u00cdCIO", None))
        self.label_17.setText(QCoreApplication.translate("JanelaPrincipal", u"CAMPO DE CADASTRO", None))
        self.label_12.setText(QCoreApplication.translate("JanelaPrincipal", u"Nome completo:", None))
        self.txtNomeCliente.setInputMask("")
        self.txtNomeCliente.setText("")
        self.txtNomeCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite seu nome", None))
        self.label_13.setText(QCoreApplication.translate("JanelaPrincipal", u"Email:", None))
        self.txtEmailCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Conta@email.com", None))
        self.label_14.setText(QCoreApplication.translate("JanelaPrincipal", u"N\u00ba de telefone:", None))
        self.txtTelefoneCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"(xx) x xxxx-xxxx", None))
        self.label_19.setText(QCoreApplication.translate("JanelaPrincipal", u"Senha:", None))
        self.txtSenhaCliente.setText("")
        self.txtSenhaCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"**********", None))
        self.label_20.setText(QCoreApplication.translate("JanelaPrincipal", u"Confirmar Senha:", None))
        self.txtConfirmarSenhaCliente.setText("")
        self.txtConfirmarSenhaCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"**********", None))
        self.btnConcluirCliente.setText(QCoreApplication.translate("JanelaPrincipal", u"CONCLUIR", None))
        self.btnCancelarCliente.setText(QCoreApplication.translate("JanelaPrincipal", u"CANCELAR", None))
        self.label.setText(QCoreApplication.translate("JanelaPrincipal", u"CAMPO DE CADASTRO", None))
        self.label_2.setText(QCoreApplication.translate("JanelaPrincipal", u"Nome completo:", None))
        self.txtNome.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite seu Nome Completo", None))
        self.label_3.setText(QCoreApplication.translate("JanelaPrincipal", u"Email:", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite sua Conta de Email", None))
        self.label_4.setText(QCoreApplication.translate("JanelaPrincipal", u"N\u00ba de telefone:", None))
        self.txtTelefone.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"(xx) x xxxx-xxxx", None))
        self.label_5.setText(QCoreApplication.translate("JanelaPrincipal", u"Rua:", None))
        self.txtRua.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: 15 de Novembro", None))
        self.label_6.setText(QCoreApplication.translate("JanelaPrincipal", u"Munic\u00edpio:", None))
        self.txtMunicipio.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Jaboat\u00e3o do Guararapes", None))
        self.label_10.setText(QCoreApplication.translate("JanelaPrincipal", u"Dias dispon\u00edveis:", None))
        self.txtDias.setText("")
        self.txtDias.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Segunda-Sexta", None))
        self.label_11.setText(QCoreApplication.translate("JanelaPrincipal", u"Hor\u00e1rio dispon\u00edvel:", None))
        self.txtHora.setText("")
        self.txtHora.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: 07AM-22PM", None))
        self.label_7.setText(QCoreApplication.translate("JanelaPrincipal", u"Senha:", None))
        self.txtSenha.setText("")
        self.txtSenha.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"**********", None))
        self.label_8.setText(QCoreApplication.translate("JanelaPrincipal", u"Confirmar senha:", None))
        self.txtConfirmarSenha.setText("")
        self.txtConfirmarSenha.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"**********", None))
        self.label_9.setText(QCoreApplication.translate("JanelaPrincipal", u"Tipo de servi\u00e7o:", None))
        self.txtTipoAtividade.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Manuten\u00e7\u00e3o de computadores", None))
        self.btnConcluir.setText(QCoreApplication.translate("JanelaPrincipal", u"CONCLUIR", None))
        self.btnCancelar.setText(QCoreApplication.translate("JanelaPrincipal", u"CANCELAR", None))
    # retranslateUi

