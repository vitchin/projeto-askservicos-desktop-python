from PyQt5.QtWidgets import (QTableWidgetItem, QMessageBox)
from PyQt5.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QTableWidgetItem, QMessageBox)
from PySide2.QtWidgets import *
from ui_DesignAsk import Ui_JanelaPrincipal
from Database import DataBase
from DatabaseCliente import DataBaseCliente
import sys

class JanelaPrincipal(QMainWindow, Ui_JanelaPrincipal):
    def __init__(self):
        super(JanelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Pesquisa de Serviços")
        appIcon = QIcon('Imagens/Logo.png')
        self.setWindowIcon(appIcon)

        # Função dos botões de levar para outras páginas
        # Página inicial
        self.btnCasa.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_inicial))
        self.btnSobre.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_sobre))
        self.btnContato.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_contato))

        # pg_escolha
        self.btnAnunciar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_cadastro))
        self.btnSolicitar.clicked.connect(lambda : self.Paginas.setCurrentWidget(self.pg_cliente))
        self.btnVoltarInicio.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_inicial))

        self.btnCancelarCliente.clicked.connect(lambda : self.Paginas.setCurrentWidget(self.pg_inicial))

        # pg_cadastro
        self.btnCadastrar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_escolha))
        self.btnCancelar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pg_inicial))
        self.btnConcluir.clicked.connect(self.cadastrar_usuario)
        self.btnPesquisar.clicked.connect(self.pesquisar_dados)
        self.btnConcluirCliente.clicked.connect(self.cadastrar_cliente)

        self.carregar_dados_usuario()

    # adiciona as informações do usuário no banco de dados usuarios.db
    def cadastrar_usuario(self):
        db = DataBase("usuarios.db")

        nome = self.txtNome.text()
        email = self.txtEmail.text()
        telefone = self.txtTelefone.text()
        rua = self.txtRua.text()
        municipio = self.txtMunicipio.text()
        hora = self.txtHora.text()
        dias = self.txtDias.text()
        senha = self.txtSenha.text()
        tipo = self.txtTipoAtividade.text()

        if self.txtSenha.text() != self.txtConfirmarSenha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Divergentes")
            msg.setText("As senhas não são iguais!")
            msg.exec_()

        if nome == "" or email == "" or telefone == "" or rua == "" or municipio == "" or hora == "" or dias == "" or senha == "" or tipo == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo vazio")
            msg.setText("Você esqueceu de preencher algumas informações!")
            msg.exec_()
        else:
            db.inserir_apaga_atualiza("INSERT INTO USUARIO(NOME, EMAIL, TELEFONE, RUA, MUNICIPIO, HORA, DIAS, SENHA, TIPO) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nome, email, telefone, rua, municipio, hora, dias, senha, tipo))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro realizado")
            msg.setText("Seu cadastro foi realizado com sucesso!")
            msg.exec_()
    # Coloca os dados na tabela
    def carregar_dados_usuario(self):

        db = DataBase("usuarios.db")
        lista = db.pegar_dados("SELECT * FROM USUARIO")

        self.tb_usuarios.setRowCount(0)
        self.tb_usuarios.setSortingEnabled(True)
        for linha, dados in enumerate(lista):
            self.tb_usuarios.insertRow(linha)
            self.tb_usuarios.resizeColumnToContents(linha)

            for coluna, dados in enumerate(dados):
                self.tb_usuarios.setItem(linha, coluna, QTableWidgetItem(str(dados)))
                self.tb_usuarios.resizeColumnToContents(linha)
    # Permite a pesquisa de dados atraves da barra de pesquisa
    def pesquisar_dados(self):

        db = DataBase("usuarios.db")
        valor_consulta = ""
        valor_consulta = self.CampoPesquisa.text()

        lista = db.pegar_dados(f"SELECT * FROM USUARIO WHERE NOME LIKE '%{valor_consulta}%' OR RUA LIKE '%{valor_consulta}%' OR MUNICIPIO LIKE '%{valor_consulta}%' OR TIPO LIKE '%{valor_consulta}%'")
        lista = list(lista)
        if not lista:
            return QMessageBox.Warning(QMessageBox(), f"Att: Usuário não encontrado!")
        else:
            self.tb_usuarios.setRowCount(0)
            for idxlinha, linha in enumerate(lista):
                self.tb_usuarios.insertRow(idxlinha)
                for idxcoluna, coluna in enumerate(linha):
                    self.tb_usuarios.setItem(idxlinha, idxcoluna, QTableWidgetItem(str(coluna)))
    # adiciona as informações do usuário no banco de dados clientes.db
    def cadastrar_cliente(self):
        dbc = DataBaseCliente("clientes.db")

        nome = self.txtNomeCliente.text()
        email = self.txtEmailCliente.text()
        telefone = self.txtTelefoneCliente.text()
        senha = self.txtSenhaCliente.text()

        if self.txtSenhaCliente.text() != self.txtConfirmarSenhaCliente.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Divergentes")
            msg.setText("As senhas não são iguais!")
            msg.exec_()

        if nome == "" or email == "" or telefone == "" or senha == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo vazio")
            msg.setText("Você esqueceu de preencher algumas informações!")
            msg.exec_()
        else:
            dbc.inserir_apaga_atualiza("INSERT INTO CLIENTE(NOME, EMAIL, TELEFONE, SENHA) VALUES('{}','{}','{}','{}')".format(nome, email, telefone, senha))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro realizado")
            msg.setText("Seu cadastro foi realizado com sucesso!")
            msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    app.exec_()

