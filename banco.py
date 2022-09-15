import mysql.connector


class conectar_banco:

        
    def conectar(self):
        try:
            self.con = mysql.connector.connect(host = "localhost", password = "sirlei231", user="root", database="biblioteca")
            self.cursor = self.con.cursor()
        except mysql.connector.Error as erro:
            return erro

    def desconectar(self):
        self.con.close()
        self.cursor.close()

    def executa_dql(self,sql):
        self.conectar()
        self.cursor.execute(sql)
        self.dados = self.cursor.fetchall()
        self.desconectar()
        return self.dados
    def executa_dml(self,sql):
        self.conectar()
        self.cursor.execute(sql)
        self.con.commit()
        self.desconectar()
        