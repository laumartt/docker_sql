import mysql.connector
from mysql.connector import Error

try:
    conexion=mysql.connector.connect(
            user="root", 
            password="root", 
            host="localhost", 
            database="bdmysql",
            port="3307"
    )

    if conexion.is_connected():
        print('Conexion exitosa')
        InfoServer = conexion.get_server_info()
        print('Informacion del servidor:', InfoServer)

        '''
        Aqui podrian ponerse las ordenes. Ej:
        cursor = conexion.cursor()
        cursor.execute('SELECT database();')
        registro = cursor.fetchone()
        para mas resultados
        cursor.execute('SELECT * FROM tabla')
        resultados = cursor.fetchall()
        for i in resultados:
            print(i[0], i[1], i[2]...)

        cursor.execute('INSERT INTO tabla VALUES (valor1)')
        conexion.commit()   #Para confirmar inserción correcta
        '''
except Error as ex:
    print('Error durante la conexion:', ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print('La conexion ha finalizado')