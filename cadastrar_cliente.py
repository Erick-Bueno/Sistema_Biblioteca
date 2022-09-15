from banco import conectar_banco


class cadastro:

    def inserir_client(self,nome_cliente, cpf_validator, telefone, email, numero, rua,bairro):
       c = conectar_banco()
       self.sql =  f"insert into clientes(Nome, Cpf, Telefone, Email, Numero, Rua, Bairro) values ('{nome_cliente}', '{cpf_validator}', '{telefone}','{email}','{numero}','{rua}', '{bairro}')"
       c.executa_dml(self.sql)
      
