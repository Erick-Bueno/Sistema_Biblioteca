from banco import conectar_banco


class devo: 
    def atualizar_alocado(self,codigo):
        self.sql = f"update livros set Alocado = 'NÃO ALOCADO' where codigo = {codigo}"
        self.c = conectar_banco()
        self.c.executa_dml(self.sql)
    def selecionar_id_cliente(self, codigo, inter = 0):
            if inter != 0:
                self.sql2 = f"select id_cliente from alocacao inner join livros on livros.id = alocacao.id_livro inner join clientes on clientes.id = alocacao.id_cliente where codigo = {codigo}"
                self.d = conectar_banco()
                self.d.executa_dql(self.sql2)
                self.cliente_id2 = self.d.dados[0][0]
                self.sql9 = f"update alocacao set intercorrencia = '{inter}' where id_cliente = {self.cliente_id2}"
                self.u = conectar_banco()
                self.u.executa_dml(self.sql9)
            self.sql2 = f"select id_cliente from alocacao inner join livros on livros.id = alocacao.id_livro inner join clientes on clientes.id = alocacao.id_cliente where codigo = {codigo}"
            self.d = conectar_banco()
            self.d.executa_dql(self.sql2)
            print(self.d.dados)

        
            
    
       