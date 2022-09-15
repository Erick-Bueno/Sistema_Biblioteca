from banco import conectar_banco


class cadastro_livro:
    def inserir(self, livro_nome, livro_codigo, livro_editora, data_livro):
        self.sql = f"Insert into livros (codigo, Nome, Editora, ano) values ({livro_codigo}, '{livro_nome}', '{livro_editora}', '{data_livro}')"
        self.c = conectar_banco()
        self.c.executa_dml(self.sql)