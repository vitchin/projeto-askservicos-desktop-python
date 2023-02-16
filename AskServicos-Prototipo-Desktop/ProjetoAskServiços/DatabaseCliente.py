import sqlite3


class DataBaseCliente:

    # Inicia o banco de dados
    def __init__(self, banco=None):  # cria o banco de dados
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    # Cria uma conexão com o banco de dados
    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão criada com sucesso! Seja bem-vindo!")
        except sqlite3.Error as e:
            print("Não foi possível estabelecer conexão!")

    # Cria tabelas no banco de dados
    def criar_tabelas(self):
        cur = self.cursor
        cur.execute("""

            CREATE TABLE IF NOT EXISTS CLIENTE(

            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            TELEFONE TEXT NOT NULL,
            SENHA TEXT NOT NULL

            )""")

    # Função que pode executar as funções inserir, deletar e atualizar em SQL
    def inserir_apaga_atualiza(self, query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    # Pega as informações dos dados
    def pegar_dados(self, query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()


db = DataBaseCliente("clientes.db")
db.inserir_apaga_atualiza("")

#db.criar_tabelas()
