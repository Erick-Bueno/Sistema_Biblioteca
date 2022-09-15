from banco import conectar_banco
import re


class alocar:

    def pegar_id_livro(self, codigo_livro_alocado):
        self.sql = f"select id from livros where codigo = {codigo_livro_alocado}"
        self.c = conectar_banco()
        self.c.executa_dql(self.sql)
        self.idLivro = self.c.dados[0]
    def atualizar_para_alocado(self, codigo_livro_alocado):
        self.sql2 =  f"update livros set Alocado = 'ALOCADO' where codigo = {codigo_livro_alocado}"
        self.c = conectar_banco()
        self.c.executa_dml(self.sql2)
    def nome_selecionado(self, cliente_nome):
        self.verificar_dado_selecionado =  re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}',cliente_nome)
    def verificar_status_block(self, cpf):
        self.sql3 = f"select Bloqueado from clientes where Cpf = '{cpf}'"
        self.c = conectar_banco()
        self.c.executa_dql(self.sql3)
        
    def pegar_id_cliente(self, cpf):
        self.sql5 = f"select id from clientes where Cpf = '{cpf}'"
        self.c = conectar_banco()
        self.c.executa_dql(self.sql5)
        self.idCliente = self.c.dados[0]
       
    def inserir_alocacao(self,idCliente, idLivro, dataa):
        print(idCliente)
        print(idLivro)
        print(dataa)
        self.sql4 = f"insert into alocacao(id_livro, id_cliente, dataa) values({idLivro}, {idCliente}, '{dataa}')"
        self.c = conectar_banco()
        self.c.executa_dml(self.sql4)
        print(idCliente)
    

