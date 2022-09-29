from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from banco import conectar_banco;


class estoque():
    def verificaEstoque(self, livro_alocado_validado):
       c = conectar_banco()
       self.sql10 = f"select count(Nome) from livros where Nome = '{livro_alocado_validado}' and Alocado = 'NÃO ALOCADO'"
       self.dados = c.executa_dql(self.sql10)

