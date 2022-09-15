from datetime import date
from distutils.log import error
from banco import conectar_banco
from imgs import icones
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
import mysql.connector
from conexões import  Verify
from enviaremail import enviar_email
import re
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
import _thread
from verificar_estoque import estoque
from cadastrar_cliente import cadastro
from alocacao import alocar
from cadastrar_livro import cadastro_livro
from alocacao_atrasada import aloc_atrasada
from devolution import devo






class App(Verify):
    #carregando tela e passando as funcoes de evento
    def __init__(self):
        #funcão que e ativada sempre q o sistema inicia
        self.app = QtWidgets.QApplication([])
        self.livraria = uic.loadUi("app.ui")
        self.livraria.setWindowTitle("livraria")
        self.livraria.pushButton.clicked.connect(self.tela_clietes)
        self.livraria.pushButton_2.clicked.connect(self.tela_livros)
        self.livraria.pushButton_3.clicked.connect(self.tela_alocacao)
        self.livraria.pushButton_9.clicked.connect(self.tela_devolucao)
        self.livraria.pushButton_4.clicked.connect(self.fechar_sistema)
        self.livraria.pushButton_6.clicked.connect(self.adicionar_Livro)
        self.livraria.pushButton_7.clicked.connect(self.verificar_estoque)
        self.livraria.pushButton_8.clicked.connect(self.alocar)
        self.livraria.pushButton_10.clicked.connect(self.devolucao)
        #setando data atual no dateedit
        data_atual = date.today()
        Data_atual = QDate(data_atual)
        self.livraria.dateEdit.setDate(Data_atual)
        self.livraria.dateEdit_2.setDate(Data_atual)
        self.livraria.pushButton_5.clicked.connect(self.adicionar_cliente)
        self.verificando()
        self.enviarr_email()
        self.livraria.show()
        self.app.exec()
        _thread.start_new_thread(self.enviarr_email,("1",1))
  
        
        

        
        
    #metodo q direiciona para tela de cadastro de clientes
    def tela_clietes(self):
        self.livraria.frame.show()
        self.livraria.frame_3.hide()
        self.livraria.frame_4.hide()
        self.livraria.frame_5.hide()
    #metodo q direciona para tela de cadastro de livros
    def tela_livros(self):

        self.livraria.frame_3.show()
        self.livraria.frame_4.show()
        self.livraria.frame_5.show()
    #metodo q direciona para tela de alocação
    def tela_alocacao(self):
        self.livraria.frame_3.hide()
        self.livraria.frame_4.show()
        self.livraria.frame_5.hide()
        self.sql8 = "select Nome, Cpf from clientes order by Nome"
        self.con = mysql.connector.connect(host="localhost", user = "root", password = "sirlei231", database = "biblioteca")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.sql8)
        self.nomes = self.cursor.fetchall()
        self.con.close()
        self.cursor.close()
       
        self.livraria.tableWidget.setRowCount(len(self.nomes))
        self.livraria.tableWidget.setColumnCount(2)
        for c in range (len(self.nomes)):
            for i in range(0,2):
                self.livraria.tableWidget.setItem(c,i,QtWidgets.QTableWidgetItem(str(self.nomes[c][i])))

    #metodo q direciona para tela de devolução
    def tela_devolucao(self):
        self.livraria.frame_3.hide()
        self.livraria.frame_4.show()
        self.livraria.frame_5.show()
    #metodo q fecha o sistema
    def fechar_sistema(self):
        self.livraria.close()
    #metodo q adiciona um novo registro de livro no database
    def adicionar_Livro(self):
        try:
            self.nome_livro = self.livraria.lineEdit_8.text()
            self.nome_livro_validado = self.nome_livro.upper().replace(" ", "")
            self.codigo_livro = self.livraria.lineEdit_11.text()
            self.editora_livro = self.livraria.lineEdit_9.text()
            self.ano_livro = self.livraria.dateEdit.date().toPyDate()
            #validações/tratamento]
            if self.nome_livro == "" or self.codigo_livro == "" or self.editora_livro == "":
                return QMessageBox.warning(self.livraria, "Erro", "preencha todos os campos")
            #dps de tudo validado é chamada a classe cadastrar_livro;
            self.c = cadastro_livro()
            self.c.inserir(self.nome_livro_validado,self.codigo_livro, self.editora_livro, self.ano_livro)
            QMessageBox.about(self.livraria,"aviso", "livro adicionado com sucesso")
        except mysql.connector.errors.ProgrammingError:
            QMessageBox.warning(self.livraria,"erro", "codigo invalido, por favor insire apenas os numeros")
    def adicionar_cliente(self):
        self.nome_cliente = self.livraria.lineEdit.text() 
        self.telefone = self.livraria.lineEdit_3.text()
        self.cpf = self.livraria.lineEdit_2.text()
        self.email = self.livraria.lineEdit_4.text()
        self.bairro = self.livraria.lineEdit_7.text()
        self.numero = self.livraria.lineEdit_5.text()
        self.rua = self.livraria.lineEdit_6.text()
        if self.nome_cliente == ""   or self.telefone == "" or self.cpf == "" or self.email == "" or self.bairro == ""  or self.numero == "" or self.rua == "":
            return QMessageBox.warning(self.livraria, "erro", "preencha todos os campos")
        self.cpf_validator = re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', self.cpf)
        if self.cpf_validator == []:
         return QMessageBox.warning(self.livraria,"erro", "insira um cpf valido seguindo o padrão xxx.xxx.xxx-xx" )
        self.nome_cliente_validador = re.findall(r'^[a-zA-Z]{1,}',self.nome_cliente)
        if self.nome_cliente_validador == []:
            return QMessageBox.warning(self.livraria,"erro","insira um nome valido")
        self.i = cadastro()
        self.i.inserir_client(self.nome_cliente, self.cpf_validator[0], self.telefone, self.email, self.numero, self.rua, self.bairro)
        return QMessageBox.about(self.livraria,"aviso","cadastro realizado com sucesso")
    def verificar_estoque(self):
        self.nome_livro_alocado = self.livraria.lineEdit_10.text()
        self.nome_livro_alocado_validado = self.nome_livro_alocado.upper().replace(" ", "")
        if self.nome_livro_alocado == "":
            return QMessageBox.about(self.livraria,"aviso", "informe um livro")
        self.v = estoque()
        self.v.verificaEstoque(self.nome_livro_alocado_validado)
        QMessageBox.about(self.livraria, "aviso", f"estoque atual de {self.v.dados[0][0]}")
    def alocar(self):
       try:
            
            self.codigo_livro_alocado = self.livraria.lineEdit_12.text()
            if self.codigo_livro_alocado == "":
                    return QMessageBox.warning(self.livraria, "erro", "insira o codigo do livro a ser alocado")
        
            self.cliente_cpf = self.livraria.tableWidget.currentItem().text()
            self.data_alocacao = self.livraria.dateEdit_2.date().toPyDate()
                #verificar se cliente esta bloqueado
            self.d = alocar()
            self.d.verificar_status_block(self.cliente_cpf)
            self.status = self.d.c.dados
            if self.status[0][0] == "True":
                return QMessageBox.warning(self.livraria, "erro", "usuario bloqueado")
                #pegar id do livro pelo codigo
            self.b = alocar()
            self.b.pegar_id_livro(self.codigo_livro_alocado)
            self.idlivro = self.b.c.dados[0][0]
            print(self.idlivro)
            
            #pegar id do cliente pelo cpf
            self.a = alocar()
            self.a.pegar_id_cliente(self.cliente_cpf)
            self.id_cliente = self.a.c.dados[0][0]
                #atualizar livro para alocado
            self.a.atualizar_para_alocado(self.codigo_livro_alocado)
                #caso a alocação for feita a partir da seleção do nome
            self.a = alocar()
            self.a.nome_selecionado(self.cliente_cpf)
            if self.a.verificar_dado_selecionado == []:
                    return QMessageBox.warning(self.livraria, "aviso","selecione o cpf do cliente especifico para efetuar alocação")
            #inserir dados na tabela de alocacao
            self.a = alocar()
            self.a.inserir_alocacao(self.id_cliente,self.idlivro,self.data_alocacao)
            QMessageBox.about(self.livraria,"aviso","livro alocado")
       except IndexError:
        QMessageBox.warning(self.livraria,"erro","nenhum livro encontrado com este codigo") 
       except AttributeError:
        QMessageBox.warning(self.livraria, "erro","selecione o cpf do cliente antes de alocar")  
               
      
    def enviarr_email(self):
       
        self.z = aloc_atrasada()
        self.z.alocs_atrasadas()
 
    def devolucao(self):
        try:
            self.codigo_livro_devoluir = self.livraria.lineEdit_13.text()
            self.intercorrencia = self.livraria.textEdit.toPlainText()
            if self.codigo_livro_devoluir == "":
                return QMessageBox.warning(self.livraria,"aviso", "insira um codigo antes de prosseguir com a devolução")
            self.x = devo()
            self.x.atualizar_alocado(self.codigo_livro_devoluir)
            self.x.selecionar_id_cliente(self.codigo_livro_devoluir,self.intercorrencia)
            QMessageBox.warning(self.livraria,"aviso","devolução feita com sucesso")
        except IndexError as error:
            QMessageBox.warning(self.livraria,"erro",f"{error}")

  
        

        

        

    
        
        
        
    



       
   
        

App()

