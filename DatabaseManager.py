import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Conexão com o banco de dados '{self.db_name}' estabelecida.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print(f"Conexão com o banco de dados '{self.db_name}' fechada.")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao executar a query: {e}")
            return False

    def fetch_all(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar os dados: {e}")
            return []

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS USUARIO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            TELEFONE TEXT NOT NULL,
            RUA TEXT NOT NULL,
            MUNICIPIO TEXT NOT NULL,
            HORA TEXT NOT NULL,
            DIAS TEXT NOT NULL,
            SENHA TEXT NOT NULL,
            TIPO TEXT NOT NULL
        )
        """
        self.execute_query(query)

    def create_client_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS CLIENTE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            TELEFONE TEXT NOT NULL,
            SENHA TEXT NOT NULL
        )
        """
        self.execute_query(query)
