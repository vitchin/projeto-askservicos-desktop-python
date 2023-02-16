# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignAsk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        if not JanelaPrincipal.objectName():
            JanelaPrincipal.setObjectName(u"JanelaPrincipal")
        JanelaPrincipal.resize(1000, 689)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JanelaPrincipal.sizePolicy().hasHeightForWidth())
        JanelaPrincipal.setSizePolicy(sizePolicy)
        JanelaPrincipal.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.569, y1:1, x2:0.563, y2:0, stop:0 rgba(107, 74, 223, 255), stop:0.994318 rgba(23, 0, 167, 255));")
        self.centralwidget = QWidget(JanelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameAcimaDeTodos = QFrame(self.centralwidget)
        self.FrameAcimaDeTodos.setObjectName(u"FrameAcimaDeTodos")
        self.FrameAcimaDeTodos.setMinimumSize(QSize(0, 60))
        self.FrameAcimaDeTodos.setMaximumSize(QSize(16777215, 60))
        self.FrameAcimaDeTodos.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(42, 55, 223, 255), stop:0.994318 rgba(40, 0, 219, 171));")
        self.FrameAcimaDeTodos.setFrameShape(QFrame.StyledPanel)
        self.FrameAcimaDeTodos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FrameAcimaDeTodos)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.Titulo = QLabel(self.FrameAcimaDeTodos)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setMinimumSize(QSize(100, 0))
        self.Titulo.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(130, 14, 255, 0), stop:0.994318 rgba(122, 0, 255, 0));\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Titulo.setTextFormat(Qt.PlainText)
        self.Titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Titulo)

        self.btnCasa = QPushButton(self.FrameAcimaDeTodos)
        self.btnCasa.setObjectName(u"btnCasa")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnCasa.sizePolicy().hasHeightForWidth())
        self.btnCasa.setSizePolicy(sizePolicy1)
        self.btnCasa.setMinimumSize(QSize(0, 50))
        self.btnCasa.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.btnCasa.setFont(font1)
        self.btnCasa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCasa.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnCasa)

        self.btnSobre = QPushButton(self.FrameAcimaDeTodos)
        self.btnSobre.setObjectName(u"btnSobre")
        sizePolicy1.setHeightForWidth(self.btnSobre.sizePolicy().hasHeightForWidth())
        self.btnSobre.setSizePolicy(sizePolicy1)
        self.btnSobre.setMinimumSize(QSize(0, 50))
        self.btnSobre.setMaximumSize(QSize(16777215, 50))
        self.btnSobre.setFont(font1)
        self.btnSobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSobre.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnSobre)

        self.btnContato = QPushButton(self.FrameAcimaDeTodos)
        self.btnContato.setObjectName(u"btnContato")
        sizePolicy1.setHeightForWidth(self.btnContato.sizePolicy().hasHeightForWidth())
        self.btnContato.setSizePolicy(sizePolicy1)
        self.btnContato.setMinimumSize(QSize(0, 50))
        self.btnContato.setMaximumSize(QSize(16777215, 50))
        self.btnContato.setFont(font1)
        self.btnContato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnContato.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.FrameSearch = QFrame(self.pg_inicial)
        self.FrameSearch.setObjectName(u"FrameSearch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FrameSearch.sizePolicy().hasHeightForWidth())
        self.FrameSearch.setSizePolicy(sizePolicy2)
        self.FrameSearch.setMinimumSize(QSize(0, 45))
        self.FrameSearch.setMaximumSize(QSize(16777215, 45))
        self.FrameSearch.setLayoutDirection(Qt.LeftToRight)
        self.FrameSearch.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.569, y1:1, x2:0.563, y2:0, stop:0 rgba(107, 74, 223, 68), stop:0.994318 rgba(23, 0, 167, 191));\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.FrameSearch.setFrameShape(QFrame.StyledPanel)
        self.FrameSearch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameSearch)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.btnPesquisar = QPushButton(self.FrameSearch)
        self.btnPesquisar.setObjectName(u"btnPesquisar")
        self.btnPesquisar.setMinimumSize(QSize(120, 35))
        self.btnPesquisar.setMaximumSize(QSize(120, 35))
        font2 = QFont()
        font2.setFamily(u"Agency FB")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnPesquisar.setFont(font2)
        self.btnPesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPesquisar.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnPesquisar)

        self.splitter_7 = QSplitter(self.FrameSearch)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.CampoPesquisa = QLineEdit(self.splitter_7)
        self.CampoPesquisa.setObjectName(u"CampoPesquisa")
        self.CampoPesquisa.setMinimumSize(QSize(0, 35))
        self.CampoPesquisa.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setFamily(u"Nirmala UI")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setWeight(50)
        self.CampoPesquisa.setFont(font3)
        self.CampoPesquisa.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:2px;")
        self.CampoPesquisa.setMaxLength(50)
        self.splitter_7.addWidget(self.CampoPesquisa)

        self.horizontalLayout_2.addWidget(self.splitter_7)

        self.btnCadastrar = QPushButton(self.FrameSearch)
        self.btnCadastrar.setObjectName(u"btnCadastrar")
        self.btnCadastrar.setMinimumSize(QSize(120, 35))
        self.btnCadastrar.setMaximumSize(QSize(120, 35))
        self.btnCadastrar.setFont(font2)
        self.btnCadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCadastrar.setLayoutDirection(Qt.LeftToRight)
        self.btnCadastrar.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnCadastrar)


        self.verticalLayout_2.addWidget(self.FrameSearch)

        self.tb_usuarios = QTableWidget(self.pg_inicial)
        if (self.tb_usuarios.columnCount() < 10):
            self.tb_usuarios.setColumnCount(10)
        font4 = QFont()
        font4.setFamily(u"Nirmala UI")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        font4.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font4);
        self.tb_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font5 = QFont()
        font5.setFamily(u"Nirmala UI")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font5);
        self.tb_usuarios.setColumnHidden(0, True)
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
        self.tb_usuarios.setColumnHidden(8, True)
        self.tb_usuarios.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tb_usuarios.setObjectName(u"tb_usuarios")
        sizePolicy2.setHeightForWidth(self.tb_usuarios.sizePolicy().hasHeightForWidth())
        self.tb_usuarios.setSizePolicy(sizePolicy2)
        self.tb_usuarios.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tb_usuarios.setStyleSheet(u"background-color: rgb(228, 229, 235);")
        self.tb_usuarios.horizontalHeader().setMinimumSectionSize(100)
        self.tb_usuarios.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.tb_usuarios)

        self.Paginas.addWidget(self.pg_inicial)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_sobre)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 5, 0, 0)
        self.frame_5 = QFrame(self.pg_sobre)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.585955, y1:0, x2:0.591, y2:1, stop:0 rgba(67, 88, 246, 239), stop:1 rgba(26, 0, 187, 255));")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.ConteudoSobre = QTextBrowser(self.frame_5)
        self.ConteudoSobre.setObjectName(u"ConteudoSobre")
        font6 = QFont()
        font6.setFamily(u"Nirmala UI")
        font6.setPointSize(8)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.ConteudoSobre.setFont(font6)
        self.ConteudoSobre.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.ConteudoSobre.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px;")

        self.verticalLayout_3.addWidget(self.ConteudoSobre)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.Paginas.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_contato)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 0)
        self.frame_4 = QFrame(self.pg_contato)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.585955, y1:0, x2:0.591, y2:1, stop:0 rgba(67, 88, 246, 239), stop:1 rgba(26, 0, 187, 255));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.ConteudoContato = QTextBrowser(self.frame_4)
        self.ConteudoContato.setObjectName(u"ConteudoContato")
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        self.ConteudoContato.setFont(font7)
        self.ConteudoContato.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.ConteudoContato.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:\"Nirmala UI\";\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));\n"
"border-radius:2px;")

        self.verticalLayout_6.addWidget(self.ConteudoContato)


        self.horizontalLayout_7.addWidget(self.frame_4)

        self.Paginas.addWidget(self.pg_contato)
        self.pg_escolha = QWidget()
        self.pg_escolha.setObjectName(u"pg_escolha")
        self.horizontalLayout_12 = QHBoxLayout(self.pg_escolha)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_9 = QFrame(self.pg_escolha)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setMinimumSize(QSize(350, 250))
        self.frame_9.setMaximumSize(QSize(350, 250))
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(96, 64, 239, 255), stop:1 rgba(36, 0, 198, 144));\n"
"border-radius:20px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 25))
        self.label_18.setMaximumSize(QSize(16777215, 25))
        font8 = QFont()
        font8.setFamily(u"Agency FB")
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_18)

        self.btnAnunciar = QPushButton(self.frame_9)
        self.btnAnunciar.setObjectName(u"btnAnunciar")
        self.btnAnunciar.setMinimumSize(QSize(0, 45))
        self.btnAnunciar.setMaximumSize(QSize(16777215, 45))
        self.btnAnunciar.setFont(font2)
        self.btnAnunciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnunciar.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btnAnunciar)

        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 25))
        self.label_21.setMaximumSize(QSize(16777215, 25))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_21)

        self.btnSolicitar = QPushButton(self.frame_9)
        self.btnSolicitar.setObjectName(u"btnSolicitar")
        self.btnSolicitar.setMinimumSize(QSize(0, 45))
        self.btnSolicitar.setMaximumSize(QSize(16777215, 45))
        self.btnSolicitar.setFont(font2)
        self.btnSolicitar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSolicitar.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btnSolicitar)

        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 25))
        self.label_22.setMaximumSize(QSize(16777215, 25))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_22)

        self.btnVoltarInicio = QPushButton(self.frame_9)
        self.btnVoltarInicio.setObjectName(u"btnVoltarInicio")
        self.btnVoltarInicio.setMinimumSize(QSize(0, 45))
        self.btnVoltarInicio.setMaximumSize(QSize(16777215, 45))
        self.btnVoltarInicio.setFont(font2)
        self.btnVoltarInicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVoltarInicio.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btnVoltarInicio)


        self.horizontalLayout_12.addWidget(self.frame_9)

        self.Paginas.addWidget(self.pg_escolha)
        self.pg_cliente = QWidget()
        self.pg_cliente.setObjectName(u"pg_cliente")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_cliente)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.pg_cliente)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMinimumSize(QSize(350, 415))
        self.frame_7.setMaximumSize(QSize(350, 415))
        self.frame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(96, 64, 239, 255), stop:1 rgba(36, 0, 198, 144));\n"
"border-radius:20px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 25))
        self.label_17.setMaximumSize(QSize(16777215, 25))
        font9 = QFont()
        font9.setFamily(u"Agency FB")
        font9.setPointSize(18)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_17)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 25))
        self.label_12.setMaximumSize(QSize(16777215, 25))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_5.addWidget(self.label_12)

        self.txtNomeCliente = QLineEdit(self.frame_7)
        self.txtNomeCliente.setObjectName(u"txtNomeCliente")
        self.txtNomeCliente.setMinimumSize(QSize(0, 30))
        self.txtNomeCliente.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setFamily(u"Nirmala UI")
        font10.setPointSize(12)
        self.txtNomeCliente.setFont(font10)
        self.txtNomeCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:2px;")
        self.txtNomeCliente.setMaxLength(32767)
        self.txtNomeCliente.setFrame(True)
        self.txtNomeCliente.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.txtNomeCliente)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 25))
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_5.addWidget(self.label_13)

        self.txtEmailCliente = QLineEdit(self.frame_7)
        self.txtEmailCliente.setObjectName(u"txtEmailCliente")
        self.txtEmailCliente.setMinimumSize(QSize(0, 30))
        self.txtEmailCliente.setMaximumSize(QSize(16777215, 30))
        self.txtEmailCliente.setFont(font10)
        self.txtEmailCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtEmailCliente.setMaxLength(50)
        self.txtEmailCliente.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.txtEmailCliente)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 25))
        self.label_14.setMaximumSize(QSize(16777215, 25))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_5.addWidget(self.label_14)

        self.txtTelefoneCliente = QLineEdit(self.frame_7)
        self.txtTelefoneCliente.setObjectName(u"txtTelefoneCliente")
        self.txtTelefoneCliente.setMinimumSize(QSize(0, 30))
        self.txtTelefoneCliente.setMaximumSize(QSize(16777215, 30))
        self.txtTelefoneCliente.setFont(font10)
        self.txtTelefoneCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtTelefoneCliente.setMaxLength(9)
        self.txtTelefoneCliente.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.txtTelefoneCliente)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 70))
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.splitter_14 = QSplitter(self.frame_10)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setOrientation(Qt.Vertical)
        self.label_19 = QLabel(self.splitter_14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 25))
        self.label_19.setMaximumSize(QSize(16777215, 25))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_14.addWidget(self.label_19)
        self.txtSenhaCliente = QLineEdit(self.splitter_14)
        self.txtSenhaCliente.setObjectName(u"txtSenhaCliente")
        self.txtSenhaCliente.setMinimumSize(QSize(0, 30))
        self.txtSenhaCliente.setMaximumSize(QSize(16777215, 30))
        self.txtSenhaCliente.setFont(font10)
        self.txtSenhaCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtSenhaCliente.setMaxLength(5)
        self.txtSenhaCliente.setEchoMode(QLineEdit.Password)
        self.txtSenhaCliente.setClearButtonEnabled(True)
        self.splitter_14.addWidget(self.txtSenhaCliente)

        self.horizontalLayout_11.addWidget(self.splitter_14)

        self.splitter_15 = QSplitter(self.frame_10)
        self.splitter_15.setObjectName(u"splitter_15")
        self.splitter_15.setOrientation(Qt.Vertical)
        self.label_20 = QLabel(self.splitter_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 25))
        self.label_20.setMaximumSize(QSize(16777215, 25))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_15.addWidget(self.label_20)
        self.txtConfirmarSenhaCliente = QLineEdit(self.splitter_15)
        self.txtConfirmarSenhaCliente.setObjectName(u"txtConfirmarSenhaCliente")
        self.txtConfirmarSenhaCliente.setMinimumSize(QSize(0, 30))
        self.txtConfirmarSenhaCliente.setMaximumSize(QSize(16777215, 30))
        self.txtConfirmarSenhaCliente.setFont(font10)
        self.txtConfirmarSenhaCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtConfirmarSenhaCliente.setMaxLength(5)
        self.txtConfirmarSenhaCliente.setEchoMode(QLineEdit.Password)
        self.txtConfirmarSenhaCliente.setClearButtonEnabled(True)
        self.splitter_15.addWidget(self.txtConfirmarSenhaCliente)

        self.horizontalLayout_11.addWidget(self.splitter_15)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.textBrowser_7 = QTextBrowser(self.frame_7)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setMinimumSize(QSize(0, 40))
        self.textBrowser_7.setMaximumSize(QSize(16777215, 43))
        self.textBrowser_7.setStyleSheet(u"background-color: rgb(121, 111, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")

        self.verticalLayout_5.addWidget(self.textBrowser_7)

        self.splitter_16 = QSplitter(self.frame_7)
        self.splitter_16.setObjectName(u"splitter_16")
        self.splitter_16.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_16.setOrientation(Qt.Horizontal)
        self.btnCancelarCliente = QPushButton(self.splitter_16)
        self.btnCancelarCliente.setObjectName(u"btnCancelarCliente")
        self.btnCancelarCliente.setMinimumSize(QSize(0, 45))
        self.btnCancelarCliente.setMaximumSize(QSize(16777215, 45))
        self.btnCancelarCliente.setFont(font2)
        self.btnCancelarCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelarCliente.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")
        self.splitter_16.addWidget(self.btnCancelarCliente)
        self.btnConcluirCliente = QPushButton(self.splitter_16)
        self.btnConcluirCliente.setObjectName(u"btnConcluirCliente")
        self.btnConcluirCliente.setMinimumSize(QSize(0, 45))
        self.btnConcluirCliente.setMaximumSize(QSize(16777215, 45))
        self.btnConcluirCliente.setFont(font2)
        self.btnConcluirCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConcluirCliente.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")
        self.splitter_16.addWidget(self.btnConcluirCliente)

        self.verticalLayout_5.addWidget(self.splitter_16)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.Paginas.addWidget(self.pg_cliente)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_cadastro)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.pg_cadastro)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(360, 600))
        self.frame.setMaximumSize(QSize(390, 600))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(96, 64, 239, 255), stop:1 rgba(36, 0, 198, 144));\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setFont(font9)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_4.addWidget(self.label_2)

        self.txtNome = QLineEdit(self.frame)
        self.txtNome.setObjectName(u"txtNome")
        self.txtNome.setMinimumSize(QSize(0, 30))
        self.txtNome.setMaximumSize(QSize(16777215, 30))
        font11 = QFont()
        font11.setFamily(u"Nirmala UI")
        font11.setPointSize(13)
        self.txtNome.setFont(font11)
        self.txtNome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:2px;")
        self.txtNome.setMaxLength(50)
        self.txtNome.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtNome)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_4.addWidget(self.label_3)

        self.txtEmail = QLineEdit(self.frame)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setMinimumSize(QSize(0, 30))
        self.txtEmail.setMaximumSize(QSize(16777215, 30))
        self.txtEmail.setFont(font11)
        self.txtEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtEmail.setMaxLength(50)
        self.txtEmail.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtEmail)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setMaximumSize(QSize(16777215, 25))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_4.addWidget(self.label_4)

        self.txtTelefone = QLineEdit(self.frame)
        self.txtTelefone.setObjectName(u"txtTelefone")
        self.txtTelefone.setMinimumSize(QSize(0, 30))
        self.txtTelefone.setMaximumSize(QSize(16777215, 30))
        self.txtTelefone.setFont(font11)
        self.txtTelefone.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtTelefone.setMaxLength(9)
        self.txtTelefone.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtTelefone)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.splitter_6 = QSplitter(self.frame_3)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.label_5 = QLabel(self.splitter_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_6.addWidget(self.label_5)
        self.txtRua = QLineEdit(self.splitter_6)
        self.txtRua.setObjectName(u"txtRua")
        self.txtRua.setMinimumSize(QSize(0, 30))
        self.txtRua.setMaximumSize(QSize(16777215, 30))
        self.txtRua.setFont(font11)
        self.txtRua.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtRua.setMaxLength(30)
        self.txtRua.setClearButtonEnabled(True)
        self.splitter_6.addWidget(self.txtRua)

        self.horizontalLayout_5.addWidget(self.splitter_6)

        self.splitter_5 = QSplitter(self.frame_3)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setMinimumSize(QSize(0, 30))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_6 = QLabel(self.splitter_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 25))
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_5.addWidget(self.label_6)
        self.txtMunicipio = QLineEdit(self.splitter_5)
        self.txtMunicipio.setObjectName(u"txtMunicipio")
        self.txtMunicipio.setMinimumSize(QSize(0, 30))
        self.txtMunicipio.setMaximumSize(QSize(16777215, 30))
        self.txtMunicipio.setFont(font11)
        self.txtMunicipio.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtMunicipio.setMaxLength(30)
        self.txtMunicipio.setClearButtonEnabled(True)
        self.splitter_5.addWidget(self.txtMunicipio)

        self.horizontalLayout_5.addWidget(self.splitter_5)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 70))
        self.frame_6.setMaximumSize(QSize(16777215, 80))
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.splitter_8 = QSplitter(self.frame_6)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Vertical)
        self.label_10 = QLabel(self.splitter_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 25))
        self.label_10.setMaximumSize(QSize(16777215, 25))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_8.addWidget(self.label_10)
        self.txtDias = QLineEdit(self.splitter_8)
        self.txtDias.setObjectName(u"txtDias")
        self.txtDias.setMinimumSize(QSize(0, 30))
        self.txtDias.setMaximumSize(QSize(16777215, 30))
        self.txtDias.setFont(font11)
        self.txtDias.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtDias.setMaxLength(25)
        self.txtDias.setEchoMode(QLineEdit.Normal)
        self.txtDias.setClearButtonEnabled(True)
        self.splitter_8.addWidget(self.txtDias)

        self.horizontalLayout_9.addWidget(self.splitter_8)

        self.splitter_9 = QSplitter(self.frame_6)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Vertical)
        self.label_11 = QLabel(self.splitter_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 25))
        self.label_11.setMaximumSize(QSize(16777215, 25))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_9.addWidget(self.label_11)
        self.txtHora = QLineEdit(self.splitter_9)
        self.txtHora.setObjectName(u"txtHora")
        self.txtHora.setMinimumSize(QSize(0, 30))
        self.txtHora.setMaximumSize(QSize(16777215, 30))
        self.txtHora.setFont(font11)
        self.txtHora.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtHora.setMaxLength(10)
        self.txtHora.setEchoMode(QLineEdit.Normal)
        self.txtHora.setClearButtonEnabled(True)
        self.splitter_9.addWidget(self.txtHora)

        self.horizontalLayout_9.addWidget(self.splitter_9)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.label_7 = QLabel(self.splitter_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 25))
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_3.addWidget(self.label_7)
        self.txtSenha = QLineEdit(self.splitter_3)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setMinimumSize(QSize(0, 30))
        self.txtSenha.setMaximumSize(QSize(16777215, 30))
        self.txtSenha.setFont(font11)
        self.txtSenha.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtSenha.setMaxLength(5)
        self.txtSenha.setEchoMode(QLineEdit.Password)
        self.txtSenha.setClearButtonEnabled(True)
        self.splitter_3.addWidget(self.txtSenha)

        self.horizontalLayout_4.addWidget(self.splitter_3)

        self.splitter_4 = QSplitter(self.frame_2)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_8 = QLabel(self.splitter_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 25))
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_4.addWidget(self.label_8)
        self.txtConfirmarSenha = QLineEdit(self.splitter_4)
        self.txtConfirmarSenha.setObjectName(u"txtConfirmarSenha")
        self.txtConfirmarSenha.setMinimumSize(QSize(0, 30))
        self.txtConfirmarSenha.setMaximumSize(QSize(16777215, 30))
        self.txtConfirmarSenha.setFont(font11)
        self.txtConfirmarSenha.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtConfirmarSenha.setMaxLength(5)
        self.txtConfirmarSenha.setEchoMode(QLineEdit.Password)
        self.txtConfirmarSenha.setClearButtonEnabled(True)
        self.splitter_4.addWidget(self.txtConfirmarSenha)

        self.horizontalLayout_4.addWidget(self.splitter_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 25))
        self.label_9.setMaximumSize(QSize(16777215, 25))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")

        self.verticalLayout_4.addWidget(self.label_9)

        self.txtTipoAtividade = QLineEdit(self.frame)
        self.txtTipoAtividade.setObjectName(u"txtTipoAtividade")
        self.txtTipoAtividade.setMinimumSize(QSize(0, 30))
        self.txtTipoAtividade.setMaximumSize(QSize(16777215, 30))
        self.txtTipoAtividade.setFont(font11)
        self.txtTipoAtividade.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius:2px;")
        self.txtTipoAtividade.setMaxLength(30)
        self.txtTipoAtividade.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.txtTipoAtividade)

        self.textBrowser_6 = QTextBrowser(self.frame)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setMinimumSize(QSize(0, 40))
        self.textBrowser_6.setMaximumSize(QSize(16777215, 43))
        self.textBrowser_6.setStyleSheet(u"background-color: rgb(121, 111, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")

        self.verticalLayout_4.addWidget(self.textBrowser_6)

        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.574, y1:1, x2:0.557, y2:0, stop:0 rgba(26, 0, 189, 0), stop:1 rgba(53, 0, 151, 0));")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.btnCancelar = QPushButton(self.splitter_2)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setMinimumSize(QSize(0, 45))
        self.btnCancelar.setMaximumSize(QSize(16777215, 45))
        self.btnCancelar.setFont(font2)
        self.btnCancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")
        self.splitter_2.addWidget(self.btnCancelar)
        self.btnConcluir = QPushButton(self.splitter_2)
        self.btnConcluir.setObjectName(u"btnConcluir")
        self.btnConcluir.setMinimumSize(QSize(0, 45))
        self.btnConcluir.setMaximumSize(QSize(16777215, 45))
        self.btnConcluir.setFont(font2)
        self.btnConcluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConcluir.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.5, y2:0.994, stop:0 rgba(52, 109, 255, 255), stop:1 rgba(94, 62, 237, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
";}\n"
"QPushButton:hover{\n"
"background-color: rgb(89, 161, 255);\n"
"}\n"
"")
        self.splitter_2.addWidget(self.btnConcluir)

        self.verticalLayout_4.addWidget(self.splitter_2)


        self.horizontalLayout_3.addWidget(self.frame)

        self.Paginas.addWidget(self.pg_cadastro)

        self.verticalLayout.addWidget(self.Paginas)

        JanelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaPrincipal)

        self.Paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(JanelaPrincipal)
    # setupUi

    def retranslateUi(self, JanelaPrincipal):
        JanelaPrincipal.setWindowTitle(QCoreApplication.translate("JanelaPrincipal", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("JanelaPrincipal", u"ASK", None))
        self.btnCasa.setText(QCoreApplication.translate("JanelaPrincipal", u"HOME", None))
        self.btnSobre.setText(QCoreApplication.translate("JanelaPrincipal", u"SOBRE", None))
        self.btnContato.setText(QCoreApplication.translate("JanelaPrincipal", u"CONTATO", None))
        self.btnPesquisar.setText(QCoreApplication.translate("JanelaPrincipal", u"PESQUISAR", None))
        self.CampoPesquisa.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Barra de Pesquisa", None))
        self.btnCadastrar.setText(QCoreApplication.translate("JanelaPrincipal", u"CADASTRE-SE", None))
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
"</style></head><body style=\" font-family:'Nirmala UI'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">SOBRE</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\">O que \u00e9 o AskServi\u00e7os?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">Uma plataforma que permite a promo\u00e7\u00e3o de servi\u00e7os de trabalhadores aut\u00f4nomos de eletr\u00f4nica.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\">Caso voc\u00ea n\u00e3o saiba:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">Trabalhadores aut\u00f4nomos s\u00e3o aqueles que trabalham por sua propria conta e risco, sem v\u00ednculo empregat\u00edci"
                        "o.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\">Quais os nossos objetivos?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">\u2022 Criar um aplicativo que possibilite o relacionamento entre os servi\u00e7os locais com o cliente.</span></p>\n"
"<p style=\"-qt-paragraph-type"
                        ":empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">\u2022 Possibilitar a divulga\u00e7\u00e3o do trabalho para os prestadores de servi\u00e7os.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">\u2022 Facilitar o encontro dos clientes com os prestadores de servi\u00e7os, utilizando meios de localiza\u00e7\u00e3o.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">\u2022 Estabelecer uma rede de servi\u00e7os na localidade.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p></body></html>", None))
        self.ConteudoContato.setHtml(QCoreApplication.translate("JanelaPrincipal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">CONTATO</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Entre em contato conosco, caso haja algum problema na execu\u00e7\u00e3o das funcionalidades do programa, ou tenha alguma indica\u00e7\u00e3o/recomenda\u00e7"
                        "\u00e3o de melhora para o nosso programa.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Instagram</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">@victoroliver_rick</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">@mhelenaxz</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">@Vanessa.vitoria14</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("JanelaPrincipal", u"ATIVIDADES", None))
        self.btnAnunciar.setText(QCoreApplication.translate("JanelaPrincipal", u"AN\u00daNCIAR SERVI\u00c7OS", None))
        self.label_21.setText(QCoreApplication.translate("JanelaPrincipal", u"OU", None))
        self.btnSolicitar.setText(QCoreApplication.translate("JanelaPrincipal", u"SOLICITAR SERVI\u00c7OS", None))
        self.label_22.setText(QCoreApplication.translate("JanelaPrincipal", u"OU", None))
        self.btnVoltarInicio.setText(QCoreApplication.translate("JanelaPrincipal", u"VOLTAR AO IN\u00cdCIO", None))
        self.label_17.setText(QCoreApplication.translate("JanelaPrincipal", u"CAMPO DE CADASTRO", None))
        self.label_12.setText(QCoreApplication.translate("JanelaPrincipal", u"NOME:", None))
        self.txtNomeCliente.setInputMask("")
        self.txtNomeCliente.setText("")
        self.txtNomeCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite seu Nome Completo", None))
        self.label_13.setText(QCoreApplication.translate("JanelaPrincipal", u"EMAIL:", None))
        self.txtEmailCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite sua Conta de Email", None))
        self.label_14.setText(QCoreApplication.translate("JanelaPrincipal", u"N\u00daMERO DE TELEFONE:", None))
        self.txtTelefoneCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"(DDD) 9-2222-3333", None))
        self.label_19.setText(QCoreApplication.translate("JanelaPrincipal", u"SENHA:", None))
        self.txtSenhaCliente.setText("")
        self.txtSenhaCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"*****", None))
        self.label_20.setText(QCoreApplication.translate("JanelaPrincipal", u"CONFIRMAR SENHA:", None))
        self.txtConfirmarSenhaCliente.setText("")
        self.txtConfirmarSenhaCliente.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"*****", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("JanelaPrincipal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Apenas \u00e9 poss\u00edvel avan\u00e7ar caso os espa\u00e7os estejam preenchidos.</span></p></body></html>", None))
        self.btnCancelarCliente.setText(QCoreApplication.translate("JanelaPrincipal", u"CANCELAR", None))
        self.btnConcluirCliente.setText(QCoreApplication.translate("JanelaPrincipal", u"CONCLUIR", None))
        self.label.setText(QCoreApplication.translate("JanelaPrincipal", u"CAMPO DE CADASTRO", None))
        self.label_2.setText(QCoreApplication.translate("JanelaPrincipal", u"NOME:", None))
        self.txtNome.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite seu Nome Completo", None))
        self.label_3.setText(QCoreApplication.translate("JanelaPrincipal", u"EMAIL:", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Digite sua Conta de Email", None))
        self.label_4.setText(QCoreApplication.translate("JanelaPrincipal", u"N\u00daMERO DE TELEFONE:", None))
        self.txtTelefone.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"(DDD)9-3333-2222", None))
        self.label_5.setText(QCoreApplication.translate("JanelaPrincipal", u"RUA:", None))
        self.txtRua.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: 15 de Novembro", None))
        self.label_6.setText(QCoreApplication.translate("JanelaPrincipal", u"MUNIC\u00cdPIO:", None))
        self.txtMunicipio.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Jaboat\u00e3o do Guararapes", None))
        self.label_10.setText(QCoreApplication.translate("JanelaPrincipal", u"DIAS DISPON\u00cdVEIS:", None))
        self.txtDias.setText("")
        self.txtDias.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Segunda-Sexta", None))
        self.label_11.setText(QCoreApplication.translate("JanelaPrincipal", u"HOR\u00c1RIO DISPON\u00cdVEL:", None))
        self.txtHora.setText("")
        self.txtHora.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: 07AM-22PM", None))
        self.label_7.setText(QCoreApplication.translate("JanelaPrincipal", u"SENHA:", None))
        self.txtSenha.setText("")
        self.txtSenha.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"*****", None))
        self.label_8.setText(QCoreApplication.translate("JanelaPrincipal", u"CONFIRMAR SENHA:", None))
        self.txtConfirmarSenha.setText("")
        self.txtConfirmarSenha.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"*****", None))
        self.label_9.setText(QCoreApplication.translate("JanelaPrincipal", u"TIPO DE SERVI\u00c7O:", None))
        self.txtTipoAtividade.setPlaceholderText(QCoreApplication.translate("JanelaPrincipal", u"Ex: Manuten\u00e7\u00e3o de computadores", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("JanelaPrincipal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Apenas \u00e9 poss\u00edvel avan\u00e7ar caso os espa\u00e7os estejam preenchidos</span></p></body></html>", None))
        self.btnCancelar.setText(QCoreApplication.translate("JanelaPrincipal", u"CANCELAR", None))
        self.btnConcluir.setText(QCoreApplication.translate("JanelaPrincipal", u"CONCLUIR", None))
    # retranslateUi

