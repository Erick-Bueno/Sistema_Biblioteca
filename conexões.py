from socketserver import DatagramRequestHandler
from threading import local
import mysql.connector
from http import server
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

from banco import conectar_banco

class Verify:
    def __init__(self):
        pass
    def verificando(self):
       print("verificando")
       self.data_atual = date.today()
       self.sql2 = "select dataa from alocacao inner join clientes on clientes.id = alocacao.id_cliente inner join livros on livros.id = alocacao.id_livro where estado = 'Em andamento'"
       self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
       self.cursor = self.con.cursor()
       self.cursor.execute(self.sql2)
       self.datas = self.cursor.fetchall()
       self.cursor.close()
       self.con.close()
    
       
       for c in range(len(self.datas)):
        self.dataa = self.data_atual > self.datas[c][0]
        if self.dataa == True:
            self.sql3 = f"update alocacao set alocacao.atraso = 'True' where alocacao.dataa = '{self.datas[c][0]}' and estado = 'Em andamento'"
            self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql3)
            self.con.commit()
            self.cursor.close()
            self.cursor.close()
            self.sql4 = f"select clientes.Nome from alocacao inner join clientes on clientes.id = alocacao.id_cliente inner join livros on livros.id = alocacao.id_livro where alocacao.dataa='{self.datas[c][0]}' and atraso = 'True' "
            self.con = mysql.connector.connect(host = "localhost", user = "root", password= "sirlei231", database = "biblioteca")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql4)
            self.user_name = self.cursor.fetchall()
            self.con.close()
            self.cursor.close()
            
            for i in range(len(self.user_name)):
                self.sql5 = f"update clientes set Bloqueado = 'True' where Nome = '{self.user_name[i][0]}'"
                self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
                self.cursor = self.con.cursor()
                self.cursor.execute(self.sql5)
                self.con.commit()
                self.cursor.close()
                self.cursor.close()
       
    

   

    
            
              
                
        