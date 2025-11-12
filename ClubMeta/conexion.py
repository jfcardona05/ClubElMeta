import mysql.connector

def conexion():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  #usuario de MySQL
        password='',  #contraseña de MySQL
        database='club_meta'  #Nombre de tu base de datos
    )
    return connection
