import psycopg2

class Model():
    def __init__(self):
        print('Model')
        # self.conexao = psycopg2.connect(database = "postgres", user = "postgres", password = "poi123", host = "localhost", port = "5432")
        # self.cursor = self.conexao.cursor()
    def abrirConexao(self):
        try:
            self.conexao = psycopg2.connect(user="postgres", password="poi123", host="127.0.0.1", port="5432", database="postgres")
            self.cursor = self.conexao.cursor()
        except (Exception, psycopg2.Error) as error :
            if(self.conexao):
                print("Falha ao se conectar ao Banco de Dados", error)
    def fecharConexao(self):
        if (self.conexao):
            self.cursor.close()
            self.conexao.close()
            print("A conexão com o PostgreSQL foi fechada.")
    def __del__(self):
        self.conexao.close()
    def select(self, sql):
        try:
            self.abrirConexao()
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)
        finally:
            self.fecharConexao()
        return registros
    def insert(self, sql):
        try:
            self.abrirConexao()
            self.cursor.execute(sql)
            self.conexao.commit()
            count = self.cursor.rowcount
            return self.cursor.lastrowid
        except (Exception, psycopg2.Error) as error :
            if(self.conexao):
                print("Falha ao inserir registros na tabela", error)
        finally:
            self.fecharConexao()
    def update(self, sql):
        try:
            self.abrirConexao()
            self.cursor.execute(sql)
            self.conexao.commit()
            count = self.cursor.rowcount
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)    
        finally:
            self.fecharConexao()
        return count
    def delete(self, sql):
        try:
            self.abrirConexao()
            self.cursor.execute(sql)
            self.conexao.commit()
            count = self.cursor.rowcount
            print(count, "Registro excluído com sucesso! ")        
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)    
        finally:
            self.fecharConexao()
        return count