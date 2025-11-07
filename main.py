import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
)
from ui_DesignAsk import Ui_JanelaPrincipal
from DatabaseManager import DatabaseManager

class JanelaPrincipal(QMainWindow, Ui_JanelaPrincipal):
    def __init__(self):
        super(JanelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Pesquisa de Serviços")
        appIcon = QIcon("Imagens/Logo.png")
        self.setWindowIcon(appIcon)

        self.setup_database()
        self.setup_connections()
        self.carregar_dados_usuario()

    def setup_database(self):
        with DatabaseManager("usuarios.db") as db:
            db.create_user_table()
        with DatabaseManager("clientes.db") as db:
            db.create_client_table()

    def setup_connections(self):
        self.btnCasa.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_inicial)
        )
        self.btnSobre.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_sobre)
        )
        self.btnContato.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_contato)
        )
        self.btnAnunciar.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_cadastro)
        )
        self.btnSolicitar.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_cliente)
        )
        self.btnVoltarInicio.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_inicial)
        )
        self.btnCancelarCliente.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_inicial)
        )
        self.btnCadastrar.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_escolha)
        )
        self.btnCancelar.clicked.connect(
            lambda: self.Paginas.setCurrentWidget(self.pg_inicial)
        )
        self.btnConcluir.clicked.connect(self.cadastrar_usuario)
        self.btnPesquisar.clicked.connect(self.pesquisar_dados)
        self.btnConcluirCliente.clicked.connect(self.cadastrar_cliente)

    def show_message(self, title, text, icon=QMessageBox.Information):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.exec_()

    def cadastrar_usuario(self):
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
            self.show_message(
                "Senhas Divergentes", "As senhas não são iguais!", QMessageBox.Warning
            )
            return

        if not all(
            [nome, email, telefone, rua, municipio, hora, dias, senha, tipo]
        ):
            self.show_message(
                "Campo vazio",
                "Você esqueceu de preencher algumas informações!",
                QMessageBox.Warning,
            )
            return

        query = """
            INSERT INTO USUARIO(NOME, EMAIL, TELEFONE, RUA, MUNICIPIO, HORA, DIAS, SENHA, TIPO)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (nome, email, telefone, rua, municipio, hora, dias, senha, tipo)

        with DatabaseManager("usuarios.db") as db:
            if db.execute_query(query, params):
                self.show_message(
                    "Cadastro realizado", "Seu cadastro foi realizado com sucesso!"
                )
                self.carregar_dados_usuario()
            else:
                self.show_message(
                    "Erro", "Não foi possível realizar o cadastro.", QMessageBox.Critical
                )

    def carregar_dados_usuario(self):
        with DatabaseManager("usuarios.db") as db:
            lista = db.fetch_all("SELECT * FROM USUARIO")

        self.tb_usuarios.setRowCount(0)
        self.tb_usuarios.setSortingEnabled(True)
        for row_number, row_data in enumerate(lista):
            self.tb_usuarios.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tb_usuarios.setItem(
                    row_number, column_number, QTableWidgetItem(str(data))
                )

    def pesquisar_dados(self):
        valor_consulta = self.CampoPesquisa.text()
        query = """
            SELECT * FROM USUARIO
            WHERE NOME LIKE ? OR RUA LIKE ? OR MUNICIPIO LIKE ? OR TIPO LIKE ?
        """
        params = (
            f"%{valor_consulta}%",
            f"%{valor_consulta}%",
            f"%{valor_consulta}%",
            f"%{valor_consulta}%",
        )

        with DatabaseManager("usuarios.db") as db:
            lista = db.fetch_all(query, params)

        if not lista:
            self.show_message("Atenção", "Usuário não encontrado!", QMessageBox.Warning)
        else:
            self.tb_usuarios.setRowCount(0)
            for row_number, row_data in enumerate(lista):
                self.tb_usuarios.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tb_usuarios.setItem(
                        row_number, column_number, QTableWidgetItem(str(data))
                    )

    def cadastrar_cliente(self):
        nome = self.txtNomeCliente.text()
        email = self.txtEmailCliente.text()
        telefone = self.txtTelefoneCliente.text()
        senha = self.txtSenhaCliente.text()

        if self.txtSenhaCliente.text() != self.txtConfirmarSenhaCliente.text():
            self.show_message(
                "Senhas Divergentes", "As senhas não são iguais!", QMessageBox.Warning
            )
            return

        if not all([nome, email, telefone, senha]):
            self.show_message(
                "Campo vazio",
                "Você esqueceu de preencher algumas informações!",
                QMessageBox.Warning,
            )
            return

        query = "INSERT INTO CLIENTE(NOME, EMAIL, TELEFONE, SENHA) VALUES(?, ?, ?, ?)"
        params = (nome, email, telefone, senha)

        with DatabaseManager("clientes.db") as db:
            if db.execute_query(query, params):
                self.show_message(
                    "Cadastro realizado", "Seu cadastro foi realizado com sucesso!"
                )
            else:
                self.show_message(
                    "Erro", "Não foi possível realizar o cadastro.", QMessageBox.Critical
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec_())

