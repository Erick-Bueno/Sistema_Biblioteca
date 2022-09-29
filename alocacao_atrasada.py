from banco import conectar_banco
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class aloc_atrasada:
    def alocs_atrasadas(self):
        self.sql = "select email from alocacao inner join livros on livros.id = alocacao.id_livro inner join clientes on clientes.id = alocacao.id_cliente where atraso = 'True' and estado = 'em andamento'"
        self.c = conectar_banco()
        self.c.executa_dql(self.sql)
        self.emails = self.c.dados
        


        host = "smtp.gmail.com"
        port = "587"
        usuario = "erickjb93@gmail.com"
        senha = "zrzhokxrkyzslcgd"

        servidor = smtplib.SMTP(host, port)

        servidor.ehlo()
        servidor.starttls()

        servidor.login(usuario, senha)

        corpo = f"o prazo de devolução do livro alocado acabou por favor devolva o livro imediatamente"
        msg_email = MIMEMultipart() #um email é codificado em mimemultipart
        msg_email["From"] = usuario
        msg_email["Subject"] = "Codigo de confirmação"
        msg_email.attach(MIMEText(corpo, 'plain'))#o conteudo do email é um texto normal 
        for c in range(len(self.emails)):
            servidor.sendmail(msg_email["From"],self.emails[c],msg_email.as_string())
            print("email enviado")
        servidor.quit()
