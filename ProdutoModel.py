from Model import Model

class ProdutoModel(Model):
    def __init__(self):
        super().__init__()
        self.createTable()
    def createTable(self):
        #cria tabela se não existir
        super().insert("CREATE TABLE IF NOT EXISTS public.\"PRODUTO\" (\"id\" SERIAL NOT NULL, \"codigo\" VARCHAR(50) NOT NULL,  \"nome\" VARCHAR(50) NOT NULL, \"preco\" FLOAT NOT NULL, CONSTRAINT \"PRODUTO_pkey\" PRIMARY KEY (\"id\"))")
    def select(self):
        return super().select("SELECT id, codigo, nome, preco FROM public.\"PRODUTO\"")
    def insert(self, codigo, nome, preco):
        return super().insert("INSERT INTO public.\"PRODUTO\" (\"codigo\", \"nome\", \"preco\") VALUES ('{}', '{}', '{}')".format(codigo, nome, preco))
    def update(self, id, codigo, nome, preco):
        super().update("UPDATE public.\"PRODUTO\" SET  \"codigo\"='{}', \"nome\"='{}', \"preco\"='{}' WHERE \"id\"={}".format(codigo, nome, preco, id))
    def delete(self, id):
        super().delete("DELETE FROM public.\"PRODUTO\" WHERE \"id\"={}".format(id))